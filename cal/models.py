from django.db import models
from django.urls import reverse

class Reader(models.Model):
    name = models.CharField('Имя', max_length=100, )
    surname = models.CharField('Фамилия', max_length=200, )
    email = models.EmailField(max_length=100, null=True, unique= True )
    phone = models.CharField('Телефон', max_length=50, blank=True, unique=True)
    start_time = models.DateTimeField('Дата регистрации', unique= True)


    def __str__(self):
            template ='{0.name} {0.surname} {0.email} {0.phone} '
            return  template.format(self)
    class Meta:
        verbose_name_plural = 'Читатели '

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.start_time } </a>'\
               f'<a href="{url}"> {  self.name,self.surname, self.email,self.phone }\
        </a>'



