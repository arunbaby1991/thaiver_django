from django.db import models


class AccountModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.title