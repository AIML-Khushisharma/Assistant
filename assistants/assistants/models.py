from django.db import models

class Assistant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name
