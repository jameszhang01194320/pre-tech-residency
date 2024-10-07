from django.db import models


class Department(models.Model):

    title = models.CharField(verbose_name='title', max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):

    name = models.CharField(verbose_name="name", max_length=16)
    password = models.CharField(verbose_name="password", max_length=64)
    age = models.IntegerField(verbose_name="age")
    account = models.DecimalField(verbose_name="balance", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="Starting time")
    create_time = models.DateField(verbose_name="Starting time")


    depart = models.ForeignKey(verbose_name="depart", to="Department", to_field="id", on_delete=models.CASCADE)
    # ### 3.2 置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # in django
    gender_choices = (
        (1, "male"),
        (2, "female"),
    )
    gender = models.SmallIntegerField(verbose_name="gender", choices=gender_choices)


class PrettyNum(models.Model):

    mobile = models.CharField(verbose_name="mobile", max_length=11)

    price = models.IntegerField(verbose_name="price", default=0)

    level_choices = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
    )
    level = models.SmallIntegerField(verbose_name="rank", choices=level_choices, default=1)

    status_choices = (
        (1, "used"),
        (2, "unuse")
    )
    status = models.SmallIntegerField(verbose_name="status", choices=status_choices, default=2)
