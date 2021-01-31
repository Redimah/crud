"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perpustakaan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('pinjam/', pinjam),

    path('status/', status_anggota),
    path('tambah-status/', tambah_status),
    path('ubah-status/<int:id_status>', ubah_status, name='ubah-status/'),
    path('hapus-status/<int:id_status>', hapus_status, name='hapus-status/'),

    path('anggota/', data_anggota),
    path('tambah-anggota/', tambah_anggota),
    path('ubah-anggota/<int:id_anggota>', ubah_anggota, name='ubah-anggota/'),
    path('hapus-anggota/<int:id_anggota>', hapus_anggota, name='hapus-anggota/'),

    path('pengarang/', data_pengarang),
    path('tambah-pengarang/', tambah_pengarang),
    path('ubah-pengarang/<int:id_pengarang>', ubah_pengarang, name='ubah-pengarang/'),

    path('penerbit/', data_penerbit),
    path('tambah-penerbit/', tambah_penerbit),
    path('ubah-penerbit/<int:id_penerbit>', ubah_penerbit, name='ubah-penerbit/'),
    path('hapus-penerbit/<int:id_penerbit>', hapus_penerbit, name='hapus-penerbit/'),

    path('kategori/', kategori),
    path('tambah-kategori/', tambah_kategori),

    path('buku/', buku),
    path('tambah-buku/', tambah_buku),
    path('ubah-buku/<int:id_buku>', ubah_buku, name='ubah-buku/'),
    path('hapus-buku/<int:id_buku>', hapus_buku, name='hapus-buku/'),

    path('laporan/', data_laporan),
    path('laporan-xls/', export_xls),
]
