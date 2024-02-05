from django.urls import path
from . import views

app_name = 'app_for_tests'

urlpatterns = [
    path('', views.index, name='index'),
    path('app_for_tests/<int:test_id>/', views.choose_test, name='choose_test'),
    path('app_for_tests/<int:test_id>/questions/<int:question_id>', views.choose_question, name='choose_question'),
    path('app_for_tests/<int:test_id>/result', views.test_result, name='test_result'),
    path('app_for_tests/create', views.test_create, name='test_create'),

]

