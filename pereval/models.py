from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    fam = models.TextField(max_length=15, null=True, verbose_name='Фамилия')
    name = models.TextField(max_length=15, null=True, verbose_name='Имя')
    otc = models.TextField(max_length=15, null=True, verbose_name='Отчество')
    emails = models.EmailField(max_length=30, unique=True, verbose_name='Почта пользователя')
    phone = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Номер телефона')

    def __str__(self):
        return f'{self.fam}: {self.name}: {self.otc}'


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')



class Pereval_areas(models.Model):
    id_parent = models.TextField(max_length=4, default=0)
    title_area = models.TextField(max_length=255, verbose_name='Горный хребет')

    def __str__(self):
        return f'{self.title_area}'


class Pereval_added(models.Model):
    beautyTitle = models.TextField(max_length=25, verbose_name='Красивое название', blank=True)
    title_added = models.TextField(max_length=25, verbose_name='Название', blank=False)
    other_titles = models.TextField(max_length=25, verbose_name='Другие комментарии', blank=True)
    connect = models.TextField(max_length=25, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    coord_id = models.ForeignKey(Coords, on_delete=models.CASCADE, null=True)

    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    LEVELS = [
        ('1А', '1А'),
        ('1Б', '1Б'),
        ('2А', '2А'),
        ('2Б', '2Б'),
        ('3А', '3А'),
        ('3Б', '3Б'),
    ]

    winter = models.TextField(max_length=5, choices=LEVELS, blank=True)
    summer = models.TextField(max_length=5, choices=LEVELS, blank=True)
    autumn = models.TextField(max_length=5, choices=LEVELS, blank=True)
    spring = models.TextField(max_length=5, choices=LEVELS, blank=True)

    STATUSES = [
        ('new', 'Новый'),
        ('pending', 'В работе'),
        ('accepted', 'информация принята'),
        ('rejected', 'информация не принята'),
    ]

    status = models.CharField(max_length=25, choices=STATUSES, default='new', verbose_name="Статус", )

    def __str__(self):
        return f'{self.beautyTitle}: {self.title_added}: {self.other_titles}'


class Spr_activities_types(models.Model):
    title_types = models.TextField(max_length=25, verbose_name='Тип')

    def __str__(self):
        return f'{self.title_types}'


class Pereval_images(models.Model):
    img = models.FileField(upload_to='files/', blank=True, verbose_name="Фото")
    id_perevala = models.ForeignKey(Pereval_added, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_perevala}'




