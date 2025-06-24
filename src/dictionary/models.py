from django.db import models

class Term(models.Model):
    id = models.AutoField(primary_key=True)
    english = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    russian = models.CharField(max_length=255)
    turkmen = models.CharField(max_length=255)

    description_en = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_tm = models.TextField(blank=True)

    def __str__(self):
        return self.english
    
    class Meta:
        ordering = ['id']