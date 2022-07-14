from django.urls import path 
from . import views 
from django.contrib.auth.decorators import login_required
urlpatterns = [


    path('add_newCustomer/',login_required(views.Add_NewCustomer.as_view(),login_url='/accounts/login/staff/?next=/accounts/'), name = 'add_newCustomer'),


    path('update/<int:id>/',login_required(views.UpdateCustomer.as_view() ,login_url='/accounts/login/staff/?next=/accounts/'), name='update_customer'),


    path('add_oldCustomer/',login_required(views.Add_OldCustomer.as_view(),login_url='/accounts/login/staff/?next=/accounts/'), name ='Add_OldCustomer'),


    path('customer/', login_required(views.CustomerListView.as_view() ,login_url='/accounts/login/staff/?next=/accounts/'), name= 'customer_list'),


    path('check/',login_required(views.CheckView.as_view(),login_url='/accounts/login/staff/?next=/accounts/'), name='checkview'),


    path('delete/<int:id>/',login_required(views.deletebook,login_url='/accounts/login/staff/?next=/accounts/'), name='delete_customer'),

    path('profile/<int:pk>/',login_required(views.UserDetailView.as_view(),login_url='/accounts/login/staff/?next=/accounts/'), name='profile_staff'),





    
    
]
