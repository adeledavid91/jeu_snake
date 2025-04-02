from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint

window: int = 0  # n° de fenêtre GLUT
width: int = 500
height: int = 500  # taille de fenêtre
field_width: int = 50
field_height: int = 50  # résolution

snake = [(20, 20)]  # liste des positions (x, y) du serpent
snake_dir: tuple[int, int] = (1, 0)  # direction du mouvement du serpent

interval: int = 200  # intervalle de mise à jour en millisecondes
food: list = []  # list de type (x, y)


def refresh2d_custom(width, height, internal_width, internal_height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, internal_width, 0.0, internal_height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)  # dessine un rectangle
    glVertex2f(x, y)  # coin bas gauche
    glVertex2f(x + width, y)  # coin bas droit
    glVertex2f(x + width, y + height)  # coin haut droit
    glVertex2f(x, y + height)  # coin haut gauche
    glEnd()  # fin du rectangle


def draw_snake():
    glColor3f(1.0, 1.0, 1.0)  # définition de la couleur en blanc
    for x, y in snake:  # passe par chaque entrée (x, y)
        draw_rect(x, y, 1, 1)  # dessine en (x, y) avec largeur = 1 et hauteur = 1


def update(value):  # move snake
    snake.insert(0, vec_add(snake[0], snake_dir))  # insère une nouvelle position au début de la liste du serpent
    snake.pop()  # supprime le dernier élément de la liste
    # spawn food
    r = randint(0, 20)  # regénère de la nourriture avec une chance de 5%
    if r == 0:
        x, y = randint(0, field_width), randint(0, field_height)  # position de la nouriture aléaroire
        food.append((x, y))
    glutTimerFunc(interval, update, 0)  # déclenche la mise à jour


def vec_add(position, direction):  # ((x1, y1), (x2, y2)):
    return position[0] + direction[0], position[1] + direction[1]


def keyboard(*args):
    global snake_dir  # important pour en indiquer la valeur
    if args[0] == 'z':
        snake_dir = (0, 1)  # vert le haut
    if args[0] == 's':
        snake_dir = (0, -1)  # vert le bas
    if args[0] == 'q':
        snake_dir = (-1, 0)  # vert la gauche
    if args[0] == 'd':
        snake_dir = (1, 0)  # vert la droite


def draw_food():
    glColor3f(0.5, 0.5, 1.0)  # sélectionne la couleur bleue
    for x, y in food:  #passe en revue les coordonnées x et y de la liste
        draw_rect(x, y, 1, 1)  # dessine la nouriture à la position (x, y) avec largeur=1 et hauteur=1


def draw():  # définition de la fonction draw
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # efface l'écran
    glLoadIdentity()  # remise à zéro de la position
    refresh2d_custom(width, height, field_width, field_height)
    draw_food()  # dessine la nouriture
    draw_snake()  # dessine le serpent
    glutSwapBuffers()  # double tampon
    # le serpent mange la nourriture
    (hx, hy) = snake[0]  # mémorise la position x et y de la tête du serpent
    for x, y in food:  # passe en revuela liste de la nourriture
        if hx == x and hy == y:  #est-ce que la position de la tête correspond à celle de la nourriture ?
            snake.append((x, y))  # allonge le serpent
            food.remove((x, y))  # efface la nourriture de l'écran
    # Initialisation
    glutInit()  # initialise glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)  # fixe la taille de la fenêtre
    glutInitWindowPosition(0, 0)  # initialise la fenêtre
    window = glutCreateWindow("Jeu de Snake")  # crée une fenêtre avec titre
    glutDisplayFunc(draw)  # callback de la fonction draw
    glutIdleFunc(draw)  # execution de la fonction draw
    glutTimerFunc(interval, update, 0)  # mise à jour
    glutKeyboardFunc(keyboard)  # indique à opengl que nous vérifions le clavier
    glutMainLoop()  # démarrage de la routine principale


if __name__ == "__main__":
    draw()
