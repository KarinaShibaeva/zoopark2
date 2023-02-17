from django.urls import path

from siteinfo.views import home_view, info_view

app_name = "siteinfo"
urlpatterns = [
    path('home/', home_view, name = "home"),
    path('info/', info_view, name = "info"),
]

