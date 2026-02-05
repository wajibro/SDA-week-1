data = list(range(1, 101))

def cek_prima(n):
    match n:
        case x if x < 2:
            return
        case 2:
            return n
        case x if x % 2 == 0:
            return
    
    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            return
    return n

angka_prima = [x for x in data if cek_prima(x)]
print(angka_prima)