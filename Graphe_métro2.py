import networkx as nx
import matplotlib.pyplot as plt

metro = nx.Graph()

L9 ={"Pont_de_Sèvres_L9" : [97, 797],
     "Billancourt_L9" : [112, 780],
     "Marcel_Semblat_L9" : [130, 762],
     "Porte_de_Saint-Cloud_L9" : [147, 740],
     "Exelmans_L9" : [147, 715],
     "Michel-Ange–Molitor_L9" : [147, 687],
     "Michel-Ange–Auteuil_L9" : [147, 659],
     "Jasmin_L9" : [147, 617],
     "Ranelagh_L9" : [147, 576],
     "La_Muette_L9" : [147, 533],
     "Rue_de_la_Pompe_L9" : [156, 487],
     "Trocadéro_L9" : [200, 487],
     "Iéna_L9" : [244, 487],
     "Alma–Marceau_L9" : [291, 469],
     "Franklin_D_Roosevelt_L9" : [326, 433],
     "Saint-Philippe_du_Roule_L9" : [359, 400],
     "Miromesnil_L9" : [379, 380],
     "Saint-Augustin_L9" : [396, 363],
     "Havre–Caumartin_L9" : [435, 378],
     "Chaussée_d’Antin–La Fayette_L9" : [481, 379],
     "Richelieu–Drouot_L9" : [511, 379],
     "Grands_Boulevards_L9" : [550, 379],
     "Bonne-Nouvelle_L9" : [602, 379],
     "Strasbourg–Saint-Denis_L9" : [631, 379],
     "République_L9" : [700, 401],
     "Oberkampf_L9" : [721, 421],
     "Saint-Ambroise_L9" : [772, 472],
     "Voltaire_L9" : [792, 492],
     "Charonne_L9" : [811, 511],
     "Rue_des_Boulets_L9" : [829, 529],
     "Nation_L9" : [858, 558],
     "Buzenval_L9" : [886, 542],
     "Maraîchers_L9" : [901, 527],
     "Porte_de_Montreuil_L9" : [916, 512],
     "Robespierre_L9" : [931, 498],
     "Croix_de_Chavaux_L9" : [945, 483],
     "Mairie de Montreuil_L9" : [960, 469]
     }

def creation_ligne(G, ligne : dict):
    position = dict()
    for station, pos in ligne.items():
        G.add_node(station)
        position[station] = pos
    liste_stations = list(ligne.keys())
    station_0 = liste_stations[0]
    for i in range(1, len(liste_stations)):
        G.add_edge(station_0, liste_stations[i])
        station_0 = liste_stations[i]
    return position

P9 = creation_ligne(metro, L9)
#P3 = creation_ligne(metro, L3)
#P4 = creation_ligne(metro, L4)

plt.clf()
nx.draw(metro, with_labels=True)
plt.show()
