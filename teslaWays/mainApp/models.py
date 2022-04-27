from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Place(models.Model):
    TYPE_CHOICES = (
        ('eat', 'eat'),
        ('sleep', 'sleep'),
        ('attraction', 'attraction')
    )
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, null=True, blank=True)
    website = models.CharField(max_length=40, null=True, blank=True)
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, null=True, blank=True)
    longitude = models.FloatField(default=20.468565, blank=True)
    latitude = models.FloatField(default=44.796942, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    news_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    place_news = models.ManyToManyField(Place)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title