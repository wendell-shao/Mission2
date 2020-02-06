"""yslfunds URL Configuration

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
import sys
sys.path.append("..")
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from basic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('article/', include('article.urls')),
    ### include simditor urls
    path('simditor/', include('simditor.urls')),
    path('', views.page, name='home'),
    # path('<slug:slug>/', views.page, name='page'),
    path('<slug:slug>/<slug:sub_slug>/', views.page, name='page'),
]
# add static url for upload images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)