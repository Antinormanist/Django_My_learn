from django.urls import path
import goods.views as views


app_name = "goods"

urlpatterns = [
    path("<slug:category_slug>/", views.index, name="index"),
    path("<slug:category_slug>/<int:page>/", views.index, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]