from django.shortcuts import get_object_or_404, redirect, render 
from accounts.models import Customer, Permission, User
from staff.models import Booking
from . import forms 
from django.http import HttpResponseRedirect , HttpResponse  
from django.views import View
from django.views.generic import ListView , DetailView
# Create your views here.




#staff can register  new customer here 
class Add_NewCustomer(View):
    login_required = True
    form_class = forms.CustomerBooking
    initial = {'key': 'value'}
    template_name = 'staff/add_customer.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/')

        return render(request, self.template_name, {'form': form})



# staff can update customer here
class UpdateCustomer(View):
    form_class = forms.BookingForm
    initial = {'key': 'value'}
    template_name = 'staff/update_customer.html'

    def get(self, request, id, **kwargs):
        try :
            booking = Booking.objects.get(customer=id)
            customer = Customer.objects.get(id_number=id)
        except:
            return HttpResponse("<h1>Exception: Data not found</h1>")  
        form = self.form_class(instance=booking)
        form_2 = forms.CustomerForm(instance=customer)
        return render(request, self.template_name, {'form': form, 'Form':form_2})

    def post(self, request,id ):
        booking = Booking.objects.get(customer=id)
        customer = Customer.objects.get(id_number=id)
        form = self.form_class(request.POST , instance=booking)
        form_2 = forms.CustomerForm(request.POST,instance=customer)
        if form.is_valid() and form_2.is_valid():
            booking.calc_book_end()
            booking.calc_total_price()
            form.save()
            form_2.save()
            return HttpResponseRedirect('/accounts/')

        return render(request, self.template_name, {'form': form })


def deletebook(request , id ):
    book_id = get_object_or_404(Booking,id=id)
    if request.method =="GET":
        book_id.delete()
        return redirect('homepage')
    return render(request,'lms_app/delete.html')





# staff can add old customer
class Add_OldCustomer(View):
    form_class = forms.Add_OldCustomerForm
    initial = {'key': 'value'}
    template_name = 'staff/add_customer.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/')

        return render(request, self.template_name, {'form': form})




class CustomerListView(ListView):
    model = Booking
    
    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        permission = Permission.objects.get(title='deletecustomer')
        user = User.objects.get(username=self.request.user)
        if permission in user.permission.all() : 
            context['some_data'] = True
        else :
            context['some_data'] = False
        return context




class CheckView(View):
    
    initial = {'key': 'value'}
    template_name = 'staff/check_customer.html'

    def get(self, request, *args, **kwargs):
        name = request.GET.get('search')

        try:
            if Customer.objects.filter(username=name):
                customer_1 = Customer.objects.get(username=name)
            elif Customer.objects.filter(id_number=int(name)):
                customer_1 = Customer.objects.get(id_number=int(name))
            else:
                pass
            booking_name = Booking.objects.get(customer=customer_1.id_number , is_active=True)
            c = booking_name.calc_is_active()
            booking_name.is_active = c[0]
            booking_name.save()
        
        except :
            return render(request, self.template_name ,{
                'message': "No User Subscription Found for id please enter username or id correctly" })
    
        return render(request, self.template_name, {
            'message':c[1],
            'time': c[2],
            'active':c[0] ,
            'booking_name':booking_name,

        })


    

class UserDetailView(DetailView):
    model = User
    pk_url_kwarg = 'pk'
    context_object_name = 'obj'
    template_name = 'staff/staff_details.html'
    
    

