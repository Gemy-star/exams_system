from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_exam, name='create-exam'),
    path('question/create', views.create_question, name='create-question'),
    path('cat/<int:pk>', views.cat_exam_list, name='exam-cat-list'),
    path('<int:pk>', views.exam_detail, name='exam-detail'),
    path('cat/question', views.get_ques_cat, name='cat-ques'),
    path('result/list', views.result_list, name='result-list')

]
