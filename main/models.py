from django.db import models

# Create your models here.


class OrderableMixin(models.Model):
    """
    Orderable Mixin
    """

    ordering = models.SmallIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["ordering"]


class JsonMixin(models.Model):
    """
    Json Mixin
    """

    json = models.JSONField(
        default=dict,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Company(OrderableMixin):
    """
    Company Model class
    """

    title = models.CharField(max_length=100)
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "CarShop"

    def __str__(self):
        return self.title

    def get_cars(self):
        if self.cars.select_related().exists():
            return self.cars.select_related()
        return []


class CarBrand(OrderableMixin):
    """
    CarBrand Model class
    """

    title = models.CharField(max_length=255)
    seller = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="brands",
    )

    class Meta:
        verbose_name = "Brand"

    def __str__(self):
        return self.title


class Car(OrderableMixin):
    """
    Car Model class
    """

    title = models.CharField(max_length=255)
    seller = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
        related_name="brand_cars",
    )

    def __str__(self):
        return self.title

    def get_props(self):
        if self.props.select_related().exists():
            return self.props.select_related()
        return []


class CarProp(OrderableMixin):
    PROP_SELECT = (
        ("body", "body"),
        ("engine", "engine"),
        ("transmission", "transmission"),
        ("interior", "interior"),
    )
    car = models.ForeignKey(
        Car,
        related_name="props",
        on_delete=models.CASCADE,
    )
    option = models.CharField(max_length=20, choices=PROP_SELECT)
    value = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return f"{self.option}: {self.value}"
