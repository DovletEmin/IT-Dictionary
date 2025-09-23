from django.db import models
import openpyxl


class Term(models.Model):
    english = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=100, blank=True)
    russian = models.CharField(max_length=255)
    turkmen = models.CharField(max_length=255)
    description_en = models.TextField()
    description_ru = models.TextField()
    description_tm = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["english"]
        verbose_name = "Term"
        verbose_name_plural = "Terms"

        def __str__(self):
            return self.id, self.english
        

class ExcelImport(models.Model):
    file = models.FileField(upload_to="imports/")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        wb = openpyxl.load_workbook(self.file.path)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            english, abbreviation, category, russian, turkmen, description_en, description_ru, description_tm = row

            Term.objects.update_or_create(
                english=english,
                defaults = {
                    "abbreviation": abbreviation,
                    "category": category,
                    "russian": russian,
                    "turkmen": turkmen,
                    "description_en": description_en,
                    "description_ru": description_ru,
                    "description_tm": description_tm,
                },
            )