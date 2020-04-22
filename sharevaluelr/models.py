from django.db import models

# Create your models here.


class sharevaluecalculate(models.Model):
    Openingvalue=models.FloatField()
    High=models.FloatField()
    Low=models.FloatField()





    def __str__(self):
        return '{} {} {}'.format(self.Openingvalue,self.High,self.Low)







