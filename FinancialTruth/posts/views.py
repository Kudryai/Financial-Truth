
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
# одна строка вместо тысячи слов на SQL
    latest = Post.objects.order_by('-pub_date')
    # собираем тексты постов в один, разделяя новой строкой
    output = []
    for item in latest:
        output.append(item.text)
    return render(request, 'index.html', {'posts': latest})
