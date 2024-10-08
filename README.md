# Toko Jam Bobert


<h2>Website saya dapat diakses pada link: http://henry-aditya-tokojambobert.pbp.cs.ui.ac.id/</h2>


<h1>TUGAS 06</h1>

**<h2>Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!</h2>**
Untuk membuat script, untuk dynamic content, friendly and interactive websites, form validation, dan banyak lainnya. Contoh penggunaannya yaitu image carousel, games, menampilkan informasi berdasarkan waktu (semacam countdown contohnya), dan  ganti styling css secara dinamis.
Lalu, dengan kemampuan manipulasi DOM, JavaScript memungkinkan kita untuk mengakses dan mengubah elemen HTML dan CSS secara langsung. Selain itu, JavaScript melakukan validasi form secara real-time, sehingga dapat meningkatkan efisiensi dan mengurangi kesalahan saat mengirim data ke server. Melalui AJAX, JavaScript dapat mengambil dan memperbarui data dari server tanpa reload, sehingga tidak perlu untuk reload-reload lagi.


**<h2>Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?</h2>**
Dengan menggunakan await, kita membuat eksekusi kode yang sekarang menunggu hingga operasi asynchronous selesai.
Ketika kita menggunakan fetch(), fungsi ini akan mengembalikan sebuah Promise yang mewakili respons dari permintaan HTTP. fetch() sendiri bersifat asynchronous, sehingga ia berjalan di belakang dan tidak memblokir eksekusi dari kode yang lain.
Dengan adanya await di depan fetch(), maka kita memaksa JavaScript untuk menunggu hingga Promisenya selesai sebelum melanjutkan ke langkah berikutnya. Hasil dari Promise tersebut (biasanya berupa response HTTP) kemudian bisa disimpan dalam variabel dan digunakan di kode berikutnya.
Mengapa perlu pakai fetch? Karena kalo pake XMLHttpRequest memiliki beberapa kelemahan, seperti penanganan yang kurang rapi ketika bekerja dengan callback, lalu fetch juga jauh lebih sederhana penulisan sintaksnya, dan XMLHttpRequest memiliki keterbatasan dalam mendukung alur kode yang lebih modern. Basically fetch adalah XMLHttpRequest versi modernnya. (Sumber: Tutorial)
Jika tidak menggunakan await, fungsi fetch() tetap akan berjalan dan mereturn Promise, tetapi karena sifatnya asynchronous, eksekusi kode berikutnya tidak menunggu hingga proses fetch() selesai. Akibatnya kode di bawahnya akan langsung dijalankan.

```python
const productEntries = await getProductEntries();
async function getProductEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }
```

**<h2>Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?</h2>**
Jadi,  kegunaan dari csrf_exempt yaitu untuk menonaktifkan pengecekan cross site request forgery. Django secara otomatis menambahkan token CSRF di form HTML yang dikirim melalui metode POST (atau metode yang memodifikasi data seperti PUT dan DELETE), yang kemudian akan divalidasi saat server menerima permintaan tersebut. Lalu mengapa kita malah perlu untuk mematikan fitur ini ketika berfungsi untuk melindungi website dari serangan CSRF? Yaitu karena view yang akan digunakan untuk AJAX POST tidak ngegenerate csrf token (data dikirim melalui AJAX request dengan menggunakan metode POST). Misal pada create_product_entry.html, pada file itu ada {% csrf_token %} yang menggeneraate token csrf. Apa yang akan terjadi kalau kita tidak menggunakan csrf_exempt? Maka akan mendapatkan 403 Forbidden (tapi pas aku tes ternyata tidak diberi warning apapun, cuman tidak berhasil nambah product? Will find this out later)

**<h2>Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?</h2>**
Karena frontend rentan terhadap manipulasi input data yang diberikan. Meskipun kita sudah menerapkan validasi di frontend, user tetap bisa dengan mudah memodifikasi kode HTML, JavaScript, atau mengirimkan request ke server melalui media seperti Postman atau curl. Penyerang bisa memasukkan kode SQL berbahaya yang dapat membahayakan database jika input hanya dibersihkan di frontend. Selain itu, Jika validasi hanya dilakukan di frontend, maka tetap ada resiko data yang masuk ke database tidak sesuai format. Sehingga agar keamanan terjamin dengan baik, maka pembersihan input data juga perlu dilakukan di backend.

**<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!</h2>**
1. Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
Pertam-tama, menambahkan fungsi add_product_entry_ajax pada views.py, lalu pathnya jangan lupa masukkan ke urls.py

```python
    @csrf_exempt
    @require_POST
    def add_product_entry_ajax(request):
        name = strip_tags(request.POST.get("name"))
        description = strip_tags(request.POST.get("description"))
        price = request.POST.get("price")
        user = request.user

        new_product = Product(
            name=name, description = description,
            price = price,
            user=user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    # Ini di urls.py
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax')
```

2. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
Lalu, menambahkan tag <script></script> beserta isi-isinya (logic for button modal, buat product_entry_cards) pada main.html, div product_entry_cards, button baru untuk handle event add ajax (bakal dilead ke addProductEntry, dimana addProductEntry bakal ngelead ke main:add_product_entry_ajax), dan juga div untuk menampilkan modal buat isi data untuk add ajax nanti.
```python
    # logic untuk buka tutup modal
    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');
  
        modal.classList.remove('hidden'); 
        setTimeout(() => {
          modalContent.classList.remove('opacity-0', 'scale-95');
          modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }
    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');
  
        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');
  
        setTimeout(() => {
          modal.classList.add('hidden');
        }, 150); 
    }
    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);
    document.getElementById("productEntryForm").addEventListener("submit", (e) => {
      e.preventDefault();
      addProductEntry();
    })
```

3. pada script itu, masukkan logic buat ngeload isi html untuk div product_entry_cards. Div product_entry_cards ini berfungsi buat nampilin card card dari product yang udah kita buat. Mungkin untuk function selain refresh tetap sama dengan yang ada di tutorial (hanya ganti variabel paling), tetapi yang berbeda ada di fungsi refreshProductEntries, dimana tentunya saya mengambil code dari yang ada pada card_product_html ke dalam isi dari refreshProductEntries ini.  Pada akhir script kita juga perlu untuk memanggil refreshProductEntries() sehingga setiap kali webnya diload scriptnya kan nanti dijalanin maka function refreshProductEntries akan berjalan untuk mengisi html dalam product_entry_cards.

```python
    async function refreshProductEntries() {
        document.getElementById("product_entry_cards").innerHTML = "";
        document.getElementById("product_entry_cards").className = "";
        const productEntries = await getProductEntries();
    
        let htmlString = "";
        let classNameString = "";
    
        if (productEntries.length === 0) {
            classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
            htmlString = `
                <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                    <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                    <p class="text-center text-gray-600 mt-4">Belum ada data product pada toko jam bobert.</p>
                </div>
        `;
        }
        else {
            classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
            productEntries.forEach((item) => {
                const name = DOMPurify.sanitize(item.fields.name);
                const description = DOMPurify.sanitize(item.fields.description);
                htmlString += `
                <div class="relative break-inside-avoid bg-gray-800 rounded-2xl shadow-lg border border-gray-600 transform transition-transform duration-300 hover:scale-105 hover:shadow-2xl">
                    <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center space-x-1">
                        <div class="w-8 h-8 bg-slate-600 rounded-full opacity-70"></div>
                        <div class="w-8 h-8 bg-slate-600 rounded-full opacity-70"></div>
                    </div>
                    <div class="p-4 text-gray-300">
                        <h3 class="text-xl font-semibold mb-2 hover:text-pink-400 transition-colors duration-300">${name}</h3>
                        <p class="text-gray-400">${item.fields.time}</p>
                    </div>
                    <div class="p-4">
                        <p class="font-medium text-lg mb-1 text-gray-100 animate-bounce">Deskripsi Produk</p>
                        <p class="text-gray-300 mb-2">${description}</p>
                        <div class="mt-4">
                        <p class="font-semibold text-gray-200 mb-2">Status Overpriced</p>
                        <div class="relative pt-1">
                            <div class="flex mb-2 items-center justify-between">
                            <span class="text-xs font-semibold inline-block py-1 px-2 rounded-full bg-slate-500 text-gray-900">
                                ${item.fields.price > 5 ?'Mahal kali astaga' : 'Terlalu murah bang buset' }
                            </span>
                            </div>
                            <div class="w-full bg-slate-600 h-2 rounded overflow-hidden animate-pulse">
                            <div style="width:${item.fields.price > 10 ? 100 : item.fields.price*10}%;" class="bg-slate-500 h-full transition-width duration-500"></div>
                            </div>
                        </div>
                    </div>
                </div>
                    <div class="absolute top-0 right-4 flex space-x-2">
                        <a href="/edit-product/${item.pk}" class="bg-yellow-400 hover:bg-yellow-500 text-black rounded-xl p-2 shadow transform transition duration-300 hover:rotate-3">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                        </svg>
                        </a>
                        <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-xl p-2 shadow transform transition duration-300 hover:rotate-3">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 animate-spin hover:animate-none" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 012 0v6a1 1 11-2 0V8zm5-1a1 1 00-1 1v6a1 1 102 0V8a1 1 00-1-1z" clip-rule="evenodd" />
                        </svg>
                        </a>
                    </div>
                </div>
                `;
            });
        }
        document.getElementById("product_entry_cards").className = classNameString;
        document.getElementById("product_entry_cards").innerHTML = htmlString;    
    }
```
Lalu, untuk memastikan itu datanya diambil dari data milik user yang logged in, maka implementasinya:
```python
    async function getProductEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }
    # pada function refreshProductEntries ada ini:
    const productEntries = await getProductEntries();
```


4. Setelah itu, tambahkan DOMPurify dan strip tags untuk pembersihan data.

```python
    # pada main.html
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
    const name = DOMPurify.sanitize(item.fields.name)
    const description = DOMPurify.sanitize(item.fields.description)
    # pada forms.py
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
```

5. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan. 
Tidak perlu refresh setiap kali ngeadd data produk baru kalo asinkronus karena bisa berubah secara dinamis.


<h1>TUGAS 05</h1>

**<h2>1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!</h2>**
Terdapat 4 jenis selector, yaitu element selector, id selector, inline style, dan class selector. Dari keempat selector tersebut, yang akan diutamakan terlebih dahulu adalah inline styling, id selector, class selector, dan terakhir element selector. 
Pemrioritasan selector ini berdasarkan seberapa spesifik selectornya, inline style paling spesifik karena langsung ke element itu pemberian stylenya, baru  id selector, class buat sekelompok element dengan ciri yang sama, dan elemen paling umum karena targetnya adalah elemennya html seperti h1 langsung. Specificity dari inline style adalah 1000, id selector memiliki specificity 100, class selector memiliki specificity 10, dan element selector memiliki specificity sebesar 1. Ada juga selector universal yang ditandai dengan *, universal selector ini specificitynya sendiri adalah 0.
<br>
Contoh inline styling:  `<div style="max-width: 1280px; margin: 0 auto; padding-left: 16px; padding-right: 16px;"></div>`<br>
Contoh id selector : `#div1{}`<br>
Contoh class selector: `.tembok{}`<br>
Contoh element selector: `h1{}`<br>
Contoh universal selector: `*{}`


**<h2>2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!</h2>**
Agar website yang kita buat bisa diakses dari berbagai platform, tidak spesifik untuk satu device saja seperti hanya bisa diakses dari desktop view. Kita perlu memastikan bahwa website yang kita buat bisa beradaptasi dengan resolution dari device user, dengan begitu jumlah user yang bisa akses web kita tentunya akan naik.
Contoh website yang belum menerapkan responsive web design adalah https://pbp.cs.ui.ac.id (meski ini sepertinya intentional :V), https://academic.ui.ac.id  dan https://dequeuniversity.com/library/responsive/1-non-responsive. Mereka tergolong tidak responsif karena tidak ada penyesuaian design webnya terhadap perubahan resolution device, intinya cuman semacam shrink down in size agar bisa muat di screen lebih kecil.
Lalu contoh website yang sudah menerapkan responsive web design adalah websitenya spotify. Contoh aplikasi yang responsive adalah discord, spotify, whatsapp, youtube, dan line.

**<h2>3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!</h2>**
Margin itu jarak antara diri sendiri dengan element parentnya atau apapun itu yang ada di luar dirinya sendiri. Simpelnya ngebuat area kosong di luar garis border. Cara implementasinya:  `margin: some measurements`<br>
Kalau border itu untuk memberikan border bagi elemen itu sendiri, berguna untuk melihat size ukurannya dari elemen yang kita buat itu ambil seberapa banyak space. Garis yang diciptakan border bisa kita pakai sebagai acuan buat margin dan padding (asal jangan aneh-aneh widthnya tebal). Cara implementasinya: `border: 2px solid black` akan membentuk border dengan ketebalan 2px<br>
Padding buat memberikan jarak antara diri sendiri dengan element direct childrennya atau konten apapun di dalam. Simpelnya buat ruang kosong antara garis border dan isi konten. Implementasinya tinggal semacam `padding: some measurements`<br>

<h1>Examples of padding and margin:</h1>

![jsonall](image/dengan-padding-margin.png/) 

<br>
<h1>Examples of without padding and without margin</h1>

![jsonall](image/tanpa-padding-margin.png/)

**<h2>4. Jelaskan konsep flexbox dan grid layout beserta kegunaannya!</h2>**
Kalau kata para sepuh, flexbox adalah layout yang sangat overpowered. Dari namanya saja sudah cukup self explanatory mengapa sangat terkenal flexbox ini, yaitu karena penataan letaknya fleksibel dan responsif untuk elemen yang berubah ukuran tergantung ukuran layar. Fitur-fitur terkenal dalam flexbox yaitu:<br>
flex-direction, untuk mengatur mau vertikal apa horizontal.<br>
align-items dan justify-content. Pada justify-content kita bisa atur penyajian items dengan fitur space-between, space-evenly, atau space-around.<br>

Kegunaan dari flexbox ini biasa terdapat pada saat membuat tata letak navbar, card layout, atau menu yang responsif. Pokoknya flexbox sangat terpakai ketika kita ingin membuat tata letak yang fleksibel dan responsif untuk elemen yang berubah ukuran tergantung pada ukuran layar.

Grid layout adalah sistem tata letak 2D yang memungkinkan penyusunan elemen dalam bentuk baris dan kolom. Grid layout sangat fleksibel untuk membuat tata letak yang terstruktur seperti dashboard ataupun galeri, kalau bisa menguasai grid layout pasti websitenya bakal kelihatan bagus. Grid layout ini juga dinamis atau bisa dibilang responsif terhadap perubahan. Kita bisa atur sebuah item mengambil berapa banyak row atau column begitu. Visit `https://www.w3schools.com/CSS/css_grid.asp` to see how grid layout works.

**<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Kustomisasi halaman login, register, dan tambah product semenarik mungkin.</h2>**

Pertama-tama taro script pada base.html `<script src="https://cdn.tailwindcss.com"></script>`. Script ini kepake buat tailwind yang ada di register.html dan create_new_product.html. Sedangkan untuk halaman login saya pakainya css. Notable use buat tailwindnya itu animate-bounce (very easy to implement). Untuk Register.html dan login.html saya pakai themenya keunguan sedangkan create_new_product pakai biru tua.
<br><br>
- Implementasikan fungsi untuk menghapus dan mengedit product:

	Tambahkan fungsi edit_product dan delete_product pada views.py, jangan lupa masukkan ke urlsnya. Untuk edit product sendiri akan dibawa ke edit_product.html untuk mengedit productnya.

    ```python
    def edit_product(request, id):
        product = Product.objects.get(pk = id)
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        context = {'form': form}
        return render(request, "edit_product.html", context)

    def delete_product(request, id):
        product = Product.objects.get(pk = id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```

- Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.<br>
    Dengan menggunakan tailwind. Untuk designnya masih agak mirip dengan yang di tutorial, saya hanya mengubah warnanya, ganti design sedikit-sedikit, dan memberikan efek-efek yang lebih lucu seperti saat dihover scalenya akan naik untuk product card, lalu text nama product ketika dihover akan ganti warna. Kurang lebih saya cuman mainin animate dalam class daftar productnya, seperti `animate-bounce, animate-spin, animate-pulse`.
    <br><br>

- Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
    ```python
    <div class="absolute top-0 right-4 flex space-x-2">
    <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-400 hover:bg-yellow-500 text-black rounded-xl p-2 shadow transform transition duration-300 hover:rotate-3">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
    </a>
    <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-xl p-2 shadow transform transition duration-300 hover:rotate-3">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 animate-spin hover:animate-none" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 012 0v6a1 1 11-2 0V8zm5-1a1 1 00-1 1v6a1 1 102 0V8a1 1 00-1-1z" clip-rule="evenodd" />
      </svg>
    </a>
  </div>
  ```
    Penjelasan: href untuk membawa kita ke fungsi yang didefine di views, svg xmlns buat bikin ikon dari delete sama editnya, pada elemen delete saya berikan animation spin dimana jika kita hover ke ikonnya maka hovernya akan berhenti.  Pada elemen edit ketika dihover saya bikin dia rotate sedikit sebanyak 3 degrees.
    <br><br>
-  Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
    ```python
        {% if not product_entries %}
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data product pada toko jam bobert.</p>
            </div>
    ```
    Mengecek jika product_entries ada atau tidak, jika tidak ada maka akan menampilkan sebuah div yang mengcenter item isinya yaitu sebuah image dan sebuah paragraph element.
    <br><br>

- Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
    untuk cara kerja dia bisa responsible identik dengan yang tutorial. saya ganti design aja (font style dan bg) kalo hover ke text logout akan muncul red background di belakangnya jadinya interaktif dengan user bisa lihat kalo itu merupakan button.








<h1>TUGAS 4</h1>

**<h2>1.    Apa perbedaan antara HttpResponseRedirect() dan redirect()</h2>**
HTTPResponseRedirect() hanya menerima argumen pertama dalam bentuk url, sedangkan redirect() dapat menerima model, view, atau sebuah url. Fungsi redirect sendiri secara internal ada memanggil HTTPResponseRedirect() atau HTTPResponsePermanentRedirect(). Secara fungsional, keduanya memiliki fungsi yang sama, tetapi redirect lebih mudah ditulis dan juga lebih fleksibel penggunaannya.

info tambahan: reverse() adalah sebuah fungsi yang digunakan untuk mendapatkan URL dari suatu view berdasarkan nama viewnya. Jadinya ini meski terlihat parameternya sama, sebenarnya direverse dulu yang HttpResponseRedirect biar jadi URL.
```python
response = HttpResponseRedirect(reverse("main:show_main"))
return redirect('main:show_main')
```
<br><br>

**<h2>2.    Jelaskan cara kerja penghubungan model Product dengan User!</h2>**
Dengan menggunakan foreign key. Foreign key ini berfungsi menyambungkan data-data dari 2 tabel, dimana biasa relasinya itu one to many antar 2 model. Model User menggunakan model bawaan Django yaitu django.contrib.auth.models.User, sedangkan model Product kita buat di models.py. Foreign key ini terdapat di user yang kita tambahkan di Product, sehingga terhubung dengan user. Ketika membuat product yang baru, kita menggunakan request.user untuk menyimpan siapa owner dari product itu.

```python
from django.contrib.auth.models import User
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
<br><br>

**<h2>3.    Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.</h2>**
Perbedaan authentication dan authorization, yaitu authentication berfungsi untuk memverifikasi identitas dari user. Authentication memastikan bahwa user adalah orang yang mereka mau login sebagai, dimana authentication melibatkan checking credentials seperti username dan password. Authorization adalah proses untuk memberikan atau membatasi akses dan fitur berdasarkan hak akses oleh user, seperti apakah user bisa mengakses admin page atau tidak, bisa pakai tools apa gitu. 
Saat pengguna login, maka untuk verify apakah penggunanya beneran ada itu menggunakan authentication, kalau sudah masuk ke dalam akun baru disebut authorization. Biasanya ada session yang membuat akun tetap terlogin saat sudah melewati authentication, sehingga tidak perlu login ulang ketika pindah ke page lain pada website yang sama.
Cara Django implementasi authentication yaitu dengan menggunakan modul django.contrib.auth. Modul ini dapat membuat login form, lalu password hashing, dan membuat login&logout views. Untuk implementasi authorization, Django menggunakan permissions dan groups. Hal tersebut adalah bagaimana Django mengelola hak akses user terhadap sumber daya atau action tertentu. Model permissions contohnya yaitu add, change, delete, and view. Fitur groups yaitu pengelompokkan user berdasarkan kekuasaan/perannya, seperti admin dan user biasa.

Kepake disini .authnya
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
```
<br><br>
**<h2>4.    Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?</h2>**
Django mengingat user yang sudah login dengan menggunakan cookies, pada cookies tersebut tersimpan session ID unik untuk identifikasi user. Django juga menggunakan middleware untuk mengecek apakah session ID di server sama dengan yang ada pada cookie, jika cocok maka Django menganggap user masih terlogin dan belum logout. Kegunaan lain dari cookies yaitu untuk melakukan tracking pengguna, untuk meningkatkan usability website, dan untuk personalization user pada website. Tidak semua cookies aman, bisa saja cookies dimanfaatkan oleh serangan siber man-in-the-middle. Terdapat beberapa contoh kasus dimana kita tidak dianjurkan untuk accept cookies, yang pertama yaitu ketika websitenya unencrypted, ketika cookies tidak memiliki tanda secure dan HTTPOnly,  lalu ketika cookiesnya merupakan third party cookies, dan ketika cookies menggunakan data personal seperti SSN.

last login untuk informasi terakhir login kapan
```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
```

**<h3>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)</h3>**
- implementasi registrasi, login, dan logout dengan pertama-tama import `UserCreationForm, AuthenticationForm, authenticate, login, logout, dan login_required`. Lalu membuat function `login_user` dengan parameter request dan juga `login.html`. Jika request adalah POST dan formnya valid maka akan membuat session untuk pengguna yang berhasil login, jika requestnya adalah GET maka akan menampilkan default page dari `login.html`.

Seperti terlihat pada fungsi login_user ini, kalo berhasil masuk yaudah dibawa ke show_main yang akan merender `main.html`. Kalo tidak masuk block code if == 'POST' kan berarti GET, jadi sepertinya render default page `login.html`?
```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
untuk fungsi logout, mereturn kembali ke page `login.html`, logout(request) sendiri berfungsi untuk mengakhiri session user.

```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

<h1>1.  Akun Pertama</h1>

![bagan Django](image/freefire.png/)
<h1>2.  Akun Kedua</h1>

![bagan Django](image/payfire.png/) 
- Menghubungkan model Product dengan User.
Penghubungan antara Product dan User yaitu dengan menggunakan foreign key, terdapat pada:
```python
#ini di models
user = models.ForeignKey(User, on_delete=models.CASCADE)
#ini di views, penghubungan dengan product dengan user pada product_entry.user = request.user
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry= form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
```
- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
Pada fungsi `show_main`, di contextnya masukkan variabel name dengan isi `request.user.username` untuk informasi username dan variabel last_login untuk informasi last login pada halaman utama aplikasi.
```python
#pada views
context = {
        'name': request.user.username,
        'description' : 'jujujuujujuupiter',
        'price': 50,
        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],
    }
#pada main.html
<p>{{ name }}<p>
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

<br><br>
<h1>TUGAS 3</h1>

**<h3>Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?</h3>**

Kita perlu data delivery ini karena kita perlu mengirim data atau menerima data dengan aman, akurat, dan efisien antar berbagai user platform.  Contoh dari data delivery yaitu XML dan JSON.
Pada platform yang sudah terdevelop dengan kompleks, sering ada berbagai komponen yang perlu untuk berkomunikasi satu dengan yang lain. Contohnya yaitu komunikasi antar frontend stack dan backend stack. Data delivery ini sangat terpakai karena terkadang data itu harus diantar secara real time, contohnya pada saat pengguna melakukan pembayaran online ovo gopay gitu atau di aplikasi chat yang harus cepat transmisi datanya.
Tanpa data delivery, platformnya kemungkinan besar jadi statis dan tidak interaktif. Tanpa data delivery, maka data yang diisi pada form tidak bisa sampai ke server. Tanpa data delivery, tidak ada jembatan untuk memindahkan data dari satu tempat ke tempat lainnya. 


**<h3>Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?</h3>**
Sources: [source 1](https://aws.amazon.com/compare/the-difference-between-json-xml/)

Menurut saya, XML dan JSON punya kelebihannya dan kekurangannya masing-masing, meski sepertinya JSON lebih baik secara umum daripada XML. 
JSON memiliki ukuran file yang lebih kecil dan memiliki sekuritas yang lebih tinggi daripada XML. Hal ini disebabkan oleh struktur tag XML yang lebih kompleks dibandingkan JSON yang hanya menggunakan key-value,  struktur data XML juga rentan terhadap modifikasi sehingga menciptakan resiko keamanan yang dikenal sebagai XML external entity injection.  
XML juga perlu diparse menggunakan XML parser, sedangkan JSON diparse menggunakan standard JS function. Salah satu alasan yang membuat JSON lebih terkenal yaitu karena JSON lebih mudah dibaca dan tidak menggunakan tags. Seperti yang sudah saya jelaskan juga di paragraf sebelumnya, JSON memiliki file size yang lebih kecil dan data transmissionnya lebih cepat. Kesimpulannya, kita pakai XML ketika membutuhkan representasi data kompleks, lalu JSON untuk aplikasi yang membutuhkan pertukaran data cepat, ringan, dan lebih efisien.


**<h3>Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?</h3>**
Sources: [source 1](https://www.javatpoint.com/django-form-validation#:~:text=The%20is_valid()%20method%20is,data%20into%20a%20cleaned_data%20attribute)

Method is_valid() digunakan untuk mengecek validasi setiap field dari form, dimana method ini terdefinisi dalam Django Form class. Method ini akan meng return true jika datanya valid, lalu akan menaruh semua data yang terisi dalam form ke cleaned_data attribute.
Mungkin salah satu contoh yang saya kepikiran, yaitu ketika kita mau submit form dengan ada field yang masih kosong datanya. Ketika saya tidak isi lalu pencet button yang berfungsi untuk submit, maka fungsi is_valid() akan mengembalikan false dan formnya kasih pesan “please fill out this field”. Tanpa method ini, datanya nanti ada field yang kosong atau tidak sesuai dengan keinginan kita.



**<h3>Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?</h3>**
Sources: [source 1, ](https://medium.com/@xploiterd/how-to-perform-and-exploit-cross-site-request-forgery-csrf-attacks-1764c0f23585)
[source 2](https://www.synopsys.com/glossary/what-is-csrf.html#:~:text=A%20CSRF%20token%20is%20a,token%20for%20every%20user%20session)

Sebelum menjelaskan alasan tersebut, kita perlu mengerti dulu apa itu csrf_token dan apa kegunaannya. Kata csrf berasal dari serangan siber CSRF yang kependekannya adalah Cross-Site Request Forgery. Cross-Site Request Forgery itu adalah jenis serangan di mana penyerang mencoba membuat user website melakukan aksi yang tidak diinginkan pada suatu web ketika usernya sudah terautentikasi.
Oleh karena hal tersebut, maka diciptakanlah yang namanya csrf_token, yaitu token yang berfungsi untuk mencegah serangan CSRF. Csrf_token ini merupakan sebuah string unik yang digenerate secara random. Token ini digunakan pada setiap formulir sehingga ketika server mendapat request, token csrf ini dipakai untuk verifikasi bahwa request itu asli, no fekfek, dan berasal dari user asli.
Jika kita tidak memakai csrf_token, tentunya akan menjadi rentan terhadap serangan siber CSRF yang sudah saya jelaskan di atas. Bisa saja CSRF memandu user untuk mengubah password akunnya, untuk mendapatkan informasi mengenai user, dan banyak lainnya.
Kalau saya lihat, berarti csrf_token ini tergenerate pada statement code {% csrf_token %} pada file create_product_entry.html, tepatnya setelah tag `<form>`.



**<h3>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h3>**
- Saya membuat forms.py, dimana model diambil dari class Product dalam models.py. Lalu fields yang diambil adalah name, description, dan price.
- Menambahkan 4 fungsi pada views.py

    ```py
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    ```
- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

    ```python
    urlpatterns = [
        #path('', show_main, name='show_main'),
        #path('create-product-entry', create_product_entry, name='create_product_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```
- Implementasi csrf_token terdapat pada statement code {% csrf_token %} pada file create_product_entry.html, tepatnya setelah tag `<form>`.
<h1>1. Json ambil semua</h1>

![jsonall](image/jsonall.png/) 
<h1>1. Xml ambil semua</h1>

![xmlall](image/xmlall.png/) 
<h1>1. Json ambil specified id</h1>

![jsonbyid](image/jsonbyid.png/) 
<h1>1. Xml ambil specified id</h1>

![xmlbyid](image/xmlbyid.png/)

<br><br>
<h1>TUGAS 2</h1>

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