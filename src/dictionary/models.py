from django.db import models

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
            return self.english