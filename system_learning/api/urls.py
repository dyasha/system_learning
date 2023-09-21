from django.urls import include, path

from .views import product_lessons, product_stats, user_lessons

urlpatterns = [
    path("user_lessons/", user_lessons, name="user_lessons"),
    path(
        "product_lessons/<int:product_id>/",
        product_lessons,
        name="product_lessons",
    ),
    path("product_stats/", product_stats, name="product_stats"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
