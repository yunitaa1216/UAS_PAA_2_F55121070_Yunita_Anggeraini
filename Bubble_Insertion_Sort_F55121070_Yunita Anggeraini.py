#YUNITA ANGGERAINI
#F55121070
#UAS PAA 2
#Algoritma Bubble Sort dan Insertion Sort
import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # Tampilkan iterasi pertama dan terakhir
        if i < 5 or i >= n - 5:
            print(f"Iterasi {i + 1}: {arr}")

    end_time = time.time()
    execution_time = end_time - start_time
    print("Waktu komputasi:", execution_time)

    return arr

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        # Tampilkan iterasi pertama dan terakhir
        if i < 5 or i >= n - 5:
            print(f"Iterasi {i + 1}: {arr}")

    end_time = time.time()
    execution_time = end_time - start_time
    print("Waktu komputasi:", execution_time)

    return arr


# Main program
def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33,
           90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63,
           84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31,
           15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    while True:
        print("Sebelum pengurutan:", arr)
        print("\nPilihan pengurutan:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        choice = int(input("Masukkan pilihan (1/2): "))

        if choice == 1:
            sorted_arr = bubble_sort(arr.copy())
        elif choice == 2:
            sorted_arr = insertion_sort(arr.copy())
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
            continue

        print("\nSetelah pengurutan:", sorted_arr)

        repeat = input("Lakukan pengurutan lagi? (y/n): ")
        if repeat.lower() != 'y':
            break


if __name__ == '__main__':
    main()