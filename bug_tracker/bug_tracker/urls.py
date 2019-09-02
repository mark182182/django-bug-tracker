"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.contrib.auth.views import logout
from . import views

version = 'api/v1'

urlpatterns = [
    path(version + '/employee',
         views.employee, name='employee'),
    path(version + '/employees',
         views.employees, name='employees'),
    path(version + '/submitter',
         views.submitter, name='submitter'),
    path(version + '/bug',
         views.bug, name='bug'),
    path(version + '/bugs',
         views.bugs, name='bugs'),
    path(version + '/bugs-by-submitter',
         views.bugs_by_submitter, name='bugs-by-submitter'),
    path(version + '/discussion',
         views.discussion, name='discussion'),
    path(version + '/discussions',
         views.discussions, name='discussion')
]
