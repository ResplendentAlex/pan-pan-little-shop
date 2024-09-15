# <p align="center"><img src="staticfiles/assets/logo/icon_horizontal.png" style="width: 350px; margin-bottom: -25px" alt="Pan Pan Little Shop"></p>

This web application is a trading hub, specifically for art and crafts. It is made specifically for one of my college projects, PBP (Programming Berbasis Platform).

<br>

# ⚙️ **USAGE**<br>
You can access the live web application directly from the link below:
[LINK TO WEBPAGE](http://alexander-william-panpanlittleshop.pbp.cs.ui.ac.id/)

If you prefer to open it locally, however, simply clone this repository into your local folder. Make sure to install the requirements using the command `pip install -r requirements.txt`. Without doing so, the Django module would not be detected and the web application would not launch.

<br>

# 🛠️ **CONTRIBUTION**<br>
If you wish to contribute to this project, you can clone the project directly and edit it with any code editor to your liking, assuming that you have Django already setup. If not, you should first get Django installed into your device before proceeding as the application is fully developed within the Django framework.

Here a few links that you might find helpful in setting up your project:
1. [Real Python's Tutorial](https://realpython.com/django-setup/)
2. [Django Official Documentation](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

<br>

# 📃 **LICENSE**<br>
This project is licensed under the MIT License - refer to the LICENSE file for more details.

<br>

# 📝 **ASSIGNMENT**<br>
**Name** : Alexander William Lim <br>
**NPM** : 2306207505 <br>
**Class** : PBP F

## **TUGAS 2**<br>
### **Step-by-Step Project Setup Guide** <br>

**A. Konfigurasi Awal Proyek**
1. Pastikan Django sudah terinstall pada perangkat yang akan digunakan.

2. Dengan asumsi Django sudah terinstall, buatlah sebuah direktori lokal baru dengan nama `Pan Pan Little Shop`.

3. Buka terminal baru pada direktori tersebut, dan inisialisasi virtual environment menggunakan perintah berikut.<br>
    ```bash
    python -m venv env
    ```

4. Untuk mengaktifkan virtual environment, perintah berikut dapat digunakan.
    ```bash
    env\Scripts\activate
    ```

5. Setelah selesai melakukan setup virtual environment, buatlah sebuah berkas bernama `requirements.txt` pada direktori yang sama. Isi dari berkas adalah sebagai berikut.
    ```txt
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```

6. Lalu, lakukan instalasi *dependencies* menggunakan perintah berikut.
    ```bash
    pip install -r requirements.txt
    ```

7. Hanya setelah melakukan semua langkah-langkah diatas, proyek Django dapat diinisialisasi.
    ```bash
    django-admin startproject pan-pan-little-shop .
    ```

8. Konfigurasi `settings.py` dan menambahkan `localhost` dan `127.0.0.1` pada `ALLOWED_HOSTS`. Tujuan penambahan ini adalah agar kita dapat melakukan local hosting pada perangkat yang kita gunakan.

**B. Persiapan Awal Implementasi MVT**<br>

1. Buka terminal pada direktori proyek `pan-pan-little-shop`. Lalu, jalankan perintah berikut untuk membuat menginisialisasi *main app* baru.
    ```bash
    python manage.py starapp main
    ```

2. Daftarkan `'main'` sebagai item terakhir ke dalam daftar aplikasi `INSTALLED_APPS` pada `settings.py` dari direktori proyek.
    ```python
    INSTALLED_APPS = [
        ...,
        'main'
    ]
    ```

**C. Konfigurasi Templates Main App**<br>
1. Pada direktori `main`, buatlah sebuah direktori baru bernama `templates`.

2. Pada direktori baru tersebut, tambahkan berkas yang dinamakan `main.html`.

3. Isi berkas tersebut dengan desain tampilan yang telah ditentukan menggunakan **HTML**. `localhost` dapat digunakan untuk melihat perubahan yang telah dilakukan pada `main.html`.

**D. Konfigurasi Model Dasar**<br>

1. Pada berkas `models.py` dalam Aplikasi `main`, implementasikan model `Product` dengan menambahkan atribut dan properti menggunakan kode berikut.
    ```python
    from django.db import models

    class Product(models.Model)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()

        @property
        def is_product_available(self):
            return self.stock > 0
    ```
2. Setelah menambahkan model pada `models.py`, jalankan kedua perintah berikut pada terminal.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

**E. Menghubungkan View dengan Template**<br>
1. Buka berkas `views.py` pada aplikasi `main`.

2. Bila belum ada, tambahkan baris berikut pada baris-baris import dalam berkas `views.py`.
    ```python
    from django.shortcuts import render
    ```

3. Tambahkan fungsi `show_product()` dan isikan fungsi seperti di bawah ini.
    ```python
    def show_main(request):
        context = {
            'name' : 'Pan-Pan Self Portrait',
            'price': 'Rp. 200.000',
            'stock': '10',
            'description': 'A self portrait of Pan-Pan, the panda.'
        }

    return render(request, "main.html", context)
    ```

4. Modifikasi `main.html` dan ubah semua variabel yang menggunakan variabel yang terdaftar pada `context` di `views.py` dengan sintaks `{{ nama_variabel }}`

**F. Routing URL pada Aplikasi `main` dan proyek** <br>
1. Buat sebuah berkas bernama `urls.py` pada aplikasi main dan tambahkan kode berikut.
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

2. Pada berkas `urls.py` dalam direktori proyek, tambahkan kode berikut.
    ```python
    ...
    from django.urls import path, include
    ...

3. Tambahkan pula kode ini pada variabel `urlpatterns`.
    ```python
    urlpatterns = [
        ...
        path('', include('main.urls'))
        ...
    ]
    ```

**G. *Deployment* pada Pacil Web Service (PWS)**<br>
1. Setelah menyelesaikan semua langkah di atas, kita akan melakukan *deployment* web melalui Pacil Web Service (PWS).

2. Akses halaman PWS dan login menggunakan akun yang sudah terdaftar sebelumnya.

3. Tekan tombol `Create New Project` dan isikan dengan nama pemilik dan nama proyek yang sesuai. Lalu, simpan *credentials* yang akan ditampilkan pada halaman selanjutnya.

4. Pada `settings.py` tambahkan URL *deployment* web dan tambahkan ke dalam `ALLOWED_HOSTS`.

5. Jalankan perintah yang tertera pada tampilan *Project Command* pada PWS.

6. Setelah menjalankan perintah tersebut, kembalikan main branch dengan menggunakan perintah di bawah ini.
    ```bash
    git branch -M main
    ```

### **Bagan *Request Client* ke Django**<br>
<img src="assets/logo/bagan.png"></img>

### **Fungsi Git**<br>
Dalam sebuah pengembangan proyek perangkat lunak, `git` memainkan peran yang sangat penting serta menyediakan pengguna dengan beberapa fitur yang akan membantu dalam masa pengembangan. Beberapa diantaranya adalah:
1. ***Version Control*** - *developer* dapat menggunakan `git` sebagai tempat penyimpanan perubahan, dimana setiap perubahan pada kode yang sedang dikerjakan dapat disimpan pada `git`, sehingga akan mudah untuk membedakan versi-versi proyek yang sedang dikerjakan. 

2. **Sarana Kolaborasi** - para *developer* juga dapat dengan mudah berkolaborasi dengan *developer* lain menggunakan fitur-fitur seperti `clone`, `pull-request`, `fork repository`, dll. Ini memudahkan para *developer* jika ingin mengerjakan suatu proyek besar yang membutuhkan lebih dari satu orang untuk menyelesaikannya.

3. **Fleksibilitas Pengembangan Proyek** - `git` juga memungkinkan para *developer* untuk melakukan pengembangan proyek dimanapun dan kapanpun, karena `git` dapat diakses pada perangkat apa pun selama ada koneksi internet.

### Kenapa Django dijadikan *framework* yang pertama kali kami pelajari?
Menurut saya, walaupun ada beberapa hal yang mungkin menjadi pertimbangan para dosen saat memilih *framework* Django sebagai *framework* yang dipelajari, inti dari semua alasan tersebut adalah karena Django sangat *beginner-friendly*. 

Dalam pengembangan web, kita tidak hanya bermain pada tampilan dan logika backend seperti routing, tetapi juga ada basis data yang digunakan untuk melakukan query atau sistem keamanan yang digunakan untuk mencegah serangan siber. Sebagi pemula yang masih memiliki tidak ada sampai sedikit pengetahuan mengenai aspek-aspek tersebut, Django menjadi sebuah pilihan yang terbaik karena sudah menyediakan *library-library* yang dapat langsung digunakan.

### Mengapa model pada Django disebut sebagai *Object-Relational Mapping* (ORM)?
Ini karena Django tidak perlu menggunakan query untuk berinteraksi dengan basis data yang digunakan. Dengan kata lain, Django memungkinkan kita untuk secara langsung berinteraksi dengan basis data yang telah dibuat menggunakan objek yang disediakan oleh Python.
