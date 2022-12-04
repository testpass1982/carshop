from django import forms

from main.models import Car, CarBrand, CarProp, Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ("ordering",)


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        exclude = (
            "ordering",
            "seller",
        )


class CarPropForm(forms.ModelForm):
    class Meta:
        model = CarProp
        exclude = ("car",)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = (
            "ordering",
            "seller",
        )
