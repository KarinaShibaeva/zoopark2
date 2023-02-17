from django.db import models

class Animal(models.Model):
    kind=models.CharField(max_length=128, verbose_name = 'Вид животного')
    description=models.TextField(blank=False, verbose_name = 'Описание животного')
    birthday = models.DateField(verbose_name = 'День рождения животного')
    image=models.ImageField(upload_to="%Y/%m/%d/", verbose_name = 'Фотография животного')
    
    def __str__(self):
        return self.kind
    
    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"
