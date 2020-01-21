from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

from movie.models import MoviesRent, UpdateLog, UserSaleHistory

def registration_view(request):

    content = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            content['registration_form'] = form
    else:
        form = RegistrationForm()
        content['registration_form'] = form
    
    return render(request, 'account/register.html', content)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    content = {}
    
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    content['login_form'] = form
    return render(request,'account/login.html', content)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    content = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                    "email": request.POST['email'],
                    "username": request.POST['username'],
                 }
            form.save()
            content['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
               initial= {
                   "email" : request.user.email,
                   "username" : request.user.username,
                        }
               )
    content['account_form'] = form
    movie_list = MoviesRent.objects.filter(owner=request.user)
    content['movie_list'] = movie_list
    movie_log = UpdateLog.objects.filter()
    content['movie_log'] = movie_log
    movie_purchase = UserSaleHistory.objects.filter(user=request.user)
    content['movie_purchase'] = movie_purchase
    return render(request, 'account/account.html', content)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html',{})


