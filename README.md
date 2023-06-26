# UAS_PAA_2_F55121070_Yunita_Anggeraini

A. Analisis Algoritma Bubble Sort dan Insertion Sort

1. Bubble Sort:

Worst Case (Kasus Terburuk):
Pada kasus terburuk, Bubble Sort akan memiliki kompleksitas waktu O(n^2), di mana 'n' adalah jumlah elemen yang diurutkan. Kasus terburuk terjadi ketika elemen-elemen terurut secara terbalik, sehingga setiap elemen harus bergeser ke posisi akhirnya melalui pertukaran berulang.

Best Case (Kasus Terbaik):
Pada kasus terbaik, Bubble Sort memiliki kompleksitas waktu O(n), di mana 'n' adalah jumlah elemen yang diurutkan. Kasus terbaik terjadi ketika elemen-elemen sudah dalam urutan yang benar dan tidak memerlukan pertukaran tambahan selama iterasi.

Average Case (Kasus Rata-rata):
Pada kasus rata-rata, Bubble Sort memiliki kompleksitas waktu O(n^2), di mana 'n' adalah jumlah elemen yang diurutkan. Bubble Sort akan melakukan pertukaran secara berulang untuk setiap pasangan elemen yang tidak berurutan. Jumlah rata-rata pertukaran tergantung pada distribusi elemen-elemen dalam data yang diurutkan.

2. Insertion Sort:

Worst Case (Kasus Terburuk):
Pada kasus terburuk, Insertion Sort memiliki kompleksitas waktu O(n^2), di mana 'n' adalah jumlah elemen yang diurutkan. Kasus terburuk terjadi ketika elemen-elemen terurut secara terbalik, dan setiap elemen harus dipindahkan ke posisi awalnya melalui pergeseran elemen lain.

Best Case (Kasus Terbaik):
Pada kasus terbaik, Insertion Sort memiliki kompleksitas waktu O(n), di mana 'n' adalah jumlah elemen yang diurutkan. Kasus terbaik terjadi ketika elemen-elemen sudah dalam urutan yang benar, sehingga tidak diperlukan pergeseran tambahan saat memasukkan setiap elemen ke dalam posisinya yang tepat.

Average Case (Kasus Rata-rata):
Pada kasus rata-rata, Insertion Sort memiliki kompleksitas waktu O(n^2), di mana 'n' adalah jumlah elemen yang diurutkan. Insertion Sort akan melakukan pergeseran elemen saat memasukkan setiap elemen ke dalam posisinya yang tepat. Jumlah rata-rata pergeseran tergantung pada distribusi elemen-elemen dalam data yang diurutkan.

B. Analisis Algoritma Traveling Salesman Problem(TSP) dan Djikstra

1. Algoritma TSP (Traveling Salesman Problem):

Worst Case (Kasus Terburuk):
Pada TSP, tidak ada kasus terburuk yang tetap ada. Algoritma TSP memiliki kompleksitas waktu eksponensial O(n!), di mana 'n' adalah jumlah node atau kota yang harus dikunjungi. Kasus terburuk terjadi ketika ada banyak node dan permutasi semua kemungkinan jalur harus diuji untuk menemukan jalur terpendek.

Best Case (Kasus Terbaik):
Pada TSP, kasus terbaik terjadi ketika terdapat sedikit node, seperti hanya dua node atau ketika semua node memiliki bobot yang sama. Pada kasus terbaik ini, algoritma TSP dapat mencapai kompleksitas waktu O(1) atau konstan, karena jalur terpendek langsung diketahui.

Average Case (Kasus Rata-rata):
Tidak ada analisis rata-rata yang tepat untuk algoritma TSP karena kompleksitas waktu algoritma ini sangat tergantung pada ukuran masalah. Namun, pada umumnya, kompleksitas waktu algoritma TSP cenderung eksponensial O(n!), yang berarti semakin banyak node yang harus dikunjungi, semakin tinggi kompleksitas waktu yang diperlukan.

2. Algoritma Dijkstra:

Worst Case (Kasus Terburuk):
Pada Dijkstra, kasus terburuk terjadi ketika setiap simpul atau node harus diproses dan setiap sisi atau edge dalam graf harus dijelajahi. Dalam kasus ini, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah simpul dan E adalah jumlah sisi dalam graf.

Best Case (Kasus Terbaik):
Pada kasus terbaik, algoritma Dijkstra memiliki kompleksitas waktu O(V + E), di mana V adalah jumlah simpul dan E adalah jumlah sisi dalam graf. Kasus terbaik terjadi ketika simpul awal adalah simpul tujuan atau ketika simpul tujuan berada tepat di sebelah simpul awal.

Average Case (Kasus Rata-rata):
Pada kasus rata-rata, algoritma Dijkstra memiliki kompleksitas waktu O((V + E) log V). Namun, kompleksitas waktu rata-rata yang sebenarnya dapat bervariasi tergantung pada struktur graf, jarak antara simpul, dan bobot sisi. Dalam kasus rata-rata, algoritma Dijkstra cenderung lebih efisien daripada kasus terburuk, tetapi tetap memiliki kompleksitas waktu yang bergantung pada ukuran graf.
