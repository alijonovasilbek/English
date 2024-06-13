from django.db import models


class  Ustoz(models.Model):
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=222)
    picture = models.ImageField(upload_to='ustoz_images/')
    birth_date=models.DateField()
    birth_city=models.CharField(max_length=222)
    likes=models.CharField(max_length=222,blank=True,null=True)
    dislikes=models.CharField(max_length=222,blank=True,null=True)
    currently=models.TextField(null=True,blank=True)
    worries=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table="Ustoz"
        verbose_name="ustoz"