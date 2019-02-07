from django.urls import path
from . import views

app_name = 'requestbox'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('req/', views.AddView.as_view(), name='req'),
    path('mypage/', views.Mypage.as_view(), name='mypage')

]
