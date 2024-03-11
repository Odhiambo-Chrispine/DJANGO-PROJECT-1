from django.db import models

# Create your models here.

category_choice = (
    ('tablets','tablets'),
    ('capsules','capsules'),
    ('injectables','injectables'),
    ('solutions','solutions'),
    ('sachets','sachets'),
)

class Items(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True, choices = category_choice)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    batch_number = models.CharField(max_length=50, blank=False, null=True)
    expiry_date =  models.DateTimeField(auto_now_add=False, auto_now=False)
    quantity_of_packs = models.IntegerField(default=0, blank=False, null=True)
    cost_per_pack = models.IntegerField(default=0.0, blank=False, null=True)
    units_per_pack = models.IntegerField(default=0, blank=False, null=True)
    markup = models.IntegerField(default=0, blank=False, null=True)
    cost_per_unit_bp = models.IntegerField(default=0.0, blank=False, null=True)
    cost_per_unit_sp = models.IntegerField(default=0.0, blank=False, null=True)
    total_amount = models.IntegerField(default=0.0, blank=False, null=True)
    quantity_received = models.IntegerField(default=0, blank=False, null=True)
    received_by = models.CharField(max_length=50, blank=False, null=True)
    received_by_internally = models.CharField(max_length=50, blank=False, null=True)
    quantity_issued = models.IntegerField(default=0, blank=False, null=True)
    issued_from = models.CharField(max_length=50, blank=False, null=True)
    issued_by = models.CharField(max_length=50, blank=False, null=True)
    issued_to = models.CharField(max_length=50, blank=False, null=True)
    issued_from_internally = models.CharField(max_length=50, blank=False, null=True)
    issued_by_internally = models.CharField(max_length=50, blank=False, null=True)
    issued_to_internally = models.CharField(max_length=50, blank=False, null=True)
    phone_number_r = models.CharField(max_length=50, blank=False, null=True)
    entered_by = models.CharField(max_length=50, blank=False, null=True)
    phone_number_e = models.CharField(max_length=50, blank=False, null=True)
    reorder_level = models.IntegerField(default=0, blank=False, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.item_name
        