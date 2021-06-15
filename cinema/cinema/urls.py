"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('films/', include(('films.urls', 'films'), namespace='film')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace="account")), 
    path('play/', include(('player.urls', 'player'), namespace='player')),
    path('marks/', include(('marks.urls', 'marks'), namespace='mark')),
    path('serial/', include(('serials.urls', 'serials'), namespace='serial')),
    path('list/', include(('movieList.urls', 'movieList'), namespace='list')),
    path('search/', include(('search.urls', 'search'), namespace='search')),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path('aboutus/', include(('about_us.urls', 'about_us'), namespace="about_us")), 
    path('manual/', include(('manual.urls', 'manual'), namespace="manual")), 
]
