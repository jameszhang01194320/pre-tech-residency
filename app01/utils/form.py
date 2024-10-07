from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm


class UserModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label="username",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", 'account', 'create_time', "gender", "depart"]


class PrettyModelForm(BootStrapModelForm):
    #1
    mobile = forms.CharField(
        label="mobile",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', 'wrong'), ],
    )

    class Meta:
        model = models.PrettyNum
        # fields = "__all__"
        # exclude = ['level']
        fields = ["mobile", 'price', 'level', 'status']

    # 2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("already exist")

        # 
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label="mobile")
    mobile = forms.CharField(
        label="mobile",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', 'mobile wrong'), ],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    # 2
    def clean_mobile(self):
        # 
        # print(self.instance.pk)
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("mobile exists")

        # 
        return txt_mobile
