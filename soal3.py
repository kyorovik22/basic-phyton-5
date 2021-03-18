x = float (input ("Masukan nilai ujian teori = "))
y = float (input ("Masukan nilai ujian praktek = "))


if  x >= 70 and y >= 70 :
    print ("Selamat, anda lulus!")
elif x >= 70 and y < 70   :
    print ("Anda harus mengulang ujian praktek.")
elif x < 70 and y >=  70 :
    print ("Anda harus mengulang ujian Teori.")
else :
    print ("Anda harus mengulang ujian teori dan praktek.")
