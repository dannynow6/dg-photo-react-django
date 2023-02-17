from django.db import models

# DG Photos-v2 models


class Photo(models.Model):
    """A model representing a photo"""

    TYPES_CHOICES = [
        ("LS", "Landscape"),
        ("SP", "Street"),
        ("MP", "Macro"),
        ("AP", "Astrophotography"),
        ("PT", "Portrait"),
        ("NP", "Night"),
        ("BW", "Black & White"),
        ("TP", "Travel"),
        ("AS", "Abstract"),
        ("EP", "Experimental"),
        ("FP", "Fashion"),
        ("LE", "Long Exposure"),
        ("AL", "Aerial"),
    ]

    FORMAT_CHOICES = [
        ("FF", "Full-Frame"),
        ("MF", "Medium-Format"),
        ("AC", "APS-C"),
        ("FT", "Micro Four Thirds"),
        ("OF", "One-Inch"),
    ]

    type = models.CharField(max_length=5, choices=TYPES_CHOICES)
    location_city = models.CharField(max_length=125, blank=True)
    location_country = models.CharField(max_length=125, blank=True)
    title = models.CharField(max_length=250)
    camera_make = models.CharField(max_length=100)
    camera_model = models.CharField(max_length=100)
    format = models.CharField(max_length=5, choices=FORMAT_CHOICES)
    description = models.CharField(max_length=250, blank=True)
    year_taken = models.DateField(blank=True)
    lens_make = models.CharField(max_length=125, blank=True)
    lens_model = models.CharField(max_length=125, blank=True)
    focal_length = models.CharField(max_length=75, blank=True)
    picture = models.ImageField(upload_to="photos/", blank=True)

    def __str__(self) -> str:
        """return a string representation of Photo model"""
        title = self.title
        # geo = self.location_country
        id = self.id
        # camera = self.camera_make
        # cam_mod = self.camera_model
        description = self.description
        year = self.year_taken
        return f"{id} | {title.title()} | {description[:50]}... | {year}"
