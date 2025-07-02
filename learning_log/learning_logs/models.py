from django.db import models

class Topic(models.Model):
    """Topic learned by a user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a representation of a model as a text string"""
        return self.text

