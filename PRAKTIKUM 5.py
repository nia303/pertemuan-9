# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:58:51 2020

@author: LENOVO A9
"""

print ("============================")
print ("===== [ program data ] =====")
print ("============================")
data = {}
while True :
    print("")
    m = input ("= [L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar =")
    print ("================================================")
    print (" | NO | NAMA | NIM | TUGAS | UTS | UAS | AKHIR |")
    print ("============ > NO DATA < =======================")
    if m.lower() == 'k' :
        break
    elif m.lower() == 'l' :
        print ("===================DAFTAR NILAI================= ")
        print ("=================================================")
        print (" | NO | NAMA | NIM | TUGAS | UTS | UAS | AKIHIR |")
        print ("=================================================")
        i = 0
        for x in data.items():
            i += 1
            print (" 1 | {0:9} | {1:9} | {2:9} | {3:9} | {4:9} | {5:9} |" .format(x[0] , x[1][0] , x[1][1] , x[1][2] , x[1][3] , x[1][4]))
            
        else :
            print (" === NO DATA ===")
            
    elif m.lower() == 't' :
        print ( "=== MENAMBAH DATA MAHASISWA ===")
        nama = input ("masukan NAMA : ")
        nim = input ("masukan NIM : ")
        tugas = float(input ("masukan nilai TUGAS : "))
        uts = float(input("masukan nilai UTS : "))
        uas = float(input("masukan nilai UAS : "))
        akhir = (0.30 * tugas ) + (0.35 * uts ) + (0.35 * uas)
        data [nama] = nim , tugas , uts , uas , akhir
        
    elif m.lower() == 'u' :
        print ("=== MENGUBAH DATA MAHASISWA ===")
        nama = input ("masukan NAMA : ")
        if nama in data.keys() :
            nim = input ("masukan NIM : ")
            tugas = float (input("masukan nilai TUGAS : "))
            uts = float(input("masukan nilai UTS : "))
            uas = float(input("masukan nilai UAS : "))
            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data [nama] = nim , tugas , uts , uas , akhir
            
        else :
            print(" === NO DATA ===")
            
    elif m.lower() == 'v' :
        print ("=== HAPUS DATA MAHASISWA ===")
        nama = input ("masukan NAMA : ")
        if nama in data.keys() :
            print ("DATA" , nama , "ADALAH {0} " .format (data [nama] ))
        else :
            print("=== NO DATA ===")
            
    else :
            print ("=== SELANJUTNYA ===")
            
            
            
            
            