from django.shortcuts import redirect, render
from .models import User
from . import forms
from django.views import View
from django.http import HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
# Create your views here.





@login_required()
def homepage(request):
   
    return render(request, 'staff/homepage.html')




class Register_staff(View):
    form_class = forms.MyUserCreationForm
    initial = {'key': 'value'}
    template_name = 'accounts/add_staff.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/')

        return render(request, self.template_name, {'form': form})


class Login_staff(View):
    form_class = forms.MyUserLoginForm
    initial = {'key': 'value'}
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            login(request , user)
            return HttpResponseRedirect('/accounts/')

        return render(request, self.template_name, {'form': form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/accounts/login/staff/')






class Setting_Staff(TemplateView):
    template_name = 'accounts/setting.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Setting_Staff, self).get_context_data(*args, **kwargs)
        context['data'] = User.objects.filter(is_staff=True)
        return context