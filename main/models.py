from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,

    )

    class MPTTMeta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return f'{self.name} | parent - {self.parent}' if self.parent else self.name

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name="No category")
        return obj.pk


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=Category.get_default_pk,

    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return f'{self.name} price - ({self.price} quantity - {self.quantity} description - {self.description})'


