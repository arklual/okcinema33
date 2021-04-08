from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import MyRegisterFormView


urlpatterns = [
    path('signup/', MyRegisterFormView.as_view(), name='signup'),
    path('profile/<int:id>/', views.get_profile, name="profile"),
    path('profile/<int:id>/settings/', views.profile_settings, name="profile_settings"),
    path('profile/<int:id>/upload/image/', views.upload_ava, name="upload_ava"),
    path('profile/<int:id>/change/email/', views.change_email, name="change_email"),
    path('profile/<int:id>/change/name/', views.change_name, name="change_name"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
