from django.contrib import admin
from perpustakaan.models import *

# Register your models here.


class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'pengarang_id', 'penerbit_id', 'tahun', 'ISBN']
    search_fields = ['judul', 'pengarang_id', 'penerbit_id', 'tahun']
    # list_filter = ('kelompok_id')
    list_per_page = 5

class anggotaData(admin.ModelAdmin):
    list_display = ['nama', 'status_id', 'alamat', 'telp']
    search_fields = ['nama', 'status_id']
    list_per_page = 5

class pengarangData(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'telp']
    search_fields = ['nama']
    list_per_page = 5

admin.site.register(Kategori)
admin.site.register(status)
admin.site.register(anggota, anggotaData)
admin.site.register(pengarang, pengarangData)
admin.site.register(penerbit)
admin.site.register(Buku, BukuAdmin)
admin.site.register(Peminjaman)