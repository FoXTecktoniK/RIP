"""lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from my_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^function_view/', function_view),
    url(r'^class_based_view/', ExampleClassBased.as_view()),
    url(r'^static_view/', ExampleStaticView.as_view()),
    url(r'^var_view/', var_view),
    url(r'^tag', var_tag),
    url(r'^orders/', OrdersView.as_view()),
    url(r'^order/(?P<id>\d+)', OrderView.as_view(), name='order_url'),
]
