from django.forms import SlugField
from django.shortcuts import redirect, render
from .models import Stocks
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm


class StockView(ListView):
    
    model = Stocks
    queryset = Stocks.objects.filter(draft=False)
    template_name = 'stocks/stocks.html'

class StockDetailView(View):

    def get(self, request, slug):
        stock = Stocks.objects.get(tiker=slug)
        return render(request, 'stocks/stocks_detail.html', {'stock': stock})


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        stock = Stocks.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.stock = stock
            form.save()
        return redirect(stock.get_absolute_url())