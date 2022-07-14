from django import forms 
from accounts.models import Customer
from .models import Booking

# for new customer
class CustomerBooking(forms.ModelForm):
    username = forms.CharField(required=True)
    phone_number = forms.CharField(required=True , max_length=11)
    class Meta:
        model = Booking
        fields = [
            'username',
            'phone_number' ,
            'offer',
            'book_start',
            ]
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        
        if Customer.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError('user has register before')
        return phone

    def save(self, commit=True):
        customer_1 = Customer(
            
            username = self.cleaned_data.get('username'),
            phone_number = self.cleaned_data.get('phone_number'),
        )
        customer_1.save()
        book = Booking(
            offer = self.cleaned_data.get('offer'),
            book_start = self.cleaned_data.get('book_start'),
            customer = customer_1
        )
        book.calc_book_end()
        book.calc_total_price()
        book.save()
        return customer_1 , book



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'username',
            'phone_number' ,
        ]
        


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'customer',
            'offer',
            'book_start', 
        ]

  


class Add_OldCustomerForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'customer',
            'offer',
            'book_start',
        ]
        widgets = {
            'customer' : forms.TextInput()
        }

    def clean_customer(self):
        data = self.cleaned_data["customer"]
        if Booking.objects.filter(customer=data , is_active=True):
            raise forms.ValidationError("the user is already booking ")
        return data
    
    def save(self):
        try :
            book = Booking(
                customer = self.cleaned_data.get('customer'),
                offer = self.cleaned_data.get('offer'),
                book_start = self.cleaned_data.get('book_start'),
            )
            book.calc_book_end()
            book.calc_total_price()
            book.save()
            return book
        except:
            raise forms.ValidationError("ERROR")
  
        




    


    




