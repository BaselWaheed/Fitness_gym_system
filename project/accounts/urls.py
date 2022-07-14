from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.homepage , name = 'homepage') ,

    path('register/staff/' , login_required(views.Register_staff.as_view(),login_url='/accounts/login/staff/?next=/accounts/'), name= 'register_staff'),

    path('login/staff/' , views.Login_staff.as_view() , name= 'login_staff'),

    path('logout/staff/' , login_required(views.LogoutView.as_view(),login_url='/accounts/login/staff/?next=/accounts/') , name= 'logout_staff'),


    path('setting/staff/' , login_required(views.Setting_Staff.as_view(),login_url='/accounts/login/staff/?next=/accounts/') , name= 'setting'),

]
