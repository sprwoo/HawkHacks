from django.db import models

# Stores information about a picture
# Name and description
class Picture(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # String representation
    def __str__(self):
        return self.name + " " + self.description