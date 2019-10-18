from django.contrib import admin
from django.urls import path,include
from drugs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index,name="index"),
    # path('search/',views.search, name='search'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
