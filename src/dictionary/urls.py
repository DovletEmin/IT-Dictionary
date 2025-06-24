from django.urls import path
from .api import get_terms, all_terms_view, AllTermsView, TermDetailView

urlpatterns = [
    path('terms/all/', all_terms_view, name='all_terms'),
    path('terms/<int:id>/', TermDetailView.as_view(), name='term_detail'),
    path('terms/<str:lang>/', get_terms, name='get_terms'),
]