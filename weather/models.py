from django.db import models


# Create your models here.
class City(models.Model):
    """Model definition for City."""

    name = models.CharField(max_length=25)

    class Meta:
        """Meta definition for City."""

        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
