from .views import account_detail
from .views import account_view
from django.urls import path

urlpatterns = [
    path('account/<int:account_id>/', account_detail, name='account_detail'),
    path('account/', account_view, name='account_view'),
]