from django.urls import path
from . import views


urlpatterns = [
    #path("student_info_home/",)
    path("student_add/", views.student_add_view, name='student_add'),
    path("student_search/", views.student_add_view, name='student_search'),
]