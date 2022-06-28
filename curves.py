import matplotlib.pyplot as plt 
import numpy as np
import csv
import pathlib
import os
import math


data_file_wallet = 3
data_file_negative = 1

def data_in_list(folder, file_to_read):
    f= open(folder + "/" + file_to_read, "r")
    lines = csv.reader(f)
    list_coord = list()
    for row in lines:
        list_row = list()
        for coord in row:
            if coord == '-':
                list_row.append('-')
            else:
                list_row.append(int(coord))
        list_coord.append(list_row)
    return list_coord


def data_in_curves(liste, title=None ):
    new_liste = []
    for i in liste:
        if len(i) == 2:
            new_liste.append(i)
    x = np.linspace(0, len(new_liste)/23.8, len(new_liste))
    liste_norm1 = []
    liste_norm2 = []    
    for i in (new_liste):
        liste_norm1.append(i[0])
        liste_norm2.append(i[1]/(200**2))
    y1 = liste_norm1
    y2 = liste_norm2
    plt.figure()
    plt.plot(x, y2, c="orange", label="gyroscope norm")
    plt.plot(x, y1, c="blue", label="accelerometer norm")
    plt.title(title)
    plt.xlabel("time")
    plt.ylabel("acceleration norm")
    plt.legend()
    plt.show()

def data_in_curves2(liste , title_file):
    nb_prises = 0
    idx = []
    for i in range(len(liste)): 
        if len(liste[i]) != 2:
            nb_prises += 1
            idx.append(i)
    idx.append(len(liste))
    plt.figure()
    for i in range(nb_prises):
        j = 0
        new_liste = []
        for j in range(idx[i]+1, idx[i+1]):
                new_liste.append(liste[j])
        x = np.linspace(0, len(new_liste), len(new_liste))
        liste_norm1 = []
        liste_norm2 = []    
        for k in (new_liste):
            liste_norm1.append(k[0])
            liste_norm2.append(k[1])
        y1 = liste_norm1
        y2 = liste_norm2
        x = np.linspace(0, len(new_liste)/23.8, len(new_liste))
        plt.subplot(2,1,1)
        plt.plot( x , y1 , label="test"+str(i+1))
        plt.xlabel("time")
        plt.ylabel("norm")
        plt.title("accelerometer norm")
        plt.subplot(2,1,2)
        plt.plot( x , y2 , label="test"+str(i+1))
        plt.xlabel("time")
        plt.ylabel("norm")
        plt.title("gyroscope norm")
        plt.legend()
    plt.savefig("output"+"/"+str(title_file))
    plt.show()
    

pathlib.Path("output").mkdir(parents=True, exist_ok=True)

for i in range(data_file_wallet):
    data_in_curves2(data_in_list("./data/wallet" ,f"custom_output_wallet_gyroscope_norm_test{i+1}.txt"), f"custom_output_wallet_norm_graph_{i+1}")

for i in range(data_file_negative):
    data_in_curves2(data_in_list("./data/negative" ,f"custom_output_negative_gyroscope_norm_{i+1}.txt"), f"custom_output_negative_norm_graph_{i+1}")




 