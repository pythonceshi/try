from time import sleep

from django.contrib.auth import authenticate
from django.core.serializers import json
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from django.contrib import messages
from twisted.mail.test.test_imap import Account


from mysql02.models import manhuainfo
from mysql02.models import maninfo
import random
import datetime
from django.core.paginator import Paginator,EmptyPage
def manhua(request):
    all_books = manhuainfo.objects.all()
    paginator = Paginator(all_books, 10)
    page1 = paginator.page(1)  # 第一页的page对象；page1可进行迭代处理
    print("objects_list", page1.object_list)  # page1.object_list：这一页所有的model记录对象；QuerySet类型
    current_page_num = int(request.GET.get("page", 1))  # get中的1表示默认获取到的值
    if paginator.num_pages > 11:

        if current_page_num - 5 < 1:
            page_range = range(1,12)
        # 如果当前页为最后面的5个， 则要让 page_range 固定为 range(paginator.num_pages-10,paginator.num_pages+1) （即最后面的11个页码）
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages-10,paginator.num_pages+1)
        else: # 中间的情况
            page_range = range(current_page_num-5,current_page_num+6)
    else:
        # 如果小于11页，就显示全部页码
        page_range = paginator.page_range

    # 如果页码错误（current_page_num不在有效页码范围之内），就让其显示第一页
    try:

        current_page = paginator.page(current_page_num)  # 当前页



    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request,"manhua.html",locals())






def addbook(request):
# 由于templates/addbook.html 中 form标签的 action没写，所以还是提交到了当前页面index.html
    if request.method == "POST":
        num = request.POST.get("num")
        name = request.POST.get("name")
        author = request.POST.get("author")

        com = request.POST.get("com")
        new = request.POST.get("new")
        pop = request.POST.get("pop")
        type1 = request.POST.get("type")
        pho = '/1/'+num+'.jpg'
        link = request.POST.get("link")

        # 添加记录
        book_obj = manhuainfo.objects.create(num=num,name=name,author=author,com=com,new=new,pop=pop,type=type1,pho=pho,link=link)

        return redirect("/")

    return render(request,"add.html")
def index(request):
    try:
        yonghu = maninfo.objects.get(on=1)
        print(yonghu)
    except :

        yonghu = maninfo.objects.get(off=1)


    if request.method == "POST":
        print('1')

        tags1 = request.POST.getlist('up')
        tags2 = request.POST.getlist('in')
        tags3 = request.POST.getlist('down')
        tags4 = request.POST.getlist('check')
        tags5 = request.POST.getlist('change')
        print(tags1,tags2,tags3,tags4,tags5)


        if tags2==["Sign in"] :
            print('denglu')
            email1 = request.POST.get('EMAIL1', False)
            password = request.POST.get('PASSWORD', False)
            if email1 and password:  # 确保用户名和密码都不
                user = maninfo.objects.get(mail=email1)
                print(user)
                if user.password == password:
                    print('1')
                    maninfo.objects.filter(mail=email1).update(on=1)
                    return redirect('/index.html')
                else :
                    return redirect('/in1.html')


        if tags1==["Sign Up"]:
            print('zhuce')
            email2 = request.POST.get('EMAIL2', False)
            # request.POST.get('is_private', False)
            username = request.POST.get('USERNAME', False)
            password_in = request.POST.get('PASSWORD_IN', False)
            password_out = request.POST.get('PASSWORD_CONFIRM', False)
            print(email2, username,password_in ,password_out)
            if 1:  # 确保用户名和密码都不为空
                print('1')
                if len(password_in)<10:
                    return redirect('/in2.html')
                if password_in == password_out:
                    dic = { "username": username, "password": password_in, "mail": email2}
                    print(dic)
                    maninfo.objects.create(**dic)
                    return redirect('/index.html')
                else :
                    return redirect('/in3.html')

        if tags3 == ["注  销"]:
            print('zhuxiao')
            maninfo.objects.update(on=0)
            return redirect('/index.html')

        if tags4==["check"] :
            print('check')
            email1 = request.POST.get('EMAIL2', False)
            username = request.POST.get('USERNAME', False)
            if 1:  # 确保用户名和密码都不为空
                try:
                    user = maninfo.objects.get(mail=email1)
                except :
                    return redirect('/in4.html')
                print(user)
                if user.username == username:
                    print('1')
                    maninfo.objects.filter(mail=email1).update(change=1)
                    return redirect('/index.html')
                else :
                    return redirect('/in5.html')

        if tags5 == ["change"]:
            print('change')

            password_in = request.POST.get('PASSWORD_IN', False)
            password_out = request.POST.get('PASSWORD_CONFIRM', False)
            print(password_in, password_out)

            if 1:  # 确保用户名和密码都不为空
                print('1')
                if password_in == password_out:
                    try:
                        maninfo.objects.filter(change=1).update(password=password_in)
                        maninfo.objects.update(change=0)
                    except:

                        return redirect('/in6.html')


                    return redirect('/index.html')


    return render(request, "index.html", locals())

# def blog(request):
#     return render(request, "blog-3-column.html")

def blog(request):
    all_books = manhuainfo.objects.all()
    paginator = Paginator(all_books, 12)
    page1 = paginator.page(1)  # 第一页的page对象；page1可进行迭代处理
    print("objects_list", page1.object_list)  # page1.object_list：这一页所有的model记录对象；QuerySet类型
    current_page_num = int(request.GET.get("page", 1))  # get中的1表示默认获取到的值
    if paginator.num_pages > 11:

        if current_page_num - 5 < 1:
            page_range = range(1,12)
        # 如果当前页为最后面的5个， 则要让 page_range 固定为 range(paginator.num_pages-10,paginator.num_pages+1) （即最后面的11个页码）
        elif current_page_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages-10,paginator.num_pages+1)
        else: # 中间的情况
            page_range = range(current_page_num-5,current_page_num+6)
    else:
        # 如果小于11页，就显示全部页码
        page_range = paginator.page_range

    # 如果页码错误（current_page_num不在有效页码范围之内），就让其显示第一页
    try:

        current_page = paginator.page(current_page_num)  # 当前页



    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request,"blog-3-column.html",locals())
def about(request):
    return render(request, "other-features.html")
def search(request):
    if 's' in request.GET:
        sss = request.GET['s']
        print(sss)
        messages.success(request, "哈哈哈哈")
        p_books = manhuainfo.objects.filter(name__contains=sss)
        paginator = Paginator(p_books, 12)
        page1 = paginator.page(1)  # 第一页的page对象；page1可进行迭代处理
        print("objects_list", page1.object_list)  # page1.object_list：这一页所有的model记录对象；QuerySet类型
        current_page_num = int(request.GET.get("page", 1))  # get中的1表示默认获取到的值
        if paginator.num_pages > 11:

            if current_page_num - 5 < 1:
                page_range = range(1, 12)
            # 如果当前页为最后面的5个， 则要让 page_range 固定为 range(paginator.num_pages-10,paginator.num_pages+1) （即最后面的11个页码）
            elif current_page_num + 5 > paginator.num_pages:
                page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
            else:  # 中间的情况
                page_range = range(current_page_num - 5, current_page_num + 6)
        else:
            # 如果小于11页，就显示全部页码
            page_range = paginator.page_range

        # 如果页码错误（current_page_num不在有效页码范围之内），就让其显示第一页
        try:

            current_page = paginator.page(current_page_num)  # 当前页



        except EmptyPage as e:
            current_page = paginator.page(1)

    return render(request, "search.html", locals())

def about1(request):
    sleep(5)
    return render(request, "in1.html")
def about2(request):
    sleep(5)
    return render(request, "in2.html")
def about3(request):
    sleep(5)
    return render(request, "in3.html")
def about4(request):
    sleep(5)
    return render(request, "in4.html")
def about5(request):
    sleep(5)
    return render(request, "in5.html")
def about6(request):
    sleep(5)
    return render(request, "in6.html")
def about7(request):
    sleep(5)
    return render(request, "in7.html")





