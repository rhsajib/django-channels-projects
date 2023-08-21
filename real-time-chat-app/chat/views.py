from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm



def frontpage(request):
    return render(request, 'chat/index.html')


def signup_view(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('frontpage')
    
    return render(request, 'chat/signup.html', {'form': form})