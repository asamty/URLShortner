from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('<str:short_url>', views.redirect_url_view, name='redirect'),
    path('counter/<str:short_url>', views.counter_view, name='counter'),
]