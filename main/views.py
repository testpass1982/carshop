from django.db.models.query_utils import check_rel_lookup_compatibility
from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from nested_formset import nestedformset_factory

from main.forms import CarForm, CarPropForm, CompanyForm
from main.models import Car, CarBrand, CarProp, Company

# Create your views here.


def index(request):
    title = "Welcome to our CarShops management system!"
    car_shops = Company.objects.all()
    context = {
        "title": title,
        "car_shops": car_shops,
    }
    return render(request, "main/index.html", context)


class CarShopCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "main/add_shop.html"

    def get_success_url(self):
        return reverse("main:shop-details", kwargs={"pk": self.object.pk})


def add_car(request, pk):
    form = CarForm()
    shop = Company.objects.get(pk=pk)
    if request.method == "POST":
        props_options = request.POST.getlist("option")
        props_values = request.POST.getlist("value")
        props_forms = [
            CarPropForm({"option": el[0], "value": el[1], "ordering": count})
            for count, el in enumerate(zip(props_options, props_values))
        ]
        form = CarForm(request.POST)
        if form.is_valid():
            car_instance = form.save(commit=False)
            car_instance.seller = shop
            car_instance.save()
            if props_forms and all(f.is_valid() for f in props_forms):
                for f in props_forms:
                    prop_inst = f.save(commit=False)
                    prop_inst.car = car_instance
                    prop_inst.save()
            else:
                print("errors", [f.errors for f in props_forms])
            return redirect("main:shop-details", shop.pk)
    context = {
        "form": form,
        "shop": shop,
    }
    return render(request, "main/add_car.html", context)


def get_prop_form(request):
    context = {"prop_form": CarPropForm}
    return render(request, "main/prop-form.html", context)


def edit_shop(request, pk):
    shop = Company.objects.get(pk=pk)
    form = CompanyForm(instance=shop)
    CarsFormset = nestedformset_factory(
        Company,
        Car,
        nested_formset=inlineformset_factory(
            Car,
            CarProp,
            exclude=("ordering",),
            extra=0,
        ),
        extra=0,
    )
    formset = CarsFormset(instance=shop)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=shop)
        formset = CarsFormset(request.POST, instance=shop)
        if formset.is_valid() and form.is_valid():
            formset.save()
            form.save()
            return redirect("main:shop-details", shop.pk)
    context = {
        "shop": shop,
        "form": form,
        "formset": formset,
    }
    return render(request, "main/edit_shop.html", context)


class CarShopDetailsView(DetailView):
    model = Company

    def get_template_names(self):
        return ["main/shop-details.html"]


class CarShopDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy("main:index")
    template_name = "main/confirm_delete.html"
