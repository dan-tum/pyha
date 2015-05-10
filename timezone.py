# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:44:50 2015

@author: Daniel
"""

def numzones_per_country():
    import csv
    
    #reading Zone and writing to list
    with open('/Users/Daniel/pyha/zone.csv', "r") as zoneFile:
        zoneData = zoneFile.readlines()
    zoneList = list(csv.reader(zoneData))
    
    #create empty dictionary
    countryDict = {}
    
    #iterating through lists
    for i in range(0, len(zoneList)):
        
        if zoneList[i][1] not in countryDict:
            countryDict[zoneList[i][1]] = 1
        elif zoneList[i][1] in countryDict:
            countryDict[zoneList[i][1]] += 1
    
    return countryDict
    

def numzones_per_continent():
    import csv

    with open('/Users/Daniel/pyha/zone.csv', "r") as zoneFile:
        zoneData = zoneFile.readlines()
    zoneList = list(csv.reader(zoneData))
    
    
    continentDict = {}
    continentList = []
    
    for i in range(0, len(zoneList)):
        
        if zoneList[i][2].split("/")[0] not in continentList:
            continentList.append(zoneList[i][2].split("/")[0])
            
        print"lololosfsadfl"
        
    
        
    
    
    return continentDict


    
    

    
print numzones_per_country()
