import os,sys,time

def bersih():
    os.system("clear")

def menu():
    bersih()
    print("")
    os.system("figlet Home")
    print("# Author : You")
    print("===============================")
    print("1). Perkenalan")
    print("2). Update")
    masuk = input("Enter (1/2): ")
    if masuk == "1":
       name = input("Masukkan nama: ")
       print("Hallo", name)
    elif masuk == "2":
         os.system("pkg update")
         os.system("pkg upgrade")

menu()
