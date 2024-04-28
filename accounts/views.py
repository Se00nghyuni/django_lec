from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:  # GET 요청일 때는 폼을 초기화하여 사용자에게 보여줍니다.
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
