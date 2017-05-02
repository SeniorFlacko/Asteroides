"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.views.generic.dates import ArchiveIndexView,DateDetailView
from newapp.views import (AsteroideYearArchiveView,
                          AsteroideMonthArchiveView,
                          AsteroideWeekArchiveView,
                          AsteroideDayArchiveView,
                          AsteroideTodayArchiveView,
                          AsteroideDetailView,
                          )
from newapp.models import Asteroide
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^(?P<slug>[-\w]+)/$', AsteroideDetailView.as_view(), name='asteroide-detail'),
    url(r'^$',AsteroideTodayArchiveView.as_view(),name="index"),
    url(r'^archive/$',ArchiveIndexView.as_view(model=Asteroide, date_field="fecha"),name="asteroide_archive"),
    url(r'^(?P<year>[0-9]{4})/$',AsteroideYearArchiveView.as_view(),name="asteroide_year_archive"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',AsteroideMonthArchiveView.as_view(month_format='%m'),name="archive_month_numeric"),
    url(r'^(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$',AsteroideWeekArchiveView.as_view(),name="archive_week"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',AsteroideDayArchiveView.as_view(month_format='%m'),name="archive_day"),
    url(r'^today/$',AsteroideTodayArchiveView.as_view(),name="archive_today"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<pk>[0-9]+)/$',DateDetailView.as_view(model=Asteroide,month_format='%m', date_field="fecha"),name="archive_date_detail"),
]
