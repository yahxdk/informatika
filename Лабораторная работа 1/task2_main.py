BT_IN_KB = 1024
KB_IN_MB = 1024

amount = 1.44  # Информационный объем дискеты
pages = 100  # Количество страниц в книге
rows = 50  # Число строк на странице
symbols = 25  # Количество символов в строке
size = 4  # Байты для хранения кода одного символа
book = size * symbols * rows * pages
book_size_mb = book / (BT_IN_KB * KB_IN_MB)
x = int(amount // book_size_mb)

print("Количество книг, помещающихся на дискету:", x)
