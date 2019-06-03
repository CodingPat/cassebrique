import pgzrun

WIDTH = 480 #largeur écran
HEIGHT = 640 #hauteur écran

def reset():
    # on positionne la batte au centre de l'écran et 20 pixels au-dessus du bas d'écran
    batte.center=(WIDTH/2, HEIGHT-20)
    # batte immobile au départ
    vx=0 # vitesse abcisse (x)
    vy=0 # vitesse ordonnée (y)
    batte.vitesse=(vx,vy)
  

def draw():
    #on efface l'écran
    screen.clear()
    #on dessine la batte
    batte.draw()

def update():
    #récupérer les coordonnnées de la batte
    x,y=batte.center
    #récupérer les vitesses en abcisse (x) et en ordonnée (y)
    vx,vy=batte.vitesse
    #mise à jour des coordonnées
    x+=vx
    y+=vy
    batte.center=x,y
    
    #vérifier que la batte ne sort pas de l'écran
    #vérifier à gauche
    if batte.left<0:
        batte.left=0
    #vérifier à droite
    elif batte.right>WIDTH:
        batte.right=WIDTH
        

def on_key_down(key):
    #si on appuye sur la flèche gauche, la coordonnée x doit décroître
    if key==keys.LEFT:
        batte.vitesse=(-5,0)
    #si on appuye sur la flèche droite, la coordonnée x doit croître
    elif key==keys.RIGHT:
        batte.vitesse=(5,0)

def on_key_up(key):
    #si on relâche les touches, la batte ne bouge plus
    batte.vitesse=(0,0)
    
#créer batte
batte = Actor('batte')

# Réinitialiser au départ
reset()


pgzrun.go()
