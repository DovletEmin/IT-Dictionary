from django.contrib import admin

from .models import Term, ExcelImport 

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ("english", "abbreviation", "category", "russian", "turkmen")
    search_fields = ("english", "russian", "turkmen", "category")
    list_filter = ("category",)
    ordering = ("english",)


@admin.register(ExcelImport)
class ExcelImportAdmin(admin.ModelAdmin):
    list_display = ("id", "file")