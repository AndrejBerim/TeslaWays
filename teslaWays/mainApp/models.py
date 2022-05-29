from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=20, blank=True, unique=True)
    password = models.CharField(max_length=64, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Country(models.Model):
    country_name = models.CharField(
        max_length=50, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return str(self.country_name)


class Region(models.Model):
    region_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    region_country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=50,  null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    city_region = models.ForeignKey(
        Region, on_delete=models.CASCADE, null=True, blank=True)
    city_country = models.ForeignKey(
        Country, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city_name


class News(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField(null=True, blank=True)
    news_image = models.ImageField(
        upload_to='staticfiles/img', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    news_region = models.ForeignKey(
        Region, on_delete=models.CASCADE, blank=True, null=True)
    news_city = models.ForeignKey(
        City, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image_one = models.ImageField(
        upload_to='uploads/', blank=True, null=True, verbose_name="image 1", help_text="text")
    image_two = models.ImageField(
        upload_to='uploads/', blank=True, null=True, verbose_name="image 2", help_text="text")
    image_three = models.ImageField(
        upload_to='uploads/', blank=True, null=True, verbose_name="image 3", help_text="text")

    class Meta:
        verbose_name = "About Us"

    def __str__(self):
        return self.title
