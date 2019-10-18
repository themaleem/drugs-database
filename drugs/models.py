from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Drug(models.Model):
    name = models.CharField(max_length=256)
    active_ingredient = models.CharField(max_length=256)
    applicant_name = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    manufacturer = models.CharField(max_length=256)
    date_approv = models.DateTimeField(auto_now=False)
    exp_date = models.DateTimeField(auto_now=False)
    reg_no = models.CharField(max_length=256)
    slug= models.SlugField()

    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Drug,self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Drugs'
