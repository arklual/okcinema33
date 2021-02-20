from django.urls import path
 
from .views import MyRegisterFormView
 
urlpatterns = [
    path('signup/', MyRegisterFormView.as_view(), name='signup'),
]