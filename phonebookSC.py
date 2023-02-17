# -*- coding: utf-8 -*-
"""
Spyder Editor

@Author: Arnan
This is a temporary script file.
"""

def tambahKontak(nama, no):
    file = open('DaftarKontak.txt', 'a')
    file.write(nama)
    file.write("#")
    file.write(no)
    file.write("\n")
    file.close()

def writeKontak(nama, nomor, maxLine):
    file = open('DaftarKontak.txt', 'w')
    i = 0
    for i in range(maxLine):
        file.write(nama[i])
        file.write("#")
        file.write(nomor[i])
        file.write("\n")
    file.close()
    
def sortFile():
    temp = []
    file = open('DaftarKontak.txt', 'r')
    for line in file.readlines():
        temp.append(line)
    file.close()
    temp.sort()
    maxLine = len(temp)
    file = open('DaftarKontak.txt', 'w')
    for i in range(maxLine):    
        file.write(temp[i])
    file.close()

def editKontak():
    i = 0
    name = []
    nomor= []
    maxLine = 0
    isTidakAda = 0
    file = open('DaftarKontak.txt', 'r')
    for line in file.readlines():
        temp = line
        x = temp.split("#")
        x[-1] = x[-1].replace("\n", "")
        name.append(x[0])
        nomor.append(x[-1])
        maxLine = maxLine + 1
    pilih = input("Search\n1. Nama Kontak\n2. Nomor Kontak\n : ")
    if pilih == '1':
        nama = input("Nama Kontak dicari: ")
        for i in range(maxLine):
            if nama == name[i]:
                isTidakAda = 2
                print("Nama Kontak Ketemu dengan nomor ", nomor[i])
                pilih = input("ingin mengedit nama kontaknya?\n1. Ya\n2. Tidak\n : ")
                if pilih == '1':
                    isTidakAda = 1
                    name[i] = input("Nama Diganti: ")
                    print("Mengganti Nama Kontak Selesai")
        file.close()
        if isTidakAda == 0:
            print('Nama kontak tidak tersedia')
        elif isTidakAda == 1: 
            writeKontak(name, nomor, maxLine)
    else : 
        num = input("Nomor Kondak dicari: ")
        for i in range(maxLine):
            if num == nomor[i]:
                isTidakAda = 2
                print("Nomor Kontak Ketemu dengan nama ",name[i])
                pilih = input("ingin mengedit nama kontaknya?\n1. Ya\n2. Tidak\n : ")
                if pilih == '1':
                    isTidakAda = 1
                    nomor[i] = input("Nomor Diganti: ")
                    print("Mengganti Nomor Kontak Selesai")
        file.close()
        if isTidakAda == False:
            print("Nomor kontak tidak tersedia")
        elif isTidakAda == 1: 
            writeKontak(name, nomor, maxLine)
            
def daftarKontak():
    i = 1
    file = open('DaftarKontak.txt', 'r')
    for line in file.readlines():
        line = line.split("#")
        print(i,". ",line[0]," ", line[-1])
        i = i + 1
    file.close()
    
def deleteKontak():
    i = 0
    name = []
    nomor= []
    maxLine = 0
    isTidakAda = False
    file = open('DaftarKontak.txt', 'r')
    for line in file.readlines():
        temp = line
        x = temp.split("#")
        x[-1] = x[-1].replace("\n", "")
        name.append(x[0])
        nomor.append(x[-1])
        maxLine = maxLine + 1
    pilih = input("Delete by\n1. Nama Kontak\n2. Nomor Kontak\n : ")
    if pilih == '1':
        nama = input("Nama Kontak didelete: ")
        for i in range(maxLine):
            if nama == name[i]:
                del name[i]
                del nomor[i]
                isTidakAda = True
                print("Delete Nama Kontak Selesai")
                break
        file.close()
        if isTidakAda == False:
            print('Nama kontak tidak tersedia')
        else: 
            maxLine = len(name)
            writeKontak(name, nomor, maxLine)
    else : 
        num = input("Nomor Kondak didelete: ")
        for i in range(maxLine):
            if num == nomor[i]:
                del name[i]
                del nomor[i]
                isTidakAda = True
                print("Delete Nomor Kontak Selesai")
                break
        file.close()
        if isTidakAda == False:
            print("Nomor kontak tidak tersedia")
        else: 
            maxLine = len(name)
            writeKontak(name, nomor, maxLine)
    
#main Program
inProgram = True
while inProgram:
    pilih = input("Phonebook\n1. Tambah Kontak\n2. Search/Edit Kontak\n3. Delete Kontak\n4. Daftar Kontak\n99. Exit\n : ")
    if pilih == '1':
        namaKontak = input('Nama Kontak: ')
        nomorHp = input('Nomor Kontak: ')
        tambahKontak(namaKontak, nomorHp)
        sortFile()
    elif pilih == '2':
        editKontak()
    elif pilih == '3':
        deleteKontak()   
    elif pilih == '4':
        daftarKontak()  
    elif pilih == '99':
        inProgram = False