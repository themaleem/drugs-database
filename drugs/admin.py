from django.contrib import admin
from drugs.models import Drug
# Register your models here.
class DrugAdmin(admin.ModelAdmin):
    list_display=('name','reg_no','date_approv')

admin.site.register(Drug,DrugAdmin)