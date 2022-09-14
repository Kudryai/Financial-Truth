from django.db import models
from PIL import Image
from PIL import ImageFilter
from PIL.Image import Resampling
# Create your models here.
class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Stocks(models.Model):
    name = models.CharField('Акция', max_length=100,null=True)
    tiker = models.CharField('Тикер', max_length=10,null=True)
    description = models.TextField('Описание',null=True)
    logo = models.ImageField('Логотип', upload_to='logo/',null=True)
    country = models.CharField('Страна', max_length=100,null=True)
    dividend = models.FloatField('Дивиденды', default =0,null=True)
    price = models.FloatField('Цена',default =0,null=True)
    proffit_52 = models.TextField('Профит за 52 недели', help_text='Указывать в процентах',default =0,null=True)
    weight_to_index = models.FloatField('Вес в индексе', help_text='Указывать в процентах',default =0,null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def save(self):
        super().save()
        img = Image.open(self.logo.path)
        if img.height > 500 or img.width > 500:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.logo.path)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)



    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
    ip = models.CharField('IP', max_length = 15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE, verbose_name = 'Акция')

    def __str__(self):
        return f'{self.star} - {self.stock}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=40)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    stock = models.ForeignKey(Stocks, verbose_name='акция', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.stock}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'