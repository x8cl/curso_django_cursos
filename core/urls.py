from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("courses/create_course", views.create_course, name="create_course"),
    path("courses/destroy/<course_id>", views.destroy_course, name="destroy_course"),
    path("courses/delete/<course_id>", views.delete_course, name="delete_course"),
]
