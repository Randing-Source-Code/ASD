import os 
os.system('cls')

def jumpSearch(arr, x):

    n = len(arr)

    step = int(n ** 0.5)

    # Mencari block yang berisi elemen x (input)
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    # Melakukan linearing di block tersebut
    while arr[prev] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    # Cek apakah elemen yang dicari adalah elemen yang sesuai 
    if arr[prev] == x:
        return prev

    return -1

data = [5, 4, 9, 1, 2]

x = 5

result = jumpSearch(data, x)

if result == -1:
    print(f"Elemen {x} tidak ditemukan")
else:
    print(f"Elemen ditemukan pada index ke - {result}")