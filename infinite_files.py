#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:17:59 2024

@author: vboxuser
"""
i = 0
name = "openme001.txt"
while True:
    
    with open(rf"/home/vboxuser/Desktop/{name}", "w") as file:
        file.write("Computer hacked")
    
    num = int(name[6:9])
    num += 1
    name = f"openme{num:03d}.txt"

    i += 1
   
    
#così creo mille file ovvero 999 è l'ultimo +1
#per poterne creare di più devo incrementare num = int(name[6:9])
#mettendo numeri maggiori di 9 e anche aggiungere zeri a name = "openme001.txt"
#e devo anche mettere f"openme{num:03d}.txt" al posto di 3, 4...

#name = "openme0001.txt"
#number = int(name[6:10]) 
#name = f"openme{number:04d}.txt"

#posso invece cambiare continuamente il nume file mantenendo lo
#stesso numero di caratteri?

