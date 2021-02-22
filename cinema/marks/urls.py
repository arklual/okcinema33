from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
 
urlpatterns = [
    path('<int:id>/ball/', views.ball, name='ball'),
    path('inf/', views.info, name="info"),
    path('<int:id>/recension/', views.recension, name='recension')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)