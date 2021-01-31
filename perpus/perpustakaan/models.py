import datetime
import calendar
from django.db import models
from django.utils import timezone

YEAR_CHOICES = [(r, r) for r in range(1800, datetime.date.today().year+1)]

# Create your models here.


class status (models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status


class anggota (models.Model):
    nama = models.CharField(max_length=50)
    status_id = models.ForeignKey(
        status, on_delete=models.CASCADE, null=True
    )
    alamat = models.CharField(max_length=200)
    telp = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.nama


class pengarang(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=200)
    telp = models.IntegerField(null=True)

    def __str__(self):
        return self.nama


class penerbit(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.CharField(max_length=200)
    telp = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.nama


class Kategori(models.Model):
    kategori = models.CharField(max_length=30)

    def __str__(self):
        return self.kategori


class Buku(models.Model):
    judul = models.CharField(max_length=50)
    kategori_id = models.ForeignKey(
        Kategori, on_delete=models.CASCADE, null=True)
    pengarang_id = models.ForeignKey(
        pengarang, on_delete=models.CASCADE, null=True)
    penerbit_id = models.ForeignKey(
        penerbit, on_delete=models.CASCADE, null=True)
    tahun = models.IntegerField(('tahun'),choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    ISBN = models.IntegerField(null=True)

    def __str__(self):
        return self.judul


class Peminjaman(models.Model):
    kodepeminjaman = models.CharField(max_length=10, primary_key=True)
    anggota_id = models.ForeignKey(
        anggota, on_delete=models.CASCADE, null=True)
    buku_id = models.ForeignKey(
        Buku, on_delete=models.CASCADE, null=True)
    tglpinjam = models.DateField()
    tglkembali = models.DateField()
    jumlahpinjaman = models.IntegerField(null=True)

    def __str__(self):
        return self.kodepeminjaman
