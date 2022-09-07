import requests
import csv

def replace(s,num):
    num=str(num);nueva="";palabra="eventId=";index=0
    for i in range(len(s)):
        if(index==len(palabra)): break
        if(palabra[index]==s[i]): index=index+1
        else: index=0
        nueva=nueva+s[i]

    nueva=nueva+num+"&sportId=66" #66->futbol

    return nueva

link_dorado='https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEventDetails?timezoneOffset=300&langId=4&skinName=doradobet&configId=12&culture=es-ES&countryCode=PE&deviceType=Desktop&numformat=en&integration=doradobet&eventId=6369991&sportId=66'
link_at='https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetEventDetails?timezoneOffset=300&langId=4&skinName=apuestatotal1&configId=1&culture=es-ES&countryCode=PE&deviceType=Desktop&numformat=en&integration=apuestatotal1&eventId=6369991&sportId=66'


beg=6369991

for i in range(8):
    
    dorado = requests.get(replace(link_dorado,beg))
    at = requests.get(replace(link_at,beg))

    dic_dorado=dorado.json()
    dic_at=at.json()


    nombre=dic_at['Result']['Name']

    temp_dorado=[]
    temp_at=[]
    
    for j in range(3):
        temp_dorado.append(dic_dorado['Result']['MarketGroups'][0]['Items'][0]['Items'][j]['Price'])
        temp_at.append(dic_at['Result']['MarketGroups'][0]['Items'][0]['Items'][j]['Price'])

    nombre_dorado=nombre+"_dorado.csv"
    nombre_at=nombre+"_at.csv"

    with open(nombre_dorado, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(temp_dorado)

    with open(nombre_at, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(temp_at)


    beg=beg+1
