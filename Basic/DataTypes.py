# ============================
#   Data Types in Python
# ============================

# ---- Integer (bilangan bulat)
x = 10
print(type(x))  # <class 'int'> → tipe data untuk bilangan bulat tanpa decimal

# ---- Float (bilangan desimal)
y = 3.14
print(type(y))  # <class 'float'> → tipe untuk angka dengan decimal

# ---- String (teks)
name = "Fazel"
print(type(name))  # <class 'str'> → tipe text yang diapit tanda kutip

# ---- Boolean (True / False)
is_active = True
print(type(is_active))  # <class 'bool'> → digunakan untuk kondisi logika

# ---- List (kumpulan data, bisa campur tipe)
numbers = [1, 2, 3, 4, 5]
print(type(numbers))  # <class 'list'> → mutable (bisa diubah), berurutan

# ---- Tuple (kumpulan data, tidak bisa diubah)
point = (10, 20)
print(type(point))  # <class 'tuple'> → immutable (tidak bisa diubah), berurutan

# ---- Set (kumpulan unik, tidak berurutan)
unique_nums = {1, 2, 3, 3, 3}
print(type(unique_nums))  # <class 'set'> → menyimpan elemen unik, tidak ada duplikasi

# ---- Dictionary (key-value pairs)
person = {
    "name": "Fazel",
    "age": 21,
    "active": True
}
print(type(person))  # <class 'dict'> → menyimpan data dalam pasangan key:value

# ---- NoneType (kosong / tidak ada nilai)
data = None
print(type(data))  # <class 'NoneType'> → representasi “tidak ada nilai”
