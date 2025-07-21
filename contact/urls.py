from django.urls import path
from . import views

urlpatterns = [
    path('', views.footer_contact_view, name='send_message'),
]
