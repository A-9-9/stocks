from django.db import models

# Create your models here.
class Company(models.Model):
    comp_name = models.CharField(max_length=200)

    def __str__(self):
        return self.comp_name

class Weight(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    weight = models.CharField(max_length=200)

    def __str__(self):
        return '%s: %s' % (self.company.comp_name, self.weight)