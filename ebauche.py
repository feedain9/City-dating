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

"""Class pour la ville avec le nom, le taux de criminalité et le prix moyen des loyers"""
class City():
    def __init__(self, name=None, crimeRate=None, averageRentPricePerM2=None) -> None:
        self.name = name
        self.crimeRate = crimeRate
        self.averageRentPricePerM2 = averageRentPricePerM2

"""Class pour la quartier avec le nom, le taux de criminalité, le prix moyen des loyers et la ville"""
class District():
    def __init__(self, name=None, gpsPt=None, crimeRate=None, city=None, averageRentPricePerM2=None):
        self.name = name
        self.gpsPt = gpsPt
        self.crimeRate = crimeRate
        self.city = city
        self.averageRentPricePerM2 = averageRentPricePerM2

"""Class pour la requete client avec le adress, le loyer maximal, le prix moyen des loyers et la ville"""
class ClientRequest():
    def __init__(self, adress=None, desiredRentPriceMax=None, desiredSizeM2=None, timeToGoWork=None, retailPlace=None) -> None:
        self.adress = adress #lieu de travail 
        self.desiredRentPriceMax = desiredRentPriceMax #loyer maximum demandé
        self.desiredSizeM2 = desiredSizeM2 #Surface maximum demandé
        self.timeToGoWork = timeToGoWork #le temps de trajet en min du travail au logement potentiel
        self.retailPlace = retailPlace #proximité en km des commerces de proximité


"""Creation des objets quartiers de Lyon"""
c1 = District(name="St-Rambert", crimeRate=4.5, averageRentPricePerM2=15.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-9eme/saint-rambert/48358.htm
c2 = District(name="La Duchère", crimeRate=4.6, averageRentPricePerM2=15.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-9eme/la-duchere/48359.htm
c3 = District(name="Croix Rousse", crimeRate=5.5, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-4eme/croix-rousse-centre/48342.htm
c4 = District(name="Vaise", crimeRate=3.5, averageRentPricePerM2=15.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-9eme/vaise-rochecardon-industrie/48361.htm
c5 = District(name="Brotteaux", crimeRate=5.5, averageRentPricePerM2=18.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-6eme/les-brotteaux-bellecombe-massena/48347.htm
c6 = District(name="Les Pentes", crimeRate=4.5, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-4eme/plateau-de-la-croix-rousse-saone/48339.htm
c7 = District(name="Vieux Lyon", crimeRate=6.5, averageRentPricePerM2=18.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-5eme/vieux-lyon/48345.htm
c8 = District(name="Point-du-Jour", crimeRate=4.5, averageRentPricePerM2=15.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-5eme/point-du-jour-menival/48343.htm
c9 = District(name="St-Just", crimeRate=7.5, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-5eme/fourviere-saint-just/48346.htm
c10 = District(name="Bellecombe", crimeRate=5.4, averageRentPricePerM2=18.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-6eme/les-brotteaux-bellecombe-massena/48347.htm
c11 = District(name="Part-Dieu", crimeRate=5.2, averageRentPricePerM2=17.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-3eme/part-dieu/48338.htm
c12 = District(name="Villette", crimeRate=3.5, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-3eme/villette/48336.htm
c13 = District(name="Sans Souci", crimeRate=2.5, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-3eme/sans-souci-dauphine/48335.htm
c14 = District(name="Montchat", crimeRate=4.4, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-3eme/montchat/48334.htm
c15 = District(name="Monplaisir", crimeRate=6.2, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-8eme/monplaisir-le-bachut/48357.htm
c16 = District(name="Bachut", crimeRate=7.0, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-8eme/monplaisir-le-bachut/48357.htm
c17 = District(name="Mermoz", crimeRate=4.5, averageRentPricePerM2=15.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-8eme/laennec-mermoz/48355.htm
c18 = District(name="Etats-Unis", crimeRate=3.8, averageRentPricePerM2=15.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-8eme/etats-unis/48353.htm
c19 = District(name="Grand Trou", crimeRate=4.8, averageRentPricePerM2=15.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-8eme/le-grand-trou/48351.htm
c20 = District(name="Gerland", crimeRate=4.2, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-7eme/gerland/48348.htm
c21 = District(name="Guillotière", crimeRate=3.5, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-7eme/la-guillotiere-sud/48350.htm
c22 = District(name="Fourvière", crimeRate=5.7, averageRentPricePerM2=16.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-5eme/fourviere-saint-just/48346.htm
c23 = District(name="Confluence", crimeRate=5.1, averageRentPricePerM2=17.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-2eme/perrache-le-confluent/48331.htm
c24 = District(name="Perrache", crimeRate=4.9, averageRentPricePerM2=17.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-2eme/perrache-le-confluent/48331.htm
c25 = District(name="Bellecour", crimeRate=5.9, averageRentPricePerM2=20.0, city="Lyon") #https://www.seloger.com/prix-de-l-immo/location/rhone-alpes/rhone/lyon-2eme/place-bellecour/r69382_xxxx_8fb4c1.htm

user = ClientRequest(adress="10 rue sainte-Hélène 69002 Lyon", desiredRentPriceMax=600.0, desiredSizeM2=25.0, timeToGoWork=20, retailPlace=1.5)
#add district to list
districts = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25]
for district in districts:
    if district.name not in dict_point.keys():
        dict_point[district.name]=point_init

    """Récupération des points actuels selon le nom du quartier"""
    current_point = dict_point.get(district.name)

    """1.Comparaison du premier critère : la sécurité du quartier"""
    if district.crimeRate > crimeRateLyon:
        current_point -= coef_crimeRate
    elif district.crimeRate < crimeRateLyon:
        current_point += coef_crimeRate
        
    """1.Comparaison du premier critère idem : la cout du loyer"""
    cost_rent = district.averageRentPricePerM2 * user.desiredSizeM2
    if user.desiredRentPriceMax > cost_rent:
        current_point -= coef_rentPrice
    elif user.desiredRentPriceMax < cost_rent:
        current_point += coef_rentPrice
    print(f"Point actuel après premier critère : {current_point}")

    """2.Comparaison du deuxième critère : temps de trajet demandé pour aller au travail"""
    time_to_go = random.choice([10, 15, 40, 20])
    if user.timeToGoWork > time_to_go:
        current_point -= coef_retail
    elif user.timeToGoWork < time_to_go:
        current_point += coef_retail
    print(f"Point actuel après deuxième critère : {current_point}")
    

    """3.Comparaison du troisième critère : proximité avec les commerces"""
    proximity_to_retail = random.choice([1, 0.5, 0.7, 2.0])
    if user.retailPlace > proximity_to_retail:
        current_point -= coef_workplace
    elif user.retailPlace < proximity_to_retail:
        current_point += coef_workplace
        print(f"Point actuel après troisième critère : {current_point}")
    
    dict_point[district.name]=current_point

# Trie le dictionnaire par ordre décroissant des valeurs
sorted_dict = sorted(dict_point.items(), key=lambda x: x[1], reverse=True)

# Affiche les trois apparts selon le critère client
for i in range(3):
    key, value = sorted_dict[i]
    print(f"Le {i+1}er quartier recommandé est {key} avec un score de {value}")
print(sorted_dict)
