
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from account.models import Account
from django.shortcuts import reverse 


def img_location(instance, filename, **kwargs ):
	file_path = 'movie/{title}-{filename}'.format(
		    title=str(instance.title), filename=filename)
	return file_path


class MoviesRent(models.Model):
    title = models.CharField(max_length=60,null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    image = models.ImageField(upload_to=img_location,null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True,verbose_name='date published')
    likes = models.IntegerField(default=0)
    stock = models.IntegerField(default=1)
    rentail_price = models.FloatField(null=False)
    sale_price = models.FloatField(null=False)
    avility = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title
    
    def get_add_sale_history(self):
        return reverse('movie:add-sale', kwargs={
               'slug':self.slug
        })


class UpdateLog(models.Model):
    title = models.CharField(max_length=60,null=False, blank=False)
    old_rentail_price = models.FloatField(null=False)
    old_sale_price = models.FloatField(null=False)
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='date updated')

    def __str__(self):
        return self.title    



@receiver(post_delete, sender=MoviesRent)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_movie_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.owner.username + "-" + instance.title)

pre_save.connect(pre_save_movie_post, sender=MoviesRent)


class UserSaleHistory(models.Model):
    
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_sale = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(MoviesRent, on_delete=models.CASCADE)
    movie_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.account.username



