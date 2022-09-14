from django.shortcuts import render
from .models import Stocks
from django.views.generic.base import View

class StockView(View):
    
    def get(self, request):
        stocks = Stocks.objects.all()
        return render(request, 'stocks/stocks.html', {'stocks_list': stocks})

class StockDetailView(View):

    def get(self, request, slug):
        stock = Stocks.objects.get(tiker=slug)
        return render(request, 'stocks/stocks_detail.html', {'stock': stock})