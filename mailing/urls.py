from django.urls import path
from mailing import views

urlpatterns = [
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('mailing/', views.MailingList.as_view()),
    path('mailing/<int:pk>/', views.MailingDetail.as_view()),
    path('message/', views.MessageList.as_view())
]

