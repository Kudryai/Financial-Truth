from django.db import models

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
    name = models.CharField('Акция', max_length=100)
    tiker = models.CharField('Тикер', max_length=10)
    description = description = models.TextField('Описание')
    logo = models.ImageField('Логотип', upload_to='logo/')
    country = models.CharField('Страна', max_length=100)
    dividend = models.PositiveIntegerField('Дивиденды', default =0 )
    price = models.PositiveIntegerField('Цена',default =0)
    proffit_52 = models.IntegerField('Профит за 52 недели', help_text='Указывать в процентах',default =0)
    weight_to_index = models.PositiveIntegerField('Вес в индексе', help_text='Указывать в процентах',default =0)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

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