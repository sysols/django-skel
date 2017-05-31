# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from core.views import MainView


urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
]
