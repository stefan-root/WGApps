from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('create_transaction', views.create_transaction, name='create_transaction'),
    path('confirm', views.confirm, name='confirm'),
    path('view_transactions', views.view_transactions, name='view_transactions'),
    path('', views.view_transactions, name='view_transactions'),
    path('view_transaction/<int:transaction_id>', views.view_transaction, name='view_transaction')
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]