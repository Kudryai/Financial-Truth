from django import forms
from django.contrib import admin
from .models import Stocks,RatingStar,Category,Rating,Reviews
from django.utils.safestring import mark_safe
# Register your models here.

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class StockAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Stocks
        fields = '__all__'




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "url", "name")
    list_display_links = ('name',)

@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ('id', "tiker", "name", 'price', 'category', 'draft', 'get_image')
    list_display_links = ('name',)
    search_fields = ('tiker', 'name')
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    readonly_fields = ('get_image',)
    form = StockAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.logo.url} widht="50" height="50"')
    
    get_image.short_description = 'Изображение'

class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', "parent", "email", 'stock')
    list_display_links = ('name',)
    search_fields = ('name', 'stock')
    inlines = [ReviewInLine]

@admin.register(RatingStar)
class RaitingStartAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(Rating)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.site_title = 'Financial Truth by Aleksey Kudryavtcev'
admin.site.site_header = 'Financial Truth by Aleksey Kudryavtcev'