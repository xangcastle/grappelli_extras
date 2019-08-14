from django.db import models
from grappelli_extras.models import base


class Country(base):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Region(base):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class City(base):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Customer(base):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=250, null=True)
    phone_number = models.CharField(max_length=25, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        permissions = (
            ("can_report_1", "Report # 1"),
            ("can_report_2", "Report # 2"),
        )

    def get_country(self):
        if self.country:
            country, created = Country.objects.get_or_create(name=self.country)
            self._country = country
            self.save()

    def get_region(self):
        if self.region:
            region, created = Region.objects.get_or_create(country=self.country, name=self.region)
            self._region = region
            self.save()

    def get_city(self):
        if self.city:
            city, created = City.objects.get_or_create(country=self.country, region=self.region,
                                                       name=self.city)
            self._city = city
            self.save()

