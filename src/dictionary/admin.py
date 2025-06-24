from import_export.admin import ImportExportModelAdmin
from .models import Term
from django.contrib import admin
from .resources import TermResource

@admin.register(Term)
class TermAdmin(ImportExportModelAdmin):
    resource_class = TermResource
    list_display = ('id', 'english', 'abbreviation', 'category')
    search_fields = ('english', 'russian', 'turkmen', 'abbreviation')
