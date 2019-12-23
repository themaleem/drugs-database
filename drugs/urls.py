from django.urls import path
from drugs import views
# from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register('api/drugs',views.DrugsViewSet,base_name='api')
app_name='drugs'


urlpatterns = [
    path('all/',views.drug_list,name="all_drugs"),
    path('detail/<str:drug_slug>',views.drug_detail,name="details"),
    path('api',views.DrugsList.as_view(),name='api-drugs-list'),
]
# urlpatterns+=router.urls