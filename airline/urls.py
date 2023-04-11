"""airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.contrib.auth.views import UserModel

urlpatterns = [
    # path('admin/',admin.site.urls),
    path('adminl/',views.adminl,name='adminl'),
    path('',views.home,name='home'),
    path('sign/', views.Insertrecord,name='sign'),
    path('addf/',views.addf,name='addf'),
    path('feedbv/',views.feedbv,name='feedbv'),
    path('lists/',views.lists,name='lists'),
    path('book/',views.book,name='book'),
    path('users/',views.users,name='user'),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>',views.delete),
    path('deleted/<int:id>',views.deleted),
    path('delet/<int:id>',views.delet),
    path('deleteb/<int:id>',views.deleteb),
    path('search/',views.search,name='search'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profi/<int:id>/',views.profi,name='profi'),
    path('upda/<int:id>/',views.upda),
    path('feedb/',views.feedb,name='feedb'),
    path('books/<int:id>',views.books,name='book'),
    path('bookv/',views.bookv,name='bookv'),
    path('rand/',views.rand,name='rand'),
    path('rando/',views.rando,name='rando'),
    # path('new/<int:id>/',views.new,name='new'),
    path('bdet/<int:id>',views.bdet,name='bdet'),
]
