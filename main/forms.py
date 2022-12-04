from django import forms

from main.models import Car, CarBrand, CarProp, Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ("ordering",)


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = "__all__"


class CarPropForm(forms.ModelForm):
    class Meta:
        model = CarProp
        exclude = ("car",)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = "__all__"
        exclude = (
            "ordering",
            "seller",
        )
