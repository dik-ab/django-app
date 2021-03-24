from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic.edit import (CreateView, FormView)
from django.views.generic.base import TemplateView, View
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView



class HomeView(TemplateView):
    template_name = 'home.html'



class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = UserLoginForm

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
                login(request, user)
        return redirect('accounts:home')
    

class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)



class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm