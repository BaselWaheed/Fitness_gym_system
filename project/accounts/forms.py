from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  User
from django.contrib.auth import authenticate, login, logout


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff = True
        if commit:
            user.save()
        return user





class MyUserChangeForm(UserChangeForm):
    class Meta():
        model = User
        fields = ('username',)






class MyUserLoginForm(forms.Form):
    username=forms.CharField(required=True)
    password1 = forms.CharField(required=True)


    def clean(self):
        user_name = self.cleaned_data["username"]
        password = self.cleaned_data["password1"]

        user = authenticate(username=user_name, password=password)
        if user is None:
            raise forms.ValidationError("Email or password incorrect")
        
        if not user.is_active :
            raise forms.ValidationError("Email or password incorrect please ")

        
        return user 
    