def draw_rectangle (hauteur,largeur):

    x = '|' + '-' *(hauteur - 2) + '|\n';
    print (x + x.replace (*'- ') * (largeur - 2) + x)
 
draw_rectangle(10,3)