from django.contrib.auth.hashers import check_password

from django import forms
from .models import Board

class BoardForm(forms.Form):
    # 입력받을 값 두개
    title = forms.CharField(error_messages={
        'required': '제목을 입력하세요.'
    }, max_length=100, label="게시글 제목")
    contents = forms.CharField(error_messages={
        'required': '내용을 입력하세요.'
    }, widget=forms.Textarea, label="게시글 내용")
    if username and password:
        try:
            member = BoardMember.objects.get(username=username)
        except BoardMember.DoesNotExist:
            self.add_error('username', '아이디가 없습니다!')
            return
            # 예외처리를 하고 return 을 실행해서 바로 아래 코드를 실행하지 않고 빠져나오게 한다.

        if not check_password(password, member.password):
            self.add_error('password', '비밀번호가 다릅니다!')
        else:
            self.user_id = member.id