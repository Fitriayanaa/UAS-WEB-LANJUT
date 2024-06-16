from django.db import models

class Bos(models.Model):
    name = models.CharField(max_length=255)

class Karyawan(models.Model):
    name = models.CharField(max_length=255)
    bos = models.OneToOneField(
        Bos, 
        on_delete=models.CASCADE,
        related_name='karyawan'
    )

class Customer(models.Model):
    name = models.CharField(max_length=255)
    karyawan = models.ForeignKey(
        Karyawan,
        on_delete=models.CASCADE,
        related_name='customers'
    )
    
class Produk(models.Model):
    name = models.CharField(max_length=255)
    customers = models.ManyToManyField(
        Customer,
        related_name='produks'
    )

'''
penjelasan dari 3 table yang telah dibuat
1 .one-to-one (satu-ke-satu)
relasi:Setiap objek Karyawan akan terkait dengan satu objek Bos, dan setiap objek Bos akan terkait 
dengan satu objek Karyawan. Ini berarti setiap karyawan bekerja di bawah satu bos, dan setiap bos 
memiliki satu karyawan yang bekerja di bawahnya secara langsung. Dalam hal ini, OneToOneField digunakan
untuk menunjukkan bahwa hubungan antara Bos dan Karyawan adalah satu-satu, yang berarti setiap karyawan 
hanya memiliki satu bos, dan setiap bos hanya memiliki satu karyawan yang terkait langsung dengannya.
secara keseluruhan, relasi ini menggambarkan bahwa setiap bos memiliki satu karyawan yang bekerja di
bawahnya secara langsung, dan setiap karyawan bekerja di bawah satu bos.

'''
'''
2. one-to-many (satu-ke-banyak)
relasi:Setiap objek Customer akan terkait dengan satu objek Karyawan, sedangkan satu objek Karyawan
dapat terkait dengan banyak objek Customer. Ini menggambarkan hubungan bahwa setiap pelanggan (Customer)
terhubung ke satu karyawan (Karyawan), sementara satu karyawan dapat melayani banyak pelanggan.
secara keseluruhan, relasi ini menggambarkan bahwa setiap pelanggan memiliki karyawan yang terkait
dengannya, dan satu karyawan dapat melayani banyak pelanggan.

'''
'''
3. many-to-many (banyak-ke-banyak)
relasi:Setiap objek Produk dapat terkait dengan banyak objek Customer, dan sebaliknya, setiap objek
Customer juga dapat terkait dengan banyak objek Produk. Ini menggambarkan hubungan bahwa setiap produk
dapat dibeli oleh banyak pelanggan, dan setiap pelanggan dapat membeli banyak produk. Dalam hal ini, 
ManyToManyField digunakan untuk menunjukkan bahwa ada hubungan banyak-ke-banyak antara objek Produk dan
objek Customer. secara keseluruhan, relasi ini menggambarkan bahwa setiap produk dapat dibeli oleh banyak 
pelanggan, dan setiap pelanggan dapat membeli banyak produk.

'''