from circle import Circle
from triangle import Triangle

# Membuat objek lingkaran
lingkaran = Circle("merah", 5)
print("Lingkaran berwarna", lingkaran.get_color())
print("Luas lingkaran:", lingkaran.area())

# Membuat objek segitiga
segitiga = Triangle("biru", 4, 6)
print("Segitiga berwarna", segitiga.get_color())
print("Luas segitiga:", segitiga.area())
