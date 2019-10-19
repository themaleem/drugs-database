from django.urls import path
from drugs import views

app_name='drugs'


urlpatterns = [
    path('all/',views.drug_list,name="all_drugs"),
    path('detail/<str:drug_slug>',views.drug_detail,name="details"),
]