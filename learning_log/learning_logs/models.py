from django.db import models

class Topic(models.Model):
    """Topic learned by a user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a representation of a model as a text string"""
        return self.text

class Entry(models.Model):
    """Specific information about a progress in learning"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Defines the special attribute that tells Django to use 'entries' form instead of 'Entrys' """
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns a representation of a model as a text string - up to 50 characters"""
        return f"{self.text[:50]}..."