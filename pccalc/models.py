from django.db import models

# Create your models here.


class Graph(models.Model):
    date = models.DateField()
    risk = models.IntegerField()

    def __str__(self):
        return "{}::{}".format(self.date, self.risk)
