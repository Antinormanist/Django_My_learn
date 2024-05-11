from django.urls import path
import goods.views as views


app_name = "goods"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about")
]