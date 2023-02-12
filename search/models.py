from django.db import models
from uuid import uuid4
# Create your models here.
class Goods(models.Model):
    id = models.UUIDField(default=uuid4, unique= True, editable=False, primary_key=True)
    amount = models.IntegerField(default = 0, null = True, blank = True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} ({self.amount} pc(s))"