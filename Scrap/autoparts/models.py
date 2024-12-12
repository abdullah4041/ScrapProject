from django.db import models
from accounts.models import ProfileSeller
from Vehicle.models import Car

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Part(models.Model):
    part_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    alternative_name = models.CharField(max_length=512, blank=True, null=True)
    image = models.ImageField(upload_to="parts_images/", default="parts_images/default.svg")

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class PartDirection(models.TextChoices):
        RIGHT = "Right", "يمين"
        LEFT = "Left", "يساد"

    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    car = models.ManyToManyField(Car, related_name="products")
    seller = models.ForeignKey(ProfileSeller, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=256, blank=True, null=True)
    part_direction = models.CharField(max_length=64, choices=PartDirection.choices, blank=True, null=True)
    made = models.CharField(max_length=64, blank=True, null=True)
    stock = models.SmallIntegerField()
    condition = models.CharField(max_length=255)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="products_images/", default="products_images/", blank=True)

    def __str__(self) -> str:
        return self.name


    # class PartCategory(models.TextChoices):
    #     ENGINES = "Engine & Transmission", "المكينة والقير"
    #     ELECTRICALS = "Electircal",  "قطع كهربائية"
    #     EXTERIORS = "Exterior & Body", "البودي"
    #     LIGHTS = "lights", "الأنوار"
    #     COOLIINGS = "Cooling & Heating", "التبريد والتكييف"
    #     INTERIOIR = "Interior & Accessories", "الداخلية والاكسسوارت"
    #     SUSPENSIONS = "Suspensions", "الميزانية / نظام التعليق"
    #     MECHANICALS = "Mechanical", "قطع ميكانيكية"
    #     UNCATEGORIZED = "Uncategorized", "قطع غير مصنفة"


    # Engine = Part.objects.all().filter(part_category=Part.PartCategory.ENGINES)
    # electricals = Part.objects.all().filter(part_category=Part.PartCategory.ELECTRICALS)
    # exteriors = Part.objects.all().filter(part_category=Part.PartCategory.EXTERIORS)
    # lights = Part.objects.all().filter(part_category=Part.PartCategory.LIGHTS)
    # coolings = Part.objects.all().filter(part_category=Part.PartCategory.COOLIINGS)
    # suspensions = Part.objects.all().filter(part_category=Part.PartCategory.SUSPENSIONS)
    # mechanicals = Part.objects.all().filter(part_category=Part.PartCategory.MECHANICALS)
    # uncategorized = Part.objects.all().filter(part_category=Part.PartCategory.UNCATEGORIZED)