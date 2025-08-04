from django.db import models

class Day(models.Model):
    """Day specified by a user - it can be day of a week or an exact date"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a representation of a model as a text string"""
        return self.text

class Meal(models.Model):
    """Specific information about a progress in learning"""
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Defines the special attribute that tells Django to use 'meals' form instead of 'Entrys' """
        verbose_name_plural = 'meals'

    def __str__(self):
        """Returns a representation of a model as a text string - up to 50 characters"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return f"{self.text}"
