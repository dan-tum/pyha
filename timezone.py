# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:44:50 2015

@author: Daniel
"""

def numzones_per_country():
    import csv
    
    #reading Zone and writing to list
    with open('/Users/Daniel/Python/pyha/zone.csv', "r") as zoneFile:
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

    with open('/Users/Daniel/Python/pyha/zone.csv', "r") as zoneFile:
        zoneData = zoneFile.readlines()
    zoneList = list(csv.reader(zoneData))
    
    
    continentDict = {}
    continentList = []
    
    for i in range(0, len(zoneList)):
        
        if zoneList[i][2].split("/")[0] not in continentList:
            continentList.append(zoneList[i][2].split("/")[0])
        
    for i in range(0, len(continentList)):
        continentDict[continentList[i]] = 0
        
        for j in range(0, len(zoneList)):
            if continentList[i] == zoneList[j][2].split("/")[0]:
                continentDict[continentList[i]] += 1
           
    
    return continentDict



def zone_countries():
    import csv
    
    #opening of data
    with open("/Users/Daniel/Python/pyha/timezone.csv", "r") as timezoneFile:
            timezoneData = timezoneFile.readlines()
    timezoneList = list(csv.reader(timezoneData))
            
    with open('/Users/Daniel/Python/pyha/zone.csv', "r") as zoneFile:
        zoneData = zoneFile.readlines()
    zoneList = list(csv.reader(zoneData))
    
    #create abreviationList
    abreviationList = []
    timezoneDict = {}   
    
    for i in range(0, len(timezoneList)):
        
        if timezoneList[i][1] not in abreviationList:
            abreviationList.append(timezoneList[i][1])
        
    for i in range(0, len(abreviationList)):
        countryList = []
        for j in range (0, len(timezoneList)):
            
            if timezoneList[j][1] == abreviationList[i]:
                countryNumber = timezoneList[j][0]
                country = zoneList[int(countryNumber)-1][2].split("/")[1]
                if country not in countryList:
                    countryList.append(country)
                timezoneDict[abreviationList[i]] = countryList
                
    print(timezoneDict)
    return timezoneDict
    

    
#print numzones_per_country()
#print numzones_per_continent()
    
print(zone_countries())

