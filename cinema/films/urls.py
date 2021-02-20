from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.single, name='single'),
    path('serial/<int:id>/', views.serial, name='serial'),
    path('play/<int:id>/<int:season>/<int:number>', views.full_player, name='full_player'),
    path('<int:id>/ball/', views.ball, name='ball'),
    path('inf/', views.info, name="info"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)