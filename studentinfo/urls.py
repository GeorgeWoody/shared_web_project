from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path("add_student/", views.add_student, name="add_student"),
    path("success/", TemplateView.as_view(template_name="success"), name="success") 
]