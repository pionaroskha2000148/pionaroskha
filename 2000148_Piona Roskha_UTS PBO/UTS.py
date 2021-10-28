#Piona Roskha
#2000148
#SIK A
#UTS PEMROGRAMAN BERORIENTASI OBJEK
user_id = 0
loop = "n"
user =  [
            {   
                "id":"1234",
                "no_rekening":"0812344321",
                "username":"test",
                "pin":"2002",
                "saldo":0
            },
            {   
                "id":"4321",
                "no_rekening":"0987654321",
                "username":"test2",
                "pin":"2003",
                "saldo":5000000
            }
        ]
status_login = False
pakai_atm = "y"
 
def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False       
     
def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1
 
def cek_rekening(no):
    for i in range(len(user)):
        if str(user[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 
def tranfer_uang(uang,no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang)
            user[index2]['saldo'] =user[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer senilai Rp."+str(uang)+" ke Rekening "+no_rekening)
            print("Sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Saldo yang tersedia tidak cukup")
             
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
            print("Anda berhasil menarik uang Rp."+str(uang))
            print("Sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Saldo yang tersedia tidak cukup")
 
 
while pakai_atm == "y":
    while status_login == False:
        print("SELAMAT DATANG DI ATM BAHAGIA")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
     
        cl = cek_login(pin)
        if cl != False:
            print("selamat datang "+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("PIN anda salah")
            print("")
            print("")
     
    while loop == "y" and status_login == True:
        u = user[cek_user(user_id)]
        print("SELAMAT DATANG DI ATM BAHAGIA")
        print('1. Informasi Saldo')
        print('2. Tambah Saldo')
        print('3. Ambil Saldo')
        print('4. Keluar Aplikasi')
        print("5. Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.",u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)
             
            if cnk >= 0:
                print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                nominal = input("Nominal Yang Akan Di Transfer : ")
                tranfer_uang(nominal,no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
                 
        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
             
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
             
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"