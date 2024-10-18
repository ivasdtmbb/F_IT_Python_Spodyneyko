# TODO Найдите количество книг, которое можно разместить на дискете


STORAGE_VOLUME_BYTES = 1.44 * 1024 * 1024
PAGES_QUANTITY = 100
LINES_PER_PAGE = 50
SYMBOLS_PER_LINE = 25
BYTE_PER_SYMBOL = 4

book_size = PAGES_QUANTITY * LINES_PER_PAGE * SYMBOLS_PER_LINE * BYTE_PER_SYMBOL
books_on_disk = int(STORAGE_VOLUME_BYTES // book_size)
#print(book_size)


print("Количество книг, помещающихся на дискету:", books_on_disk)

