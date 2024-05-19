from django.db import models

# Stores information about a picture
# Name and description
class Picture(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    group_image = models.ImageField(upload_to='group_images/')

    # String representation
    def __str__(self):
        return self.name + ", " + self.email