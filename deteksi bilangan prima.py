data = list(range(1, 101))

def cek_prima(n):
    match n:
        case 2:
            return True
        case x if x < 2:
            return False
        case _:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

status = 0
print("""
==============================
1. Cek Prima berdasarkan input
2. Cek Prima 1 - 100
==============================
""")
status = input('Masukkan opsi anda: ')
status = int(status)
match status:
    case 1:
        input_prima = input('Masukkan angka yang ingin diperiksa: ')
        input_prima = int(input_prima)
        print(f'Angka {input_prima} adalah', "benar angka prima" if cek_prima(input_prima) else "bukan angka prima")
    case 2:
        for i in data:
            if cek_prima(i):
                print(i," ", end='')
    case _:
        print("""
1. Cek Prima berdasarkan input
2. Cek Prima 1 - 100
""")
        status = input('Masukkan opsi anda: ')