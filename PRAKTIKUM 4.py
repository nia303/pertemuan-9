# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:58:40 2020

@author: LENOVO A9
"""

x = 0
names = []
nim = []
tgs = []
uts = []
uas = []
total = []

while True:
    nama = input("Nama : ")
    names.append(nama)
    Nim = input("Nim : ")
    nim.append(Nim)
    tugas = input("TUGAS : ")
    tgs.append(tugas)
    UTS = input("UTS : ")
    uts.append(UTS)
    UAS = input("UAS : ")
    uas.append(UAS)
    Total = (int(tugas)* .30) + (int(UTS)* .35) + (int(UAS)* .35)
    total.append(Total)
    
    data = ''
    while data != 'y' and data != 't':
        data = input("Tambah Data (y/t)? ")
         
        
    x += 1
    if data == 't':
        break
        
        
        
print("========================================================")
print(" | NO |  NAMA  |   NIM   | TUGAS | UTS  | UAS  | AKHIR |")
print("========================================================")
        
for n in range(x):
    print(" | ",n+1, "|", names [n], "|", nim[n], "|", tgs[n], "|", uts[n], "|", uas[n], " | ", total[n], " | ")
            
            
            
