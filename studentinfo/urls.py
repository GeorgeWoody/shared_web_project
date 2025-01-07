from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    ### MAIN STUDENT INFO URL ###
    path("student_home/", views.student_home, name="student_home"),
    #############################
    ### FUNCTIONALITY URL'S #####
    path("student_search/", views.student_search, name="student_search"),
    # path("add_student/", views.add_student, name="add_student"),
    # path("success/", TemplateView.as_view(template_name="success"), name="success"),
    # path("student_list/", views.student_list, name="student_list" )
]