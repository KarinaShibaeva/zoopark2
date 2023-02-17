from django.urls import path

from animals.views import animal_list_view, animal_id_view

app_name="animals"
urlpatterns=[
    path("",animal_list_view, name = "a"),
    path("animal/<int:pk>", animal_id_view, name="animal")
]

