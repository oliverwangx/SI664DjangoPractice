from django.db import models
from django.core.validators import MinLengthValidator

class Type(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Type must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Boat(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    length = models.PositiveIntegerField()
    knots = models.PositiveIntegerField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname