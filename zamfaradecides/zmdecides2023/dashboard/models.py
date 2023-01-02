from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password

lgas = [
    ("Anka", "Anka"),
    ("Bakura", "Bakura"),
    ("Birnin Magaji", "Birnin Magaji"),
    ("Bukkuyum", "Bukkuyum"),
    ("Bungudu", "Bungudu"),
    ("Tsafe", "Tsafe"),
    ("Gummi", "Gummi"),
    ("Gusau", "Gusau"),
    ("Kaura Namoda", "Kaura Namoda"),
    ("Maradun", "Maradun"),
    ("Maru", "Maru"),
    ("Shinkafi", "Shinkafi"),
    ("Talata Mafara", "Talata Mafara"),
    ("Zurmi", "Zurmi"),
]

# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", 1)
        extra_fields.setdefault("last_name", "System")
        extra_fields.setdefault("first_name", "Administrator")

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    USER_TYPE = {1, "User"}
    
    def __str__(self):
        return self.username
    
    
class Agent(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=11, null=False, blank=False)
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    lga = models.CharField(null=False, max_length=100)
    ward = models.CharField(null=False, max_length=100)
    polling_unit = models.CharField(null=False, max_length=100)
    USER_TYPE = {2, "Agent"}
    
    def __str__(self):
        return self.name 


class LocalGovernment(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, choices=lgas, unique=True)


class PollingUnit(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    pu_id = models.CharField(max_length=100, null=False, blank=False)
    agent = models.ForeignKey(Agent, related_name="pu", on_delete=models.CASCADE)
    local_government = models.CharField(max_length=50, null=False, blank=False, choices=lgas)


class Ward(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    polling_units = models.ManyToManyField(PollingUnit, related_name="ward")
    local_government = models.CharField(max_length=50, null=False, blank=False, choices=lgas)


class Result(models.Model):
    polling_unit = models.ForeignKey(PollingUnit, related_name="result", on_delete=models.CASCADE)
    accredited_votes = models.FloatField(default=0, null=True, blank=True)
    casted_votes =models.FloatField(default=0, null=True, blank=True)
    valid = models.FloatField(default=0, null=True, blank=True)
    rejected = models.FloatField(default=0, null=True, blank=True)
    apc_result = models.FloatField(default=0, null=True, blank=True)
    pdp_result = models.FloatField(default=0, null=True, blank=True)
    other_result = models.FloatField(default=0, null=True, blank=True)
