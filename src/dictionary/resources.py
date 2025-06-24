from import_export import resources
from .models import Term

class TermResource(resources.ModelResource):
    class Meta:
        model = Term
