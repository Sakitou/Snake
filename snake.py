import pygame
import random

# Initialisation de pygame
pygame.init()

# Définition des couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (213, 50, 80)
vert = (0, 255, 0)

# Configuration de l'affichage
largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Jeu du Serpent')

# Horloge
horloge = pygame.time.Clock()

# Paramètres du serpent
taille_bloc = 10
vitesse_serpent = 15

# Police
police = pygame.font.SysFont(None, 30)
police_score = pygame.font.SysFont(None, 25)

def message(msg, couleur):
    mesg = police.render(msg, True, couleur)
    fenetre.blit(mesg, [largeur / 6, hauteur / 3])

def jeu():
    game_over = False
    game_close = False

    x_serpent = largeur / 2
    y_serpent = hauteur / 2

    x_serpent_change = 0
    y_serpent_change = 0

    serpent_corps = []
    longueur_serpent = 1

    nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
    nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            fenetre.fill(noir)
            message("Vous avez perdu ! Appuyez sur Q pour quitter ou C pour rejouer.", rouge)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jeu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_close = True
                    game_over = True
                # Gestion des touches directionnelles
                if event.key == pygame.K_LEFT and x_serpent_change != taille_bloc:
                    x_serpent_change = -taille_bloc
                    y_serpent_change = 0
                elif event.key == pygame.K_RIGHT and x_serpent_change != -taille_bloc:
                    x_serpent_change = taille_bloc
                    y_serpent_change = 0
                elif event.key == pygame.K_UP and y_serpent_change != taille_bloc:
                    y_serpent_change = -taille_bloc
                    x_serpent_change = 0
                elif event.key == pygame.K_DOWN and y_serpent_change != -taille_bloc:
                    y_serpent_change = taille_bloc
                    x_serpent_change = 0

        if x_serpent >= largeur or x_serpent < 0 or y_serpent >= hauteur or y_serpent < 0:
            game_close = True

        x_serpent += x_serpent_change
        y_serpent += y_serpent_change
        fenetre.fill(noir)
        pygame.draw.rect(fenetre, vert, [nourriture_x, nourriture_y, taille_bloc, taille_bloc])

        tete_serpent = []
        tete_serpent.append(x_serpent)
        tete_serpent.append(y_serpent)
        serpent_corps.append(tete_serpent)

        if len(serpent_corps) > longueur_serpent:
            del serpent_corps[0]

        for x in serpent_corps[:-1]:
            if x == tete_serpent:
                game_close = True

        for x in serpent_corps:
            pygame.draw.rect(fenetre, blanc, [x[0], x[1], taille_bloc, taille_bloc])

        # Affichage du score
        score = police_score.render("Score: " + str(longueur_serpent - 1), True, blanc)
        fenetre.blit(score, [0, 0])

        pygame.display.update()

        if x_serpent == nourriture_x and y_serpent == nourriture_y:
            nourriture_x = round(random.randrange(0, largeur - taille_bloc) / 10.0) * 10.0
            nourriture_y = round(random.randrange(0, hauteur - taille_bloc) / 10.0) * 10.0
            longueur_serpent += 1

        horloge.tick(vitesse_serpent)

    pygame.quit()
    quit()

jeu()
