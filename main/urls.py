from django.urls import path

import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path(
        "create-shop/",
        main.CarShopCreateView.as_view(),
        name="create-shop",
    ),
    path(
        "delete-shop/<pk>/",
        main.CarShopDeleteView.as_view(),
        name="delete-shop",
    ),
    path("edit-shop/<pk>/", main.edit_shop, name="edit-shop"),
    path(
        "shop-details/<pk>/",
        main.CarShopDetailsView.as_view(),
        name="shop-details",
    ),
    path("add-car/<pk>/", main.add_car, name="add-car"),
    path("add-brand/<pk>/", main.add_brand, name="add-brand"),
    path("get-prop-form/", main.get_prop_form, name="get-prop-form"),
]
