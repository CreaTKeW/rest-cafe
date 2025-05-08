# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cafe(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=False, null=False)
    name = models.TextField(blank=True, null=True)
    map_url = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    has_sockets = models.BigIntegerField(blank=True, null=True)
    has_toilet = models.BigIntegerField(blank=True, null=True)
    has_wifi = models.BigIntegerField(blank=True, null=True)
    can_take_calls = models.BigIntegerField(blank=True, null=True)
    seats = models.TextField(blank=True, null=True)
    coffee_price = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'cafe'
