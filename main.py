from cs50 import SQL 

db = SQL("sqlite:///file.db")
db.execute("DELETE FROM daftar_pemilih")
db.execute("CREATE TABLE IF NOT EXISTS daftar_pemilih (id_pilih INT NOT NULL, name TEXT PRIMARY KEY NOT NULL, pilihan INT NOT NULL)")

capres_1 = 0
capres_2 = 0
capres_3 = 0
id_pemilih = [1,2,3]

while True:
    print("===============================================")
    print("****         PILPRES RI TAHUN 2024         ****")
    print("===============================================")
    if id_pemilih == []:
        break

    else:
        nama_pemilih = input("Masukkan Nama anda : ")
        pemilih = int(input("Masukkan ID pemilih anda : "))
        if pemilih in id_pemilih:
            id_pemilih.remove(pemilih)
            print (f"\nAnda terdaftar di TPS ini")
            pilih = int(input("Silahkan ketik ( 1/ 2/ 3 ) untuk CAPRES pilihan anda : "))
            db.execute("INSERT INTO daftar_pemilih (id_pilih, name, pilihan ) VALUES(?, ?, ?)", pemilih, nama_pemilih, pilih)
            if pilih == 1:
                capres_1+=1
            elif pilih == 2:
                capres_2+=1
            elif pilih == 3:
                capres_3+=1
            print("Terima kasih telah memilih\n")       
                           
        else:
            print("Maaf...Kamu tidak terdaftar atau telah selesai memilih\n")
           
print("Semua warga telah memilih, hasil akhirnya adalah sebagai berikut :")
hasil = db.execute("SELECT* FROM daftar_pemilih")
for i in hasil:
    print(i)
print(f"\nCapres no 1 dengan jumlah suara : {capres_1}")
print(f"Capres no 2 dengan jumlah suara : {capres_2}")
print(f"Capres no 3 dengan jumlah suara : {capres_3}")

