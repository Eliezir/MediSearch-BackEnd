from django.db import models

class Medicine(models.Model):
    substance = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    laboratory = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    presentation = models.CharField(max_length=100)
    therapeutic_class = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    pf_12_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_17_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_18_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_19_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_19_percent_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_19_5_percent_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_20_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_20_percent_alc = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_20_5_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pf_21_percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cap = models.CharField(max_length=100)
    confaz_87 = models.BooleanField()
    icms_0_percent = models.BooleanField()
    hospital_only = models.BooleanField()
    

    def __str__(self):
        return self.product
