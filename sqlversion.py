import sqlite3
import random

"""Point et coefficient de pénalité/gain"""
point_init = 100.0 #point de départ
coef_crimeRate = 1.0 #point gagné/perdu lors du respect de la valeur du taux de criminalité
coef_rentPrice = 1.0 #point gagné/perdu lors du respect de la valeur du prix demandé par le client
coef_retail = 0.1 #point gagné/perdu lors du respect de la valeur de la proximité des commerces de proximité
coef_workplace = 0.1 #point gagné/perdu lors du respect de la valeur du temps de trajet du travail au logement potentiel

"""Valeur pour Lyon"""
crimeRateLyon = 4.3 #taux de criminalité moyen de Lyon

"""Définition des variables"""
dict_point = {} #dictionnaire des points
dict_appt = {
    "St-Rambert": {
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "La Duchère": {
        "ApptA":1.3,
        "ApptB":3.1,
        "ApptC":0.3,
        "ApptD":2.0,
        "ApptE":1.5,
    },
    "Croix Rousse": {
        "ApptA":1.1,
        "ApptB":3.0,
        "ApptC":0.9,
        "ApptD":2.9,
        "ApptE":1.4,
    },
    "Vaise": {
        "ApptA":1.0,
        "ApptB":3.0,
        "ApptC":0.7,
        "ApptD":2.0,
        "ApptE":1.5,
    },
    "Brotteaux": {
        "ApptA":2.2,
        "ApptB":4.2,
        "ApptC":6.8,
        "ApptD":8.2,
        "ApptE":10.9,
    },
    "Les Pentes": {
        "ApptA":0.2,
        "ApptB":2.2,
        "ApptC":4.8,
        "ApptD":6.2,
        "ApptE":8.9,
    },
    "Vieux Lyon": {
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":5.8,
        "ApptD":7.2,
        "ApptE":9.9,
    },
    "Point-du-Jour": {
        "ApptA":1.1,
        "ApptB":3.3,
        "ApptC":0.5,
        "ApptD":2.7,
        "ApptE":1.9,
    },
    "St-Just": {
        "ApptA":1.0,
        "ApptB":3.2,
        "ApptC":0.4,
        "ApptD":2.6,
        "ApptE":1.8,
    },
    "Bellecombe": {
        "ApptA":9.1,
        "ApptB":6.2,
        "ApptC":3.3,
        "ApptD":0.2,
        "ApptE":0.9,
    },
    "Part-Dieu":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Villette":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Sans Souci":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Montchat":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Monplaisir":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Bachut":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Mermoz":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Etats-Unis":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Grand Trou":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Gerland":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Guillotière":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Fourvière":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Confluence":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
    "Bellecour":{
        "ApptA":1.2,
        "ApptB":3.2,
        "ApptC":0.8,
        "ApptD":2.2,
        "ApptE":1.9,
    },
}

con = sqlite3.connect("cityDating.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS District(name, crimeRate, city, averageRentPricePerM2)")
cur.execute("CREATE TABLE IF NOT EXISTS ClientRequest(adress, desiredRentPriceMax, desiredSizeM2, timeToGoWork, retailPlace)")

con.commit()


# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("St-Rambert", 4.5, "Lyon", 15))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("La Duchère", 4.6, "Lyon", 15))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Croix Rousse", 5.5, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Vaise", 3.5, "Lyon", 15))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Brotteaux", 5.5, "Lyon", 18))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Les Pentes", 4.5, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Vieux Lyon", 6.5, "Lyon", 18))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Point-du-Jour", 4.5, "Lyon", 15))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("St-Just", 3.5, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Bellecombe", 6.4, "Lyon", 18))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Part-Dieu", 7.5, "Lyon", 17))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Villette", 6.7, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Sans Souci", 9.5, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Montchat", 1.5, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Monplaisir", 3.8, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Bachut", 8.6, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Mermoz", 1.8, "Lyon", 15))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Etats-Unis", 3.4, "Lyon", 15))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Grand Trou", 3.5, "Lyon", 15))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Gerland", 8.5, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Guillotière", 6.3, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Fourvière", 2.7, "Lyon", 16))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Confluence", 1.9, "Lyon", 17))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Perrache", 4.5, "Lyon", 17))
# cur.execute("INSERT INTO District VALUES(?,?,?,?)", ("Bellecour", 6.5, "Lyon", 20))
# con.commit()

# cur.execute("INSERT INTO ClientRequest VALUES(?,?,?,?,?)", ("10 rue sainte-Hélène 69002 Lyon", 600, 25, 20, 1.5))
# con.commit()

cur.execute("SELECT * FROM District")
districts = cur.fetchall()
print(f"Districts in Lyon: {districts}") 

cur.execute("SELECT * FROM ClientRequest")
user = cur.fetchone()
print(f"ClientRequest: {user}") 

for district in districts:
    #print(district[0])
    if district[0] not in dict_point.keys():
        dict_point[district[0]]=point_init
    current_point = dict_point.get(district[0])

    if district[1] > crimeRateLyon:
        diff = district[1] - crimeRateLyon
        diff = int(diff/0.1)
        current_point -= int(coef_crimeRate * diff)
        print(f"Le quartier {district[0]} a un taux de criminalité de {district[1]} et perd {int(coef_crimeRate * diff)} points")
    elif district[1] < crimeRateLyon:
        diff =  crimeRateLyon - district[1]
        diff = int(diff/0.1)
        current_point += int(coef_crimeRate * diff)
        print(f"Le quartier {district[0]} a un taux de criminalité de {district[1]} et gagne {int(coef_crimeRate * diff)} points")
    dict_point[district[0]]=current_point

print("1ère étape : la sécurité !")
sorted_dict = sorted(dict_point.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    key, value = sorted_dict[i]
    print(f"Le {i+1}er quartier recommandé est {key} avec un score de {value}")    
print("-------------------------------------------")

for district in districts:
    if district[0] not in dict_point.keys():
        dict_point[district[0]]=point_init

    """Récupération des points actuels selon le nom du quartier"""
    current_point = dict_point.get(district[0])
    """2.Comparaison du premier critère idem : la cout du loyer"""
    cost_rent = district[3] * user[2]
    if user[1] > cost_rent:
        diff =  user[1] - cost_rent
        diff = int(diff/50)
        current_point -= int(coef_rentPrice * diff)
        print(f"Le quartier {district[0]} a un loyer de {cost_rent} et perd {int(coef_rentPrice * diff)} points")
    elif user[1] < cost_rent:
        diff =  cost_rent - user[1]
        diff = int(diff/50)
        current_point += int(coef_rentPrice * diff)
        print(f"Le quartier {district[0]} a un loyer de {cost_rent} et gagne {int(coef_rentPrice * diff)} points")
    dict_point[district[0]]=current_point

print("2eme étape : le loyer demandé par le client !")
sorted_dict = sorted(dict_point.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    key, value = sorted_dict[i]
    if key:
        print(f"Le {i+1}er quartier recommandé est {key} avec un score de {value}")
print("-------------------------------------------")

for district in districts:
    if district[0] not in dict_point.keys():
        dict_point[district[0]]=point_init

    """Récupération des points actuels selon le nom du quartier"""
    current_point = dict_point.get(district[0])

    """3.Comparaison du deuxième critère : temps de trajet demandé pour aller au travail"""
    time_to_go = random.choice([10, 15, 40, 20, 25, 5, 9, 23, 39])
    if user[3] > time_to_go:
        diff = user[3] - time_to_go
        diff = int(diff/(0.5*time_to_go))
        current_point -= int(coef_retail * diff)
        print(f"Le quartier {district[0]} a un temps de trajet pour aller au travail de {time_to_go} et perd {int(coef_retail * diff)} points")
    elif user[3] < time_to_go:
        diff = time_to_go - user[3]
        diff = int(diff/(0.5*time_to_go))
        current_point += int(coef_retail * diff)
        print(f"Le quartier {district[0]} a un temps de trajet pour aller au travail de {time_to_go} et gagne {int(coef_retail * diff)} points")
    dict_point[district[0]]=current_point
    
print("3eme étape : le temps de trajet demandé !")
sorted_dict = sorted(dict_point.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    key, value = sorted_dict[i]
    if key:
        print(f"Le {i+1}er quartier recommandé est {key} avec un score de {value}")
print("-------------------------------------------")

"""4.Lister les appartements qui ont le plus de points à ce stade et les afficher"""
sorted_dict = sorted(dict_point.items(), key=lambda x: x[1], reverse=True)
#print(f"sorted_dict: {sorted_dict}")
best_district = []
#print("4eme étape : Lister les appartements qui ont le plus de points à ce stade !")
for i in range(3):
    key, value = sorted_dict[i]
    if key:
        best_district.append(key)
    #print(f"Le {i+1}er quartier recommandé est {key} avec un score de {value}")
#print("-------------------------------------------")


"""5.Comparaison du troisième critère : proximité avec les commerces"""
for districtr in best_district:
    #proximity_to_retail = random.choice([1, 0.5, 0.7, 2.0, 5.0, 3.4, 1.8, 2.8])
    appt = dict_appt.get(districtr) 
    print(f"appt: {appt}")
    current_point = dict_point.get(district[0])
    #print(f"appt: {appt}")
    if appt:
        for k,v in appt.items():
            proximity_to_retail = v
            #print(f"{proximity_to_retail}")
            if user[4] > proximity_to_retail:
                diff = user[4] - proximity_to_retail
                diff = int(diff/0.05)
                current_point -= int(coef_workplace * diff)
                print(f"Le quartier {district[0]} a une proximité avec les commerces de {proximity_to_retail} et perd {int(coef_workplace * diff)} points")
            elif user[4] < proximity_to_retail:
                diff = proximity_to_retail-user[4]
                diff = int(diff/0.05)
                current_point += int(coef_workplace * diff)
                print(f"Le quartier {district[0]} a une proximité avec les commerces de {proximity_to_retail} et gagne {int(coef_workplace * diff)} points")
            #print(f"result: {current_point}")
    dict_point[district[0]]=current_point

# Trie le dictionnaire par ordre décroissant des valeurs
sorted_dict = sorted(dict_point.items(), key=lambda x: x[1], reverse=True)

# Affiche les trois apparts selon le critère client
print("4eme étape : Résultat final !")
for i in range(3):
    key, value = sorted_dict[i]
    print(f"Le {i+1}er quartier recommandé est {key} avec un score de {value}")
print("-------------------------------------------")