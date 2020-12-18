from django.db import models

# Create your models here.
class ConVModels(models.Model):
    mid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    nowConfirm=models.IntegerField(null=False)
    confirm=models.IntegerField(null=False)
    suspect=models.IntegerField(null=False)
    dead=models.IntegerField(null=False)
    heal=models.IntegerField(null=False)