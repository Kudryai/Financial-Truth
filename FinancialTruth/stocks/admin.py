from django.contrib import admin
from .models import Stocks,RatingStar,Category,Rating,Reviews
# Register your models here.

admin.site.register(Category)
admin.site.register(Stocks)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)