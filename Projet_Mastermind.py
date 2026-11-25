import sys, pygame, random, time

LAUNCHED = True
RUNNING = True
COLOUR = "pictures/empty.png"
LINE = 0
LINE_1 = 4
TRY_NUMBERS = 0
SOUND=True

## Fonction principale

def Mastermind():
    ''' Cette fonction est appelée à l'exécution du programme, et permet d'afficher l'interface graphique du jeu Mastermind.
    Le Mastermind est un jeu de logique dans lequel le joueur doit essayer de trouver les quatre couleurs d'une combinaison secrète déterminée aléatoirement à chaque partie par le programme.
    Les couleurs pouvant être sélectionnées sont le rouge, le orange, le jaune, le vert, le bleu et le violet, et chaque couleur peut être présente jusqu'à deux fois dans la combinaison.

    Lorsque la fonction s'exécute, un interface avec deux boutons s'affiche : il faut appuyer sur "start" pour jouer ou sur "quit" pour quitter le jeu. Si l'on clique sur "start",
    une page contenant les règles du jeu apparaît à l'écran. Il faut alors cliquer sur la flèche pour passer les règles : la fenêtre principale du jeu apparaît alors.

     Elle contient :
    - à gauche de l'écran six boutons correspondant aux six couleurs présentes dans le jeu ainsi qu'un bouton "poubelle"
    - au centre de l'écran une grille (vide au départ) ainsi qu'un tableau à deux colonnes, qui servira à afficher les indices
    - à droite de l'écran différents boutons (alors que le bouton "ok" est indispensable, les autres permettent d'améliorer l'expérience de jeu ; se référer aux règles pour plus d'informations)

    Pour jouer, il faut appuyer sur une couleur, puis sur un emplacement de la grille. Il n'est possible de remplir que la ligne située au plus bas.
    Vous pouvez aussi effacer vos couleurs en cliquant sur un emplacement que vous avez rempli soit en cliquant sur le bouton "poubelle" ou soit en sélectionnant une nouvelle couleur et ensuite remplacer l'ancienne.
    Lorsque qu'une ligne est entièrement remplie, vous pouvez cliquer sur le bouton "ok" afin que l'ordinateur vérifie votre combinaison.
    En fonction du nombre de couleurs justes et d"emplacements corrects, le programme remplira au fur et à mesure le tableau, pour vous aider à trouver la bonne combinaison.

    Si vous trouvez la bonne combinaison, vous gagnez, et une page s'affiche alors, vous donnant la possibilité de rejouer ou de quitter la partie et vous indique le nombre d'essais dont vous avez eu besoin.
    Cependant, si vous ne trouvez pas la combinaison au bout des dix essais, vous avez perdu : une page s'affiche et indique la combinaison qui était à trouver, et vous propose de rejouer ou de quitter.'''

    # Initialisation du module Pygame
    pygame.init()

    while LAUNCHED :
        screen = init_screen()
        start_menu(screen)

## Les classes

# Permet de pouvoir créer des boutons et de pouvoir intéragir avec
class Button():
    # Construction du bouton
    def __init__(self, x, y, image) :
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, screen):
        # Permet de gérer les évènements de la souris
        action = False

        # Récupérer la position de la souris
        position = pygame.mouse.get_pos()

        # Vérifier la position du curseur par rapport à celle du bouton
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0 :
            self.clicked = False

        # Affichage des boutons
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return (action)

# Permet de pouvoir afficher du texte
class Text():
    # Création du texte
    def __init__(self, text, size, x, y, r, g, b):
        self.text = text
        self.size = size
        font_name = "font/arial.TTF"
        font_colour = r, g, b
        font = pygame.font.Font(font_name, self.size)
        self.text = font.render(self.text, True, font_colour)
        self.text_rect = self.text.get_rect()
        self.text_rect.midleft = (x, y)

    def draw_text(self, screen):
        # Affichage du texte
        screen.blit(self.text, (self.text_rect.x, self.text_rect.y))

## Fonctions vitales (indispensables)

# Création de la fenêtre
def init_screen():
    size = 1080, 720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mastermind")
    logo = pygame.image.load("pictures/logo.png").convert_alpha()
    pygame.display.set_icon(logo)
    return(screen)

# Permet de choisir l'image qui deviendra un bouton ainsi que sa taille
def button(chemin):
    button_image = pygame.image.load(chemin)
    button_image.convert_alpha()
    button_image = pygame.transform.scale(button_image, (200, 100))
    return(button_image)

# Idem, mais avec une taille différente
def square_button(chemin):
    button_image = pygame.image.load(chemin)
    button_image.convert_alpha()
    button_image = pygame.transform.scale(button_image, (80, 80))
    return(button_image)

# Idem, mais avec une taille différente
def circle_button(chemin):
    button_image = pygame.image.load(chemin)
    button_image.convert_alpha()
    button_image = pygame.transform.scale(button_image, (60, 60))
    return(button_image)

# Idem, mais avec une taille différente
def size_grid_button(chemin):
    button_image = pygame.image.load(chemin)
    button_image.convert_alpha()
    button_image = pygame.transform.scale(button_image, (37, 37))
    return(button_image)

# Idem, mais avec une taille différente
def mini_button(chemin):
    button_image = pygame.image.load(chemin)
    button_image.convert_alpha()
    button_image = pygame.transform.scale(button_image, (50, 30))
    return(button_image)

# Idem, mais avec une taille différente
def sound_button(chemin):
    button_image = pygame.image.load(chemin)
    button_image.convert_alpha()
    button_image = pygame.transform.scale(button_image, (60, 60))
    return(button_image)

# Idem, mais avec une taille différente
def hour_button(chemin):
    button_image = pygame.image.load(chemin)
    button_image.convert_alpha()
    button_image = pygame.transform.scale(button_image, (170, 170))
    return(button_image)


# Permet d'afficher le menu principal, celui du jeu
def game_menu(screen, start_time):
    global LAUNCHED
    global COLOUR
    global LINE
    LINE = 0
    global LINE_1
    LINE_1 = 4
    global TRY_NUMBERS
    TRY_NUMBERS = 0
    global RUNNING
    global SOUND

    background = 236, 222, 208

    # Création des combinaisons de l'utilisateur et de de l'ordinateur
    user_combination = ["pictures/empty2.png" for i in range(4)]
    computer_combination = choice_combination()

    # Création de la grille, du tableau et du texte
    grid = pygame.image.load("pictures/grid.png").convert_alpha()
    grid = pygame.transform.scale(grid, (250, 600))
    sep = pygame.image.load("pictures/separation.png").convert_alpha()
    couleurs = Text("couleurs", 20, 580, 40, 0, 0, 0)
    bien_placées = Text("bien placées", 20, 580, 60, 0, 0, 0)
    couleurs_correctes = Text("couleurs correctes", 20, 710, 40, 225, 83, 83)
    mais_mal_placées = Text("mais mal placées", 20, 710, 60, 225, 83, 83)
    available_colours = Text("Couleurs disponibles :", 25, 25, 60, 114, 72, 30)
    error_l1 = Text("Vous n'avez pas", 20, 880, 560, 225, 83, 83)
    error_l2 = Text("rempli toute la ligne !", 20, 880, 590, 225, 83, 83)

    error = False

    # Création des boutons
    red_button = Button(150, 135, circle_button("pictures/red.png"))
    orange_button = Button(150, 225, circle_button("pictures/orange.png"))
    yellow_button = Button(150, 315, circle_button("pictures/yellow.png"))
    green_button = Button(150, 405, circle_button("pictures/green.png"))
    blue_button = Button(150, 495, circle_button("pictures/blue.png"))
    purple_button = Button(150, 580, circle_button("pictures/purple.png"))

    # Création des images qui apparaîtront lorsqu'une couleur est sélectionnée
    red_selected = Button(150, 135, circle_button("pictures/selected.png"))
    orange_selected = Button(150, 225, circle_button("pictures/selected.png"))
    yellow_selected = Button(150, 315, circle_button("pictures/selected.png"))
    green_selected = Button(150, 405, circle_button("pictures/selected.png"))
    blue_selected = Button(150, 495, circle_button("pictures/selected.png"))
    purple_selected = Button(150, 580, circle_button("pictures/selected.png"))
    erase_selected = Button(150, 670, square_button("pictures/square_selected.png"))

    # Création des boutons vides
    empty_buttons = []

    y = 606
    for i in range(10):
        x = 347
        for j in range(4):
            locals()['button_line%s_%s' % (i, j)] = Button(x, y, size_grid_button("pictures/empty.png"))
            empty_buttons.append(locals()['button_line%s_%s' % (i, j)])
            x += 50
        y -= 56

    # Création des boutons utilitaires
    ok_button = Button(960, 650, square_button("pictures/ok.png"))
    erase_button = Button(150, 670, square_button("pictures/erase.png"))
    button_quit_game = Button(960, 55, square_button("pictures/cancel.png"))
    button_rules = Button(960, 150, square_button("pictures/button_rules.png"))
    
    button_sound = Button(960, 240, square_button("pictures/sound.png"))
    sound_activated = Button(960, 240, sound_button("pictures/soundActivate.png"))
    sound_desactivated = Button(960, 240, sound_button("pictures/soundDesactivate.png"))
    
    button_hour = Button(976, 430, hour_button("pictures/clock.png"))
    
  

    indications = []
    correct_locations = 0

    while LAUNCHED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LAUNCHED = False
                sys.exit()
        screen.fill(background)


        #affichage et gestion du son
        if button_sound.draw(screen):
            if SOUND==False :
                SOUND=True
            else :
                SOUND=False

        if SOUND==False:
            pygame.mixer.music.pause()
            sound_desactivated.draw(screen)
        
        if SOUND==True:
            pygame.mixer.music.unpause()
            sound_activated.draw(screen)

        #chrononomètre :
        button_hour.draw(screen)

        current_time=time.time()
        chronometer = int(current_time - start_time)
        number_1 = int(chronometer/600)
        number_2 = int((chronometer-(number_1*600))/60)
        number_3 = int((chronometer-(number_1*600)-(number_2*60))/10)
        number_4 = int(chronometer-(number_1*600)-(number_2*60)-(number_3*10))  #on détermine quel chiffre correspond à chaque emplacement

        if number_1==6 :
            if number_2==0 :
                if number_3==0 :
                    if number_4==0 :
                        lost(computer_combination, screen, number_1, number_2, number_3, number_4)   #au bout de 59 min et 59 secs le joueur a perdu


        
        if correct_locations == 4:  #dans le cas où le joueur gagne
            time.sleep(1)
            win(screen, number_1, number_2, number_3, number_4)
        if LINE > 36:     #dans le cas où le joueur perd
            time.sleep(1)
            lost(computer_combination, screen, number_1, number_2, number_3, number_4)


        number_1 = Text(str(number_1), 40, 930, 437, 246, 143, 88)
        number_2 = Text(str(number_2), 40, 950, 437, 246, 143, 88)
        colon = Text(":", 40, 970, 435, 246, 143, 88)
        number_3 = Text(str(number_3), 40, 980, 437, 246, 143, 88)
        number_4 = Text(str(number_4), 40, 1000, 437, 246, 143, 88)   #on crée indépendant chacun des chiffres du chrono

        #on affiche tous les chiffres
        number_1.draw_text(screen)
        number_2.draw_text(screen)
        colon.draw_text(screen)
        number_3.draw_text(screen)
        number_4.draw_text(screen)

        # Affichage de la grille, du tableau et du texte
        pygame.Surface.blit(screen, grid, (300, 55))
        pygame.Surface.blit(screen, sep, (580, 35))
        couleurs.draw_text(screen)
        bien_placées.draw_text(screen)
        couleurs_correctes.draw_text(screen)
        mais_mal_placées.draw_text(screen)
        available_colours.draw_text(screen)

        # Affichage des boutons
        if button_rules.draw(screen):
            show_rules(screen)

        if red_button.draw(screen):
            COLOUR = "pictures/red.png"
        if orange_button.draw(screen):
            COLOUR = "pictures/orange.png"
        if yellow_button.draw(screen):
            COLOUR = "pictures/yellow.png"
        if green_button.draw(screen):
            COLOUR = "pictures/green.png"
        if blue_button.draw(screen):
            COLOUR = "pictures/blue.png"
        if purple_button.draw(screen):
            COLOUR = "pictures/purple.png"
        if erase_button.draw(screen):
            COLOUR = "pictures/empty2.png"

        if COLOUR == "pictures/red.png":
            red_selected.draw(screen)
        if COLOUR == "pictures/orange.png":
            orange_selected.draw(screen)
        if COLOUR == "pictures/yellow.png":
            yellow_selected.draw(screen)
        if COLOUR == "pictures/green.png":
            green_selected.draw(screen)
        if COLOUR == "pictures/blue.png":
            blue_selected.draw(screen)
        if COLOUR == "pictures/purple.png":
            purple_selected.draw(screen)
        if COLOUR == "pictures/empty2.png":
            erase_selected.draw(screen)

        for i in range(LINE, LINE_1):
            number = LINE_1 - i - 1
            if empty_buttons[i].draw(screen):
                empty_buttons[i].image = size_grid_button(COLOUR)
                user_combination[number] = COLOUR

        if ok_button.draw(screen):
            if "pictures/empty2.png" in user_combination:
                error = True
            else:
                # if SOUND:
                    # pygame.mixer.music.pause()
                    # ok = pygame.mixer.Sound('sounds/idea.wav')
                    # ok.play()
                    # import time
                    # time.sleep(1)
                    # pygame.mixer.music.unpause() ça fait crash python
                    # pygame.mixer.music.load('sounds/idea.mp3')
                    # pygame.mixer.music.play()
                    # import time
                    # time.sleep(0.5)
                    # pygame.mixer.music.load('sounds/musique.mp3')
                    # pygame.mixer.music.play(-1)   là ca rend pas bienn car ca arrete la musique pour la recommencer ensuite depuis le début bref c'est nul
                error = False
                for element in user_combination:
                    user_combination = ["red" if x == "pictures/red.png" else x for x in user_combination]
                    user_combination = ["orange" if x == "pictures/orange.png" else x for x in user_combination]
                    user_combination = ["yellow" if x == "pictures/yellow.png" else x for x in user_combination]
                    user_combination = ["green" if x == "pictures/green.png" else x for x in user_combination]
                    user_combination = ["blue" if x == "pictures/blue.png" else x for x in user_combination]
                    user_combination = ["purple" if x == "pictures/purple.png" else x for x in user_combination]
                results = comparison_combinations(computer_combination, user_combination, screen)
                correct_locations = results[1]
                indications_comparison = results[0]
                indications.append(indications_comparison)
                user_combination = ["pictures/empty2.png" for i in range(4)]

        for i in range(len(indications)):
             for j in range(len(indications[i])):
                 indications[i][j].draw_text(screen)

        if error == True :
            error_l1.draw_text(screen)
            error_l2.draw_text(screen)

        if button_quit_game.draw(screen):
            COLOUR = "pictures/empty.png"
            confirmation_quit_game(screen)
            RUNNING = True

        for i in empty_buttons :
            i.draw(screen)

        pygame.display.flip()

# Permet de créer aléatoirement le code que l'utilisateur devra trouver
def choice_combination():
    colours = ["blue", "green", "red", "orange", "yellow", "purple"]*2
    random.shuffle(colours)
    computer_combination = random.sample(colours, 4)
    return(computer_combination)

# Compare la combinaison de couleurs de l'ordinateur à celle de l'utilisateur
# Et affiche le nombre de couleurs et d'emplacements corrects
def comparison_combinations(computer_combination, user_combination, screen):
    global LINE
    global LINE_1
    global TRY_NUMBERS

    user_combination = user_combination[::-1]

    correct_locations = 0
    right_colours = 0

    number = len(user_combination)
    for i in range(number):
        if computer_combination[i] == user_combination[i]:
            correct_locations += 1

    user_combination_modify = user_combination # Liste des couleurs que le joueur a choisi mais chaque couleur n'est présente qu'au maximum deux fois
    for element in user_combination_modify:
        while user_combination_modify.count(element) > 2:
            user_combination_modify.remove(element)

    for i in computer_combination:
        if computer_combination.count(i) == 2: # Gère si la couleur correspondant à l'élément i est présente deux fois dans la combinaison de l'ordinateur
            if i in user_combination:
                if user_combination_modify.count(i) == 1: # Si cette couleur est présente une fois dans la combinaison du joueur, il y a donc une bonne couleur dans la combinaison du joueur
                    right_colours += 1
                    user_combination = ["none" if x == i else x for x in user_combination] # On "supprime" les couleurs en double dans la combinaison du programme en les remplaçant par "none"
                elif user_combination_modify.count(i) == 2:  # Si cette couleur est présente une fois dans la combinaison du joueur, il y a donc deux bonnes couleurs dans la combinaison du joueur
                    right_colours += 2
                    user_combination = ["none" if x == i else x for x in user_combination] # On "supprime" les couleurs en double de la combinaison du programme en les remplaçant par "none"

    for i in computer_combination: # Vérifie si l'utilisateur a mis les mêmes couleurs que celle que le programme a choisi en un seul exemplaire
        if i in user_combination:
            right_colours += 1


    misplaced_colours = right_colours - correct_locations


    misplaced_colours_show_text = str(misplaced_colours)
    correct_locations_show_text = str(correct_locations)

    indications = []

    if LINE == 0:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 610, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 610, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 4:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 551, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 551, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 8:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 496, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 496, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 12:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 438, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 438, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 16:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 383, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 383, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 20:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 326, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 326, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 24:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 269, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 269, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 28:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 214, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 214, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 32:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 158, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 158, 225, 83, 83)
        indications.append(misplaced_colours_show)

    if LINE == 36:
        correct_locations_show = Text(correct_locations_show_text, 30, 629, 108, 0, 0, 0)
        indications.append(correct_locations_show)
        misplaced_colours_show = Text(misplaced_colours_show_text, 30, 773, 108, 225, 83, 83)
        indications.append(misplaced_colours_show)

    # Désactiver la ligne validée et activer la lige suivante
    LINE += 4
    LINE_1 += 4

    TRY_NUMBERS += 1

    results = [indications, correct_locations, misplaced_colours]

    return(results)

# Premier menu du jeu
def start_menu(screen):
    global LAUNCHED
    global SOUND

    background = 236, 222, 208
    mastermind_title = Text("Mastermind", 80, 345, 250, 114, 72, 30)
    button_start = Button(540, 370, button("pictures/button_start.png"))
    button_quit = Button(540, 450, button("pictures/button_quit.png"))
    button_sound = Button(1020, 60, square_button("pictures/sound.png"))

    sound_activated = Button(1020, 60, sound_button("pictures/soundActivate.png"))
    sound_desactivated = Button(1020, 60, sound_button("pictures/soundDesactivate.png"))

    # if SOUND : par défaut le son est activé
    pygame.mixer.music.load('sounds/musique.mp3')
    pygame.mixer.music.play(-1)

   

    while LAUNCHED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LAUNCHED = False
                sys.exit()
        screen.fill(background)

        mastermind_title.draw_text(screen)

        if button_quit.draw(screen):
            LAUNCHED = False
            sys.exit()
            
        if button_start.draw(screen):
            rules_menu(screen)
        
        if button_sound.draw(screen):
            if SOUND==False :
                SOUND=True
            else :
                SOUND=False

        if SOUND==False:
            pygame.mixer.music.pause()
            sound_desactivated.draw(screen)
        
        if SOUND==True:
            pygame.mixer.music.unpause()
            sound_activated.draw(screen)

        pygame.display.flip()

# Permet d'afficher le menu des règles
def rules_menu(screen):
    global LAUNCHED
    global SOUND

    background = 236, 222, 208
    rules = pygame.image.load("pictures/rules.png").convert()
    

    button_sound = Button(1020, 60, square_button("pictures/sound.png"))
    sound_activated = Button(1020, 60, sound_button("pictures/soundActivate.png"))
    sound_desactivated = Button(1020, 60, sound_button("pictures/soundDesactivate.png"))
       

    while LAUNCHED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LAUNCHED = False
                sys.exit()
        screen.fill(background)

        screen.blit(rules, (40, 15))

        button_next = Button(1000, 660, square_button("pictures/next.png"))
        if button_next.draw(screen):
            start_time = time.time()
            game_menu(screen, start_time)
        
        if button_sound.draw(screen):
            if SOUND==False :
                SOUND=True
            else :
                SOUND=False

        if SOUND==False:
            pygame.mixer.music.pause()
            sound_desactivated.draw(screen)
        
        if SOUND==True:
            pygame.mixer.music.unpause()
            sound_activated.draw(screen)

        pygame.display.flip()

# Annonce à l'utilisateur s'il a gagné
def win(screen, number_1, number_2, number_3, number_4):
    global LAUNCHED
    global TRY_NUMBERS
    global SOUND

    background = 236, 222, 208
    congratulations_text_1 = Text("Félicitations !", 60, 365, 200, 114, 72, 30)
    congratulations_text_2 = Text("Vous avez gagné en {} essais !".format(TRY_NUMBERS),  60, 137, 275, 114, 72, 30)
    button_restart = Button(535, 400, button("pictures/button_restart.png"))
    button_quit = Button(535, 500, button("pictures/button_quit.png"))

    #bouton son :
    button_sound = Button(1020, 60, square_button("pictures/sound.png"))
    sound_activated = Button(1020, 60, sound_button("pictures/soundActivate.png"))
    sound_desactivated = Button(1020, 60, sound_button("pictures/soundDesactivate.png"))

    if SOUND:
        pygame.mixer.music.load('sounds/applause.mp3')
        pygame.mixer.music.play(-1) #on le jooue à l'infini

    # création du temps à afficher
    number_1 = Text(str(number_1), 40, 930, 437, 246, 143, 88)
    number_2 = Text(str(number_2), 40, 950, 437, 246, 143, 88)
    colon = Text(":", 40, 970, 435, 246, 143, 88)
    number_3 = Text(str(number_3), 40, 980, 437, 246, 143, 88)
    number_4 = Text(str(number_4), 40, 1000, 437, 246, 143, 88)   #on crée indépendant chacun des chiffres du chrono
    button_hour = Button(976, 430, hour_button("pictures/clock.png"))
                    
    while LAUNCHED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LAUNCHED = False
                sys.exit()
        screen.fill(background)

        congratulations_text_1.draw_text(screen)
        congratulations_text_2.draw_text(screen)

        if button_quit.draw(screen):
            LAUNCHED = False
            sys.exit()
        if button_restart.draw(screen):
            pygame.mixer.music.load('sounds/musique.mp3')
            pygame.mixer.music.play(-1)
            start_time = time.time()
            game_menu(screen, start_time)
        
        #affichage et gestion du son
        if button_sound.draw(screen):
            if SOUND==False :
                SOUND=True
            else :
                SOUND=False

        if SOUND==False:
            pygame.mixer.music.pause()
            sound_desactivated.draw(screen)
        
        if SOUND==True:
            pygame.mixer.music.unpause()
            sound_activated.draw(screen)

        #affichage du temps
        number_1.draw_text(screen)
        number_2.draw_text(screen)
        colon.draw_text(screen)
        number_3.draw_text(screen)
        number_4.draw_text(screen)
        button_hour.draw(screen)

        pygame.display.flip()
    return ()

# Annonce à l'utilisateur si il a perdu
def lost(computer_combination, screen, number_1, number_2, number_3, number_4):
    global LAUNCHED
    global SOUND

    background = 236, 222, 208

    text_1 = Text("Dommage !", 60, 385, 75, 114, 72, 30)
    text_2 = Text("Vous avez perdu...", 50, 333, 150, 114, 72, 30)
    text_3 = Text("La combinaison correcte était :", 50, 198, 285, 114, 72, 30)

    # Affiche la combinaison qui était à trouver
    combination_show = []

    ordonate = 385

    #bouton son :
    button_sound = Button(1020, 60, square_button("pictures/sound.png"))
    sound_activated = Button(1020, 60, sound_button("pictures/soundActivate.png"))
    sound_desactivated = Button(1020, 60, sound_button("pictures/soundDesactivate.png"))

    if SOUND:
        pygame.mixer.music.load('sounds/ghost.mp3')
        pygame.mixer.music.play(-1) #on le joue à l'infini
    
    for x in range(4):
        if computer_combination[x] == "red":
                red_button = Button(390 + 100 * x, ordonate, circle_button("pictures/red.png"))
                combination_show.append(red_button)

        if computer_combination[x] == "orange":
                orange_button = Button(390 + 100 * x, ordonate, circle_button("pictures/orange.png"))
                combination_show.append(orange_button)

        if computer_combination[x] == "yellow":
                yellow_button = Button(390 + 100 * x, ordonate, circle_button("pictures/yellow.png"))
                combination_show.append(yellow_button)

        if computer_combination[x] == "green":
                green_button = Button(390 + 100 * x, ordonate, circle_button("pictures/green.png"))
                combination_show.append(green_button)

        if computer_combination[x] == "blue":
                blue_button = Button(390 + 100 * x, ordonate, circle_button("pictures/blue.png"))
                combination_show.append(blue_button)

        if computer_combination[x] == "purple":
                purple_button = Button(390 + 100 * x, ordonate, circle_button("pictures/purple.png"))
                combination_show.append(purple_button)


    # Création des boutons rejouer et quitter
    button_restart = Button(535, 540, button("pictures/button_restart.png"))
    button_quit = Button(535, 640, button("pictures/button_quit.png"))

    # création du temps à afficher
    number_1 = Text(str(number_1), 40, 930, 437, 246, 143, 88)
    number_2 = Text(str(number_2), 40, 950, 437, 246, 143, 88)
    colon = Text(":", 40, 970, 435, 246, 143, 88)
    number_3 = Text(str(number_3), 40, 980, 437, 246, 143, 88)
    number_4 = Text(str(number_4), 40, 1000, 437, 246, 143, 88)   #on crée indépendant chacun des chiffres du chrono
    button_hour = Button(976, 430, hour_button("pictures/clock.png"))

    while LAUNCHED:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LAUNCHED = False
                sys.exit()
        screen.fill(background)

        text_1.draw_text(screen)
        text_2.draw_text(screen)
        text_3.draw_text(screen)

        #affichage des boutons de couleurs
        for i in combination_show:
            i.draw(screen)

        if button_quit.draw(screen):
            LAUNCHED = False
            sys.exit()
        if button_restart.draw(screen):
            pygame.mixer.music.load('sounds/musique.mp3')
            pygame.mixer.music.play(-1)
            start_time = time.time()
            game_menu(screen, start_time)

        #affichage et gestion du son
        if button_sound.draw(screen):
            if SOUND==False :
                SOUND=True
            else :
                SOUND=False

        if SOUND==False:
            pygame.mixer.music.pause()
            sound_desactivated.draw(screen)
        
        if SOUND==True:
            pygame.mixer.music.unpause()
            sound_activated.draw(screen)

        #affichage du temps
        number_1.draw_text(screen)
        number_2.draw_text(screen)
        colon.draw_text(screen)
        number_3.draw_text(screen)
        number_4.draw_text(screen)
        button_hour.draw(screen)

        pygame.display.flip()
    return ()

## Fonctions "de rêve" (non vitales, apportent quelques améliorations qui n'interfèrent pas avec la réussite ou non du projet)

# Permet d'avoir une confirmation avant de quitter la partie
def confirmation_quit_game(screen):
    global RUNNING
    global LAUNCHED

    background = pygame.image.load("pictures/background.png")
    background.convert_alpha()
    background = pygame.transform.scale(background, (587, 154))
    background = Button(540, 360, background)
    text1 = Text("Voulez-vous vraiment quitter la partie ? ", 21, 354, 346, 114, 72, 30)
    text2 = Text("Attention, votre progression ne sera pas sauvegardée. ", 21, 280, 312, 114, 72, 30)
    yes_button = Button(670, 390, mini_button("pictures/yes.png"))
    no_button = Button(750, 390, mini_button("pictures/no.png"))

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LAUNCHED = False
                sys.exit()

        background.draw(screen)
        text1.draw_text(screen)
        text2.draw_text(screen)

        if yes_button.draw(screen):
            start_menu(screen)
        if no_button.draw(screen):
            RUNNING = False

        pygame.display.flip()

# Permet d'avoir accès aux règles durant la partie
def show_rules(screen):
    global RUNNING
    global LAUNCHED
    global SOUND

    rules = pygame.image.load("pictures/rules2.png").convert()
    button_sound = Button(1020, 60, square_button("pictures/sound.png"))
    sound_activated = Button(1020, 60, sound_button("pictures/soundActivate.png"))
    sound_desactivated = Button(1020, 60, sound_button("pictures/soundDesactivate.png"))

    while RUNNING:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LAUNCHED = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    RUNNING = False

        screen.blit(rules, (0, 0))

        #affichage et gestion du son
        if button_sound.draw(screen):
            if SOUND==False :
                SOUND=True
            else :
                SOUND=False

        if SOUND==False:
            pygame.mixer.music.pause()
            sound_desactivated.draw(screen)
        
        if SOUND==True:
            pygame.mixer.music.unpause()
            sound_activated.draw(screen)

        pygame.display.flip()

           

## On appelle la fonction principale

Mastermind()

