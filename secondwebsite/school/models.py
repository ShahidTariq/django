from django.db import models


class Classes(models.Model):
    class_name = models.CharField(max_length=100)
    class_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.class_name


class Subjects(models.Model):
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    max_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.subject_name


class Fees(models.Model):
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    fee_amount = models.IntegerField(default=0)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return self.fee_amount
