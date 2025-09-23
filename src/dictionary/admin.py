from django.contrib import admin

from .models import Term

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("english", "abbreviation", "category", "russian", "turkmen")
    search_fields = ("english", "russian", "turkmen", "category")
    list_filter = ("category",)