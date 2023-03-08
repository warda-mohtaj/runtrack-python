def fruileg (type, saison):

    if type == "fruits" and saison == "hiver":
        print("Il y a orange, mandarine et kiwi")

    if type == "fruits" and saison == "été":
        print("Il y a poire, fraise, cassis")

    if type == "legumes" and saison == "hiver":
        print("Il y a carotte, topinambour, endive")
    
    if type == "legumes" and saison == "été":
        print("Il y a artichaut, aubergine,navet")

fruileg ("fruits", "hiver")
fruileg ("fruits", "été")
fruileg ("legumes", "hiver")
fruileg ("legumes", "été")