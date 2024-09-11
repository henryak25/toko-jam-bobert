# Toko Jam Bobert

<h2>Website saya dapat diakses pada link: http://henry-aditya-tokojambobert.pbp.cs.ui.ac.id/</h2>

**<h3>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h3>**
1. Pertama-tama, saya membuat direktori lokal bernama toko-jam-bobert pada desktop saya.
2. Setelah itu saya menambahkan file README.md, membuat repo baru pada akun Github saya dan menginisialisasikannya dengan lokal.
3. Lalu melakukan set up environment, membuat dan mendownload text requirements, membuat proyek django baru menggunakan `git startproject`, membuat file gitignore, dan add commit push.
4. Setelah melakukan startproject dan melakukan push, saya melakukan `python manage.py startapp main` dan menambahkan app tersebut ke dalam `settings.py INSTALLED_APPS` pada direktori proyek `toko_jam_bobert`.
5. Sehabis itu, saya membuat model `Product` dalam models.py dengan atribut `nama, description, dan price`.
6. Lalu saya membuat fungsi show_main pada `views.py` untuk menampilkan `main.html` dan mengatur `urls.py` pada direktori main dan juga pada direktori toko_jam_bobert.
7. Terakhir, melakukan deployment dengan menambahkan pws `git remote add pws link`, lalu melakukan git mantras `add, commit, dan push terhadap origin dan juga pws`.

**<h3>Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</h3>**

![bagan Django](image/bagan.png/) 
1. urls.py menerima url yang sudah diambil dari HTTP yang dikirim oleh user. Lalu urls.py akan mengdirect dan akan membuka views yang mana berdasarkan url yang diterima tadi.
2. views.py akan memproses data yang diperlukan berdasarkan request. Disinilah views.py akan berhubungan dengan data yang ada dalam models.py. Lalu akan mengirimkan data tersebut ke dalam template HTML.
3. views lalu merender template menjadi HTML dan mengembalikannya sebagai response.

**<h3>Jelaskan fungsi git dalam pengembangan perangkat lunak!</h3>**
Git adalah *tools version control system* yang digunakan untuk mengelola perubahan kode selama pengembangan perangkat lunak. Berikut beberapa fungsi utama dari git:
1. Untuk Melacak dan Menyimpan Perubahan Kode<br>
Git memungkinkan user untuk melihat dan menyimpan perubahan yang terjadi pada kode. Jika terdapat perubahan baru terhadap kode, kita bisa melakukan git add, commit, dan push ke dalam repo untuk mengupdate versi terbaru dari perubahan kode kita. Jika terdapat kesalahan pada kode yang sekarang, kita bisa mengubah git ke versi sebelumnya karena git menyimpan perubahan-perubahan yang kita lakukan.

2. Untuk Mengerjakan Project Bersama Orang Lain<br>
Tentunya kita akan diperhadapkan dengan situasi dimana kita perlu bekerja sama dengan orang lain. Dengan adanya git, git memungkinkan banyak user untuk bekerja sama pada repo github yang sama.

3. Untuk Memudahkan Pengelolaan Versi<br>
Setiap perubahan yang dibuat dapat diberi label dengan versi tertentu menggunakan tag. Misalnya, jika setelah perilisan sebuah versi dengan tag 2.0 ditemukan bug, user bisa memperbaiki bug pada versi itu karena sudah ada tagnya.

**<h3>Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?</h3>**
Menurut saya sendiri, alasan pertamanya yaitu karena Django *beginner friendly* sehingga mudah untuk dipelajari, praktis, simpel, dan efisien. Selain itu, bahasa yang digunakan dalam Django adalah `Python`, dimana kita sudah mempelajari bahasa pemrograman tersebut pada Semester 1. Django juga menyediakan banyak fitur bawaan, seperti autentikasi, pengelolaan database, dan sistem template, yang memungkinkan pengembang fokus pada logika aplikasi tanpa harus membangun banyak hal dari nol. Selain itu, Django memiliki komunitas yang besar sehingga terdapat banyak sumber dalam internet mengenai tutorial Django bagi pemula.

**<h3>Mengapa model pada Django disebut sebagai ORM?</h3>**
Model pada Django disebut sebagai ORM atau *Object Relational Mapping* karena dia menghubungkan objek Python secara langsung ke tabel-tabel dalam basis data, dimana setiap atribut yang ada pada model akan diubah menjadi kolom pada tabel dalam database. Dengan ORM, kita dapat melakukan operasi CRUD pada database tanpa harus menulis query SQL secara langsung.