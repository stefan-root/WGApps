from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('confirm', views.confirm, name='confirm')
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]