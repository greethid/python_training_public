from django.db import models

class Pizza(models.Model):
    """Name of pizza"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Returns a representation of a model as a text string"""
        return self.name

class Topping(models.Model):
    """Specific information about a progress in learning"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    # class Meta:
    #     """Defines the special attribute that tells Django to use 'entries' form instead of 'Entrys' """
    #     verbose_name_plural = 'entries'

    def __str__(self):
        """Returns a representation of a model as a text string - up to 50 characters"""
        if len(self.name) > 50:
            return f"{self.name[:50]}..."
        return f"{self.name}"
