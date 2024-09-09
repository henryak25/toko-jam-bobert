from django.db import models
from django.db import models

class Product(models.Model):
    nama_barang = models.CharField(max_length=255)
    nama_mahasiswa = models.TextField()
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()

    @property
    def is_overpriced(self):
        return self.price > 5
# Create your models here.
