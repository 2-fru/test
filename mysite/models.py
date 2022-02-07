from django.db import models

class Test(models.Model):
    test1 = models.IntegerField(blank=True, null=True)
    test2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'