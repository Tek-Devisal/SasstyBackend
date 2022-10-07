from django.db import models

class Ads(models.Model):
    name = models.CharField(max_length=500, null=False)
    link = models.CharField(max_length=1000, null=False)
    banner = models.ImageField(blank=False, default="", upload_to="images/ads/")

    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)
