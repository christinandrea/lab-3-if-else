# Christina Andrea Putri - Universitas Kristen Duta Wacana

#Buatlah algoritma dan program yang dapat menentukan jenis tunjangan dan tambahan gaji yang didapat karyawan
# Tunjangan anak hanya didapatkan oleh karyawan yang sudah menikah dan memiliki anak
# Tunjangan keluarga hanya diberikan kepada karyawan laki-laki yang sudah menikah
# Untuk karyawan yang memiliki anak < 3 atau gaji < Rp3.000.000,- akan diberikan tambahan gaji sebesar 10% dari gaji karyawan

#Input : gaji, status, jk, punya anak/tidak, jml anak
#Proses : menentukan jenis tunjangan yang didapat dan tambahan gaji yang didapat
#Output : jenis tunjangan dan tambahan gaji

try:
    nama = input("Nama Anda : ")
    gaji = int(input("Gaji Anda : Rp "))
    jk = input("Jenis Kelamin (L/P) : ")
    status = input("Menikah/Belum Menikah : ")
    tambahan = gaji*0.1
    
    if status=="Menikah":
        anak = input("Punya Anak/Tidak Punya Anak : ")
        if anak == "Punya Anak" : 
            jml_anak = int(input("Jumlah Anak : "))
            if jml_anak < 3 or gaji < 3000000 : 
                print("Selamat Anda mendapatkan tambahan gaji sebesar Rp", tambahan)
                if jk == "L":
                    print("Selamat Anda juga mendapatkan tunjangan keluarga!")
                else : 
                    print("Maaf Anda tidak mendapatkan tunjangan keluarga.")
        elif anak == "Tidak Punya Anak" and jk=="L":
            print("Anda hanya mendapatkan tunjangan keluarga. \n Silahkan gunakan dengan bijaksana.")
        else : 
            print("Maaf Anda tidak mendapat tunjangan dari perusahaan. \n Terimakasih atas pengertiannya")
    else : 
        print("Maaf Anda tidak mendapat tunjangan dari perusahaan. \n Terimakasih atas pengertiannya.")

except : 
    print("Terjadi kesalahan saat input data. Silahkan coba lagi.")