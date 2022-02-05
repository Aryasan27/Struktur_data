
from itertools import count
import random
import numpy as np
import pandas as pd
import time
import os

#fungsi fungsi dari 3 metode

#metode sorting data dengan bublesort
def bublesort(data):
  for i in range(len(data)-1,0,-1):#untuk menentukan terlebih dahulu panjang array yang akan menjadi patokan sorting
    for j in range(0,len(data)-1):#melakukan langkah satu persatu dengan memanipulasi index
      if (data[j] > data[j+1]):#melakukan langkah satu persatu dengan memanipulasi index dan perbandingan
        data[j],data[j+1]=data[j+1],data[j]#hasil tanpa menampilkan satu persatu langkah atau menu utama
    #print(data)

def bublesort_test(dataku):
  langkah=0#fungsi dari metode bublesort hanya ditambahkan langkah per masing masing sorting
  for i in range(len(dataku)-1,0,-1):
    print('langkah ke --',langkah)
    for j in range(0,len(dataku)-1):
      if (dataku[j]>dataku[j+1]):
        dataku[j],dataku[j+1]=dataku[j+1],dataku[j]

    langkah+=1
    print(dataku)#hasil yang menampilkan sortingan per masing masing langkah

#metode sorting data dengan selection sort

def selectionSort(dataku3):
  for i in range(len(dataku3)-1,0,-1):#untuk memnentukan panjang array yang akan menjadi patokan dalam sorting
    m=0
    for j in range(1,i+1):
      if dataku3[j]>dataku3[m]:#membuat titik ukur dengan variable m dan o
        m=j
    temp=dataku3[i]
    dataku3[i]=dataku3[m]
    dataku3[m]=temp#hasil akan di tampilkan tanpa menampilkan langkah langkah yang akan di sorting
    #print(dataku3) 

def selectionSort_test(T_sel_sort):
  langkah=0
  for i in range(len(T_sel_sort)-1,0,-1): #fungsi selection sort yang sama namun akan menampilkan hasil langkah 1 per satu 
    print('langkah ke--',langkah)
    m=0
    for j in range(1,i+1):
      if T_sel_sort[j]>T_sel_sort[m]:
        m=j
    temp=T_sel_sort[i]
    T_sel_sort[i]=T_sel_sort[m]
    T_sel_sort[m]=temp

    langkah+=1
    print(T_sel_sort)
#metode sorting dengan insertion sort

def insertionSort_test(data):
    langkah=0
    for i in range(1,len(data)):
        print('langkah ke--',langkah)
        key=data[i]
        j=i-1#fungsi yang sama dengan dua metode yang di atas namun sebagai testing atau akan menampilkan satu persatu langkah yang akan di jalankan
        while j>=0 and key<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key
        langkah+=1
        print(data)

def insertionSort(data):
    for i in range(1,len(data)):
        key=data[i]
        j=i-1
        while j>=0 and key<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key
        #print(data)



opt='y'
while (opt == 'y'):#melakukan perulangan yang diisi dengan percabangan agar menu yang di pilih kembali ke menu utama
  #menu utama
  print("PROGRAM 'SORT DATA 3 METODE")
  print("Pilih program yang akan di pilih")
  print("1.Tampilkan 1000 data")
  print("2.proses sorting bublesort")
  print("3.proses sorting selection sort")
  print("4.Proses sorting insertion sort")
  print("5.Tampilkan hasil sorting")
  print("6.Tampilkan waktu sorting")
  print("7.Keluar dari program")
  opt1=int(input('Pilih program yang akan di pilih(1/2/3..dst):'))#variable opt dalah untuk menentukan inputan kemana menu yang akan di pilih
  print('-------------------------------------------------------------')

  #OUTPUT
  if(opt1==1):#menu 1
    #membuat data random 1000 data untuk semua metode sort
    database_1000=list(range(0,1000))
    random.shuffle(database_1000)
    print(database_1000)

    #melakukan penyalinan data untuk ke 3 sort agar data tidak random kembali
    data_1000=database_1000.copy()
    data_1000_sel_sort=database_1000.copy()
    data_1000_ins_sort=database_1000.copy()
  elif(opt1==2):
    #penghitungan waktu pil 2
    start_time=time.time()
    bublesort(data_1000)
    waktu=time.time()-start_time
    #sorting test buble sort
    data_test=list(range(0,10))
    random.shuffle(data_test)
    print("DATA SEBELUM DI SORT")
    print(data_test)
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    bublesort_test(data_test)
    print("PROSES SORT")
    print(data_test)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("SORTING 1000 Data(buble Sort)")
    print(data_1000)
    
  elif(opt1==3):
    data_test3=list(range(0,10))
    random.shuffle(data_test3)
    print("DATA SEBELUM DI SORT")
    print(data_test3)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    selectionSort_test(data_test3)
    print("PROSES SORT DATA DENGAN SELECTION SORT")
    print(data_test3)
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    #penghitungan waktu selection sort
    start_time3=time.time()
    selectionSort(data_1000_sel_sort)
    print('SORTING 1000 DATA(Selection sort)')
    print(data_1000_sel_sort)
    waktu3=time.time()-start_time3
  elif(opt1==4):
    data_test4=list(range(0,10))
    random.shuffle(data_test4)
    print('Data Sebelum di sort')
    print(data_test4)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    insertionSort_test(data_test4)
    print('PROSES SORT DENGAN INSERTION SORT')
    print(data_test4)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    start_time4=time.time()
    insertionSort(data_1000_ins_sort)
    print('SORTING DATA (INSERTION SORT)')
    print(data_1000_ins_sort)
    waktu4=time.time()-start_time4

  elif(opt1==5):
    print("Data sebelum di sort")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    print(database_1000)
    print("Data hasil bublesort 1000 data")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    print(data_1000)
    print("Data hasil selection sort 1000 data")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    print(data_1000_sel_sort)
    print("Data hasil insertion sort 1000 data")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    print(data_1000_ins_sort)
    
  elif(opt1==6):
    Time={'Perolehan waktu':[waktu,waktu3,waktu4],# kesimpulan perolehan waktu
            '   Dalam Satuan':['detik','detik','detik']
          }
    df=pd.DataFrame(Time,index=['Bubble sort','selection sort','insertion sort'])
    print(df)
  else:
    print("end program [n],,,,,           \press/            ,,,,,back to frogram [y]")
  opt=input("back press y/:")
  os.system('cls')
print('thanks')