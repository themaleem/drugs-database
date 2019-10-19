from django.urls import path
from drugs import views
app_name='drugs'


urlpatterns = [
    path('all/',views.drug_list,name="all_drugs"),
]

