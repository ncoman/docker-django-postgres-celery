from django.db import models

ACCOUNT_CHOICES = (
    ("reseller", "Reseller"),
    ("direct", "Direct"),
)


class Company(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True, unique=False)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_CHOICES, default="direct")

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=254, null=True, blank=True, unique=False)
    phone = models.CharField(max_length=254, null=True, blank=True, unique=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
    key = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}, {self.company}, {self.key}"
