from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NotDeleted(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(default=False, help_text="Used for soft delete")

    all_object = models.Manager()
    objects = NotDeleted()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class Case(BaseModel):
    CASE_TYPE = (
        ('Civil', 'Civil'),
        ('Intellectual Property', 'Intellectual Property'),
        ('Criminal Defense', 'Criminal Defense'),
        ('Employment', 'Employment'),
        ('Personal Injury', 'Personal Injury'),
        ('Bankrupcy', 'Bankrupcy',)
    )

    CASE_STATUS = (
        ('Further Action Needed', 'Further Action Needed'),
        ('Processing', 'Processing'),
        ('Deposition Data Set', 'Deposition Data Set'),
        ('Trial date pending', 'Trial date pending'),
        ('Trial Date Set', 'Trial Date Set'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(max_length=225)
    detail = models.TextField()
    number = models.IntegerField(unique=True)
    case_type = models.CharField(max_length=225, choices=CASE_TYPE)
    case_status = models.CharField(max_length=225, choices=CASE_STATUS)
    opened_at = models.DateField()
    lawyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lawyer_cases')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_cases')


class Invoice(BaseModel):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_invoices')
    lawyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lawyer_invoices')
