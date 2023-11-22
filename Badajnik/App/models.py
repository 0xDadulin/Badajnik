from django.db import models
from django.db.models import JSONField

class Laboratory(models.Model):
    place_id = models.CharField(max_length=255, blank=True,null=True)
    name = models.CharField(max_length=255, blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    is_spending_on_ads = models.BooleanField(default=False)
    reviews = models.IntegerField(null=True, blank=True,)
    website = models.URLField(max_length=1024, blank=True,null=True)
    featured_image = models.URLField(max_length=1024, blank=True, null=True)
    main_category = models.CharField(max_length=255, blank=True, null=True)
    categories = JSONField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    workday_timing = models.CharField(max_length=255, blank=True,null=True)
    closed_on = JSONField(null=True, blank=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True,null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    review_keywords = JSONField(null=True, blank=True)
    link = models.URLField(max_length=1024, blank=True,null=True)
    owner = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
