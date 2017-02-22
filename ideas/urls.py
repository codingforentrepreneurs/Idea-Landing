"""ideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from newsletter.api.views import JoinCreateAPIView
from pages.views import HomeView, PageDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)$', PageDetailView.as_view(), name='page-detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/email/join/$', JoinCreateAPIView.as_view(), name='email-join'),

]
