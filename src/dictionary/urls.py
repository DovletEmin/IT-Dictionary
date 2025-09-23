from django.urls import path

from . import views

urlpatterns = [
    path("terms/", views.TermsEnglishListView.as_view(), name="terms-list"),
    path("terms/<int:pk>/", views.TermDetailView.as_view(), name="term-detail"),
    path("terms/names/", views.TermNameByLangView.as_view(), name="term-names-by-lang"),
    path("categories/", views.CategoriesView.as_view(), name="categories"),
    path("terms/count/", views.TermsCountView.as_view(), name="terms-count"),
]