import os
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Menambah Daftar Email
def addFile():
    file = open("receiver_list.txt", "a")
    file.write(input("Masukkan Email Penerima: "))
    file.write("\n")
    file.close()

# Melihat Daftar Email
def readFile():
    file = open("receiver_list.txt", "r")
    print(file.read())

# Menghapus Daftar Email
def removeFile():
    os.remove("receiver_list.txt")

# Send Email I've Try Ma Best, luvv Ma self <3 
def thisIsMyBest():
    # Memindah Daftar Email receiver_list.txt ke listEmail = []
    listEmail = []
    file = open("receiver_list.txt", "r")
    for line in file:
        listEmail.append(line.strip())

    fromaddr = input("Masukan Email Anda: ")
    paswd = getpass.getpass("Masukan Pasword Anda: ")
    toaddr = listEmail 
    
    # Isi Email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ', '.join(listEmail) #Menggunakan Join Agar Bisa Mengirim Pesan ke List
    msg['Subject'] = "Bismillah, Ya Allah This Is My Best"
 
    body = "Bismillah Semoga Berhasil"
 
    msg.attach(MIMEText(body, 'plain'))

    # Lampiran, sesuaikan nama filename dengan nama di attachment harus sesuai direktori lokal
    filename = "PPW04_M0519006_Aditya Aulia Al-Azizi.pdf"
    attachment = open("C:\\Users\\PRAD.ID\\Documents\\Adit\\basic-python\\Final Project\\PPW04_M0519006_Aditya Aulia Al-Azizi.pdf", "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, paswd)
    print ("Login Berhasil.")
    print ("Sedang Mengirim Email...")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    print("Email Telah Berhasil Terkirim Ke: ")
    for x in range(len(listEmail)):
        print ("{}. {}".format(x+1, listEmail[x]))

print ("Selamat Datang!")

while True:
    # Tampilan Menu Utama
    print ('''
---Pilihan Menu--
1. Melihat Daftar Email.
2. Menambah Daftar Email.
3. Menghapus Daftar Email.
4. Mengirim Email.
5. Keluar.
    ''')

    # Input User
    masukanUser = int(input("Masukkan Pilihan Menu: "))

    # Percabangan Menu
    if masukanUser == 1:
        try:
            print("Menampilkan Semua Email: ")
            readFile()
        except FileNotFoundError:
            print("Daftar Email Masih Kosong.")
    
    elif masukanUser == 2:
        jmlh = int(input("Berapa Email yang Akan Ditambahkan: "))
        for y in range (jmlh):
            addFile()
        print ("Email Berhasil Ditambahkan.")

    elif masukanUser == 3:
        try:
            removeFile()
            print ("Daftar Email Berhasil Dihapus.")
        except FileNotFoundError:
            print("Daftar Email Tidak Ada.")
    
    elif masukanUser == 4:
        print("Silahkan Login Terlebih Dahulu.")
        thisIsMyBest()

    elif masukanUser == 5:
        print ("Program Selesai, Sampai Jumpa :)")
        break

    else:
        print ("Pilihan Menu Salah!")
