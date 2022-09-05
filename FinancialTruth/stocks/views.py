from django.shortcuts import render
from .models import Stocks
from django.views.generic.base import View

class StockView(View):
    
    def get(self, request):
        stocks = Stocks.objects.all()
        return render(request, 'stocks/stocks_list.html', {'stocks_list': stocks})
