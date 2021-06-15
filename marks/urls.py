from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
 
urlpatterns = [
    path('<int:id>/ball/', views.ball, name='ball'),
    path('inf/', views.info, name="info"),
    path('<int:id>/recension/', views.recension, name='recension'),
    path('<int:id>/recension/list/', views.recension_list, name='recension_list'),
    path('recension/<int:id>/', views.single_recension, name='single_recension'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)