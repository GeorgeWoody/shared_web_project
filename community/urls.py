from django.urls import path
from . import views



urlpatterns = [
    path("community_home/", views.community_home_view, name='community_home'),
    path("student_search/", views.student_search_view, name='student_search'),
    #path("student_search_result/", views.student_search_result_view, name='student_search_result'),
    
    
    path("student_add/", views.student_add_view, name='student_add'),
    
]