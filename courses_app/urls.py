from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index),
    path ('addcourse', views.add_course),
    path ('delete/<int:id>', views.verify),
    path ('verify/<int:id>', views.delete)
]
