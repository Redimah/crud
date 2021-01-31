from import_export import resources
from perpustakaan.models import *
from import_export.fields import Field

class PeminjamanReport(resources.ModelResource):
    kodepeminjaman = Field(attribute='kodepeminjaman', column_name='Kode')
    anggota_id__nama = Field(attribute='anggota_id__nama', column_name='Nama Anggota')
    buku_id__judul = Field(attribute='buku_id__judul', column_name='Judul Buku')
    tglpinjam = Field(attribute='tglpinjam', column_name='Tanggal Pinjam')
    tglkembali = Field(attribute='tglkembali', column_name='Tanggal Kembali')
    jumlahpinjaman = Field(attribute='jumlahpinjaman', column_name='Jumlah')
    class Meta:
        model = Peminjaman
        fields = ['kodepeminjaman', 'anggota_id__nama', 'buku_id__judul', 'tglpinjam', 'tglkembali', 'tglkembali', 'jumlahpinjaman']
        export_order = ['kodepeminjaman', 'anggota_id__nama', 'buku_id__judul', 'tglpinjam', 'tglkembali', 'jumlahpinjaman']