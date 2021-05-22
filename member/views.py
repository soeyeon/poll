from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import BoardMember

def home(request):
    return render(request, 'home.html')

def login(request):
    if request == "POST":
        form = LoginForm(request.POST)
        # 폼 객체, 폼 클래스를 만들 때 괄호에 POST 데이터를 담아준다.
        # POST 안에 있는 데이터가 form 변수에 들어간다.
        if form.is_valid(): # 장고 폼에서 제공하는 검증 함수 is_valid()
            # session_code 검증
            return redirect('/')
    else:
        form = LoginForm()
        # 빈 클래스 변수를 만든다.
    return render(request, 'login.html', {'form':form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        #print (request.POST)
        username    = request.POST.get('username', None)
        #print(username)
        password    = request.POST.get('password', None)
        #print(password)
        re_password = request.POST.get('re_password', None)
        #print(re_password)
        email       = request.POST.get('email', None)


        res_data = {}
        if not (username and password and re_password and email):
            res_data['error'] = '모든 값을 입력하세요!'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
            print(res_data)

        else:
            member = BoardMember(
                username    = username,
                email       = email,
                password    = make_password(password)
            )
            member.save()

        return render(request, 'register.html', res_data)