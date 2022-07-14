from django.db import models
import datetime
from accounts.models import Customer 
import pandas as pd 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _




class Offers(models.Model):
    describtion = models.TextField(_("describe"))
    price = models.IntegerField(_("price"))
    count = models.PositiveIntegerField(_("month"))
    def __str__(self):
        return  self.describtion


    

class Booking(models.Model):
    customer = models.ForeignKey( Customer , verbose_name=_("user"), on_delete=models.CASCADE)  
    offer = models.ForeignKey(Offers, verbose_name=_("offer"), on_delete=models.CASCADE)  
    book_start = models.DateField(_("start"),  blank=True,default=timezone.now)
    book_end = models.DateField(_("end"), null =True , blank=True)
    is_active = models.BooleanField(_("active"),default=True , blank=True)
    total_price = models.DecimalField(_("total_price"), max_digits=5, decimal_places=2 , blank=True)

    def __str__(self):
        return str(self.customer.username)

    def calc_book_end(self):
        # date = datetime.datetime.strptime(self.book_start, "%Y-%m-%d")
        self.book_end  = self.book_start + pd.DateOffset(months=self.offer.count)
        # self.book_end = self.book_start + relativedelta(months=self.count)
        return self.book_end

    def calc_is_active(self):
        print(datetime.datetime.today().date())
        c= datetime.datetime.strftime(self.book_end, '%Y/%m/%d ')
        n = datetime.datetime.strftime(datetime.datetime.now(),'%Y/%m/%d ')
        date = datetime.datetime.strptime(c, "%Y/%m/%d ")
        data_now = datetime.datetime.strptime(n, "%Y/%m/%d ")
        if date == data_now :
            days = date - data_now
            message = 'Today the last day for Booking '
            return False ,message ,  days.days
        elif date > data_now :
            days = date - data_now
            message = ''
            return True ,message , days.days

        else :
            return True 

            



    def calc_total_price(self):
        self.total_price = self.offer.price
        return self.total_price 
