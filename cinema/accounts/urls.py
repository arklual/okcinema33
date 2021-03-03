from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import MyRegisterFormView

urlpatterns = [
    path('signup/', MyRegisterFormView.as_view(), name='signup'),
    path('profile/<str:username>', views.get_profile, name="profile"),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)