from django.db import models


class FormTemplate(models.Model):
    name = models.CharField(max_length=100)
    fields = models.JSONField()

    def __str__(self):
        return self.name
