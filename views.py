from unicodedata import category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse,reverse_lazy
from .models import Order
from django.db.models import Q
from datetime import date

# Create your views here.

class OrderListView(LoginRequiredMixin,ListView):
    template_name = 'list.html'
    model = Order

    def get_queryset(self):
        # 1回目はNone
        q_word = self.request.GET.get('query')
        date1 = self.request.GET.get('date1') 
        date2 = self.request.GET.get('date2')
        category = self.request.GET.get('category')

        # print(q_word)

        keywords = {}

        cnt = 0
        if q_word:
            cnt +=1
            keywords["customer__name__icontains"] = q_word
        if date1 and len(date1) > 0:
            cnt +=1
        else:
            date1 = date(1900, 1, 1)

        if date2 and len(date2) > 0:
            cnt += 1
        else:
            date2 = date.today()  

        if category:
            cnt +=1
            keywords["customer__customer_category__category__icontains"] = category

                  

        keywords["date__range"] =[date1, date2]

        
        #print(len(keywords))
        if cnt > 0:
            object_list = Order.objects.filter(**keywords)
        else:
            object_list = Order.objects.all()
        return object_list

class OrderDetailView(LoginRequiredMixin,DetailView):
    template_name = 'detail.html'
    model = Order

class OrderUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'update.html'
    model = Order
    fields = ('customer','prodact','unit_price','quantity','date','memo')
    success_url = reverse_lazy('list')

class OrderCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'create.html'
    model = Order
    fields = ('customer','prodact','unit_price','quantity','date','memo')
    success_url = reverse_lazy('list')
    success_message = "営業データが追加されました。"

class OrderDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'delete.html'
    model = Order
    success_url = reverse_lazy('list')





