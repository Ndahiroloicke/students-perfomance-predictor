from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.classify_and_predict, name='predict_performance'),
    path('form/', views.performance_form, name='performance_form'),
    path('test/', views.performance_form, name='test_form'),
]
