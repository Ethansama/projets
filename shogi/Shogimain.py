import pygame
import Shogiengine

Largeur = longeur = 400
dimensions = 9
taillec = Largeur//dimensions
fps = 60
images = {}

def charger_images():
    pcs = ["Lj","Cj","Aj","Oj","Tj","Fj","Pj","J","R","Or","Ar","Cr","Lr","Tr","Fr","Pr"]
    for pc in pcs:
        img = pygame.image.load("images/" + pc + ".png")
        img = pygame.transform.scale(img, (taillec, taillec))
        images[pc] = img


def prin():
    pygame.init()
    ecran = pygame.display.set_mode((Largeur,longeur))
    horloge = pygame.time.Clock()
    ecran.fill(pygame.Color("white"))
    game = Shogiengine.Game()
    print(game.tablier)
    charger_images()
    run = True
    carselec = ()
    clics = []
    while run:
        for w in pygame.event.get():
            if w.type == pygame.QUIT:
                run = False
            elif w.type == pygame.MOUSEBUTTONDOWN:
                local = pygame.mouse.get_pos()
                colonne = local[0]//taillec
                ligne = local[1]//taillec
                if carselec() == (ligne,colonne):
                    carselec = ()
                    clics = []
                else:
                    carselec = (ligne,colonne)
                    clics.append(carselec)
                if len(clics) == 2:
                    pass

        dessine_jeu(ecran,game)
        horloge.tick(fps)
        pygame.display.flip()

def dessine_jeu(ecran, game):
    dessinetablier(ecran)
    dessinepcs(ecran, game.tablier)

def dessinetablier(ecran):
    couls = [pygame.Color('white'), pygame.Color('black')]
    for c in range(dimensions):
        for l in range(dimensions):
            coul = couls[((c+l) % 2)]
            pygame.draw.rect(ecran,coul,pygame.Rect(l*taillec,c*taillec,taillec,taillec))

def dessinepcs(ecran,tablier):
    for r in range(dimensions):
        for c in range(dimensions):
            pc = tablier[r][c]
            if pc != '--':
                ecran.blit(images[pc], pygame.Rect(c*taillec, r*taillec, taillec, taillec))



prin()