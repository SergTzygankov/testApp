from django.urls import path
from . import views

app_name = 'app_for_tests'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.test_create, name='test_create'),  # Обновленный URL-адрес
    path('<int:test_id>/', views.choose_test, name='choose_test'),
    path('/<int:test_id>/start/', views.start_test, name='start_test'),  # Новый URL-шаблон для начала теста
    path('test_result/<int:test_id>/', views.test_result, name='test_result'),
    path('<int:test_id>/questions/<int:question_id>/', views.choose_question, name='choose_question'),
]
