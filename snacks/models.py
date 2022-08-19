from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    title = models.CharField(max_length=64)
    #Name of the snack - could be text or char field
    description = models.TextField(default = "")
    # TextFields need an initial default value
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # This is going to be a primary key for this database. Remember, primary key for one database is the foreign key from another db.
    # Deleting from the frontend deletes from the database

    def __str__(self):
        return self.title
    #This gives us some description in the admin portal

    def get_absolute_url(self):
        return reverse('detail_snack', args=[str(self.id)])