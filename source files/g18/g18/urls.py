"""g18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from fileretrieval import views

#路由配置
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('get_folder_path/',views.get_folder_path,name='get_folder_path'),
    path('seek_keyword/',views.seek_keyword,name='seek_keyword'),
    path('download/',views.download,name='download'),
    path('get_directory/',views.get_directory,name='get_directory'),
    path('get_child/',views.get_child,name='get_child')
]