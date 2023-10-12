# TODO Найдите количество книг, которое можно разместить на дискете
M_BYTE = 1024
K_BYTE = 1024

DISK_SIZE_BYTE = 1.44 * M_BYTE * K_BYTE
BOOK_PAGE_NUM = 100
STRING_PAGE_NUM = 50
SYMS_PAGE_NUM = 25
SYMS_SIZE_B = 4

BOOK_SIZE_B = BOOK_PAGE_NUM * STRING_PAGE_NUM * SYMS_PAGE_NUM * SYMS_SIZE_B

print("Количество книг, помещающихся на дискету:", int(DISK_SIZE_BYTE // BOOK_SIZE_B))
