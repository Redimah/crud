from django.shortcuts import render, redirect, HttpResponse, Http404
from perpustakaan.models import *
from perpustakaan.forms import *
from perpustakaan.resource import *

# Create your views here.

def base(request):
    konteks = {
        'judul': 'SELAMAT DATANG DI ',
    }
    return render(request, 'base.html', konteks)

def export_xls(request):
    pinjam = PeminjamanReport()
    dataset = pinjam.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Laporan.xls'
    return response

# -------------------------------- Table peminjaman ---------------------------------

def pinjam(request):
    if request.POST:
        form = FormPeminjaman(request.POST)
        if form.is_valid():
            form.save()
            form = FormPeminjaman()
            konteks = {
                'form' : form,
            }
        return redirect('/pinjam/', konteks)
    else:
        form = FormPeminjaman()
        judul = "PERPUSTAKAAN ONLINE"
        konteks = {
            'form' : form,
            'judul' : judul,
        }
    return render(request, 'peminjaman.html', konteks)

def data_laporan(request):
    rek = Peminjaman.objects.all()
    konteks = {
        'borr' : rek,
    }

    return render(request, 'laporan.html', konteks)

# --------------------------------- Table Status --------------------------------------


def status_anggota(request):
    statuss = status.objects.all()
    judul = "DATA STATUS PERPUSTAKAAN ONLINE"
    konteks = {
        'position': statuss,
        'judul' : judul,
    }

    return render(request, 'status.html', konteks)


def tambah_status(request):
    if request.POST:
        form = FormStatus(request.POST)
        if form.is_valid():
            form.save()
            form = FormStatus()
            konteks = {
                'form' : form,
            }
            return redirect('/tambah-status/', konteks)
    else:
        form = FormStatus()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah_status.html', konteks)


def ubah_status(request, id_status):
    statuss = status.objects.get(id=id_status)
    template = 'ubah_status.html'
    if request.POST:
        form = FormStatus(request.POST, instance=statuss)
        if form.is_valid():
            form.save()
            return redirect('ubah-status/', id_status=id_status)
    else:
        form = FormStatus(instance=statuss)
        konteks = {
            'form': form,
            'statuss': statuss,
        }
    return render(request, template, konteks)


def hapus_status(request, id_status):
    statuss = status.objects.filter(id=id_status)
    statuss.delete()
    return redirect('/status/')

# --------------------------------- Table Anggota --------------------------------------


def data_anggota(request):
    member = anggota.objects.all()

    konteks = {
        'member': member,
    }

    return render(request, 'anggota.html', konteks)


def tambah_anggota(request):
    if request.POST:
        form = FormAnggota(request.POST)
        if form.is_valid():
            form.save()
            form = FormAnggota()
            konteks = {
                'form': form,
            }
            return redirect('/tambah-anggota/', konteks)
    else:
        form = FormAnggota()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah_anggota.html', konteks)

def ubah_anggota(request, id_anggota):
    member = anggota.objects.get(id=id_anggota)
    template = 'ubah_anggota.html'
    if request.POST:
        form = FormAnggota(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('ubah-anggota/', id_anggota=id_anggota)
    else:
        form = FormAnggota(instance=member)
        konteks = {
            'form': form,
            'member': member,
        }
    return render(request, template, konteks)

def hapus_anggota(request, id_anggota):
    member = anggota.objects.filter(id=id_anggota)
    member.delete()
    return redirect('/anggota/')

# -------------------------------- Table Pengarang --------------------------------------


def data_pengarang(request):
    cipta = pengarang.objects.all()

    konteks = {
        'cipta': cipta,
    }

    return render(request, 'pengarang.html', konteks)


def tambah_pengarang(request):
    if request.POST:
        form = FormPengarang(request.POST)
        if form.is_valid():
            form.save()
            form = FormPengarang()
            konteks = {
                'form': form,
            }
            return redirect('/tambah-pengarang/', konteks)
    else:
        form = FormPengarang()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah_pengarang.html', konteks)


def ubah_pengarang(request, id_pengarang):
    cipta = pengarang.objects.get(id=id_pengarang)
    template = 'ubah_pengarang.html'
    if request.POST:
        form = FormPengarang(request.POST, instance=cipta)
        if form.is_valid():
            form.save()
            return redirect('ubah-pengarang/', id_pengarang=id_pengarang)
    else:
        form = FormPengarang(instance=cipta)
        konteks = {
            'form': form,
            'cipta': cipta,
        }
    return render(request, template, konteks)


def hapus_pengarang(request, id_pengarang):
    cipta = pengarang.objects.filter(id=id_pengarang)
    cipta.delete()
    return redirect('/pengarang/')

# ------------------------------- Table Penerbit --------------------------------------


def data_penerbit(request):
    cetaks = penerbit.objects.all()

    konteks = {
        'cetak': cetaks,
    }

    return render(request, 'penerbit.html', konteks)


def tambah_penerbit(request):
    if request.POST:
        form = FormPenerbit(request.POST)
        if form.is_valid():
            form.save()
            form = FormPenerbit()
            konteks = {
                'form': form,
            }
            return redirect('/tambah-penerbit/', konteks)
    else:
        form = FormPenerbit()

        konteks = {
            'form': form,
        }
    return render(request, 'tambah_penerbit.html', konteks)

def ubah_penerbit(request, id_penerbit):
    cetaks = penerbit.objects.get(id=id_penerbit)
    template = 'ubah_penerbit.html'
    if request.POST:
        form = FormPenerbit(request.POST, instance=cetaks)
        if form.is_valid():
            form.save()
            return redirect('ubah-penerbit/', id_penerbit=id_penerbit)
    else:
        form = FormPenerbit(instance=cetaks)
        konteks = {
            'form': form,
            'cetak': cetaks,
        }
    return render(request, template, konteks)

def hapus_penerbit(request, id_penerbit):
    cipta = penerbit.objects.filter(id=id_penerbit)
    cipta.delete()
    return redirect('/penerbit/')

# --------------------------------- Table kategori --------------------------------------

def kategori(request):
    jenis = Kategori.objects.all()

    konteks = {
        'jenis' : jenis,
    }

    return render(request, 'kategori.html', konteks)

def tambah_kategori(request):
    if request.POST:
        form = FormKategori(request.POST)
        if form.is_valid():
            form.save()
            form = FormKategori()
            konteks = {
                'form' : form,
            }
            return redirect('/tambah-kategori', konteks)
    else:
        form = FormKategori()
        konteks = {
            'form' : form,
        }
    return render(request, 'tambah_kategori.html', konteks)

def ubah_kategori(request, id_kategori):
    jenis = Kategori.objects.get(id=id_kategori)
    template = 'ubah_kategori.html'
    if request.POST:
        form = FormKategori(request.POST, instance=jenis)
        if form.is_valid():
            form.save()
            return redirect('ubah-kategori/', id_kategori=id_kategori)
    else:
        form = FormKategori(instance=jenis)
        konteks = {
            'form' : form,
            'jenis': jenis,
        }
    return render(request, template, konteks)

def hapus_kategori(request, id_kategori):
    jenis = Kategori.objects.filter(id=id_kategori)
    jenis.delete()
    return redirect('/kategori')

# ----------------------------------- Table Buku --------------------------------------

def buku(request):
    books = Buku.objects.all()
    judul = "DATA BUKU"
    konteks = {
        'books': books,
        'judul' : judul,
    }

    return render(request, 'buku.html', konteks)


def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            konteks = {
                'form': form,
            }
            return redirect('/tambah-buku/', konteks)
    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah_buku.html', konteks)


def ubah_buku(request, id_buku):
    books = Buku.objects.get(id=id_buku)
    template = 'ubah_buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('ubah-buku/', id_buku=id_buku)
    else:
        form = FormBuku(instance=books)
        konteks = {
            'form' : form,
            'books' : books,
        }

    return render(request, template, konteks)

def hapus_buku(request, id_buku):
    books = Buku.objects.filter(id=id_buku)
    books.delete()
    return redirect('/Buku')