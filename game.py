import pygame
import random

pygame.init()


class Puzzle:
    blockVariety = [
        [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
        [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
        [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 0, 0], [1, 0, 0], [1, 1, 1]],

        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],

        [[1, 1, 1], [0, 1, 0]],
        [[0, 1, 0], [1, 1, 1]],
        [[0, 1], [1, 1], [0, 1]],
        [[1, 0], [1, 1], [1, 0]],

        [[1, 1, 1], [1, 0, 0]],
        [[1, 1, 1], [0, 0, 1]],
        [[1, 0, 0], [1, 1, 1]],
        [[0, 0, 1], [1, 1, 1]],

        [[0, 1], [0, 1], [1, 1]],
        [[1, 0], [1, 0], [1, 1]],
        [[1, 1], [0, 1], [0, 1]],
        [[1, 1], [1, 0], [1, 0]],

        [[1, 1], [1, 1]],

        [[1, 1], [1, 0]],
        [[1, 1], [0, 1]],
        [[0, 1], [1, 1]],
        [[1, 0], [1, 1]],

        [[1]],

        [[1, 1]],
        [[1, 1, 1]],
        [[1, 1, 1, 1]],
        [[1, 1, 1, 1, 1]],

        [[1], [1]],
        [[1], [1], [1]],
        [[1], [1], [1], [1]],
        [[1], [1], [1], [1], [1]],
    ]
    dataMap = []
    score = 0
    X = 0
    Y = 0

    def __init__(self):
        self.height = 10
        self.width = 10
        self.nextOb = random.choice(self.blockVariety)
        self.currentObj = self.nextOb
        self.objWidth = len(self.currentObj[0])
        self.objHeight = len(self.currentObj)
        self.screenWidth = 850
        self.screenHeight = 500
        self.tileWidth = 39
        self.tileHeight = 39
        self.margin = 10
        self.colorPalette = {"filled": (232, 93, 4), "blank": (83, 144, 217), "background": (229, 229, 229),
                             "demo": (255, 209, 102), "menu": (20, 33, 61), "text": (255, 255, 255), "button": (231, 111, 81)}
        self.win = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("Block Game")
        self.game_window = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.font = pygame.font.Font('freesansbold.ttf', 35)
        
        for i in range(self.height):
            new_line = []
            for j in range(self.height):
                new_line.append(0)
            self.dataMap.append(new_line)

        run = True
        while run:
            pygame.time.delay(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.win.fill(self.colorPalette["background"])
            self.menu = pygame.draw.rect(self.win, self.colorPalette["menu"], (500, 0, 400, 500))
            self.restartButton = pygame.draw.rect(self.win, self.colorPalette["button"], (600, 400, 150, 60))
            self.mousePos = pygame.mouse.get_pos()
            self.highScore = open("highScore.txt", "r").read()
            self.textRenderer(self.score, (640, 132), self.colorPalette["text"])
            self.textRenderer("Score:", (510, 130), self.colorPalette["text"])
            self.textRenderer("Block Game", (525, 50), (46, 196, 182))
            self.textRenderer("Quit", (635, 415), (self.colorPalette["text"]))
            self.textRenderer("High score:", (510, 200), self.colorPalette["text"])
            self.textRenderer(self.highScore, (710, 202), self.colorPalette["text"])

            if int(self.highScore) < self.score:
                open("highScore.txt", "w").write(str(self.score))

            for cy in range(self.height):
                for cx in range(self.width):
                    if self.dataMap[cy][cx] == 0:
                        self.colour = self.colorPalette["blank"]
                    elif self.dataMap[cy][cx] == 1:
                        self.colour = self.colorPalette["filled"]
                    pygame.draw.rect(self.win,
                                     self.colour,
                                     ((self.margin + self.tileWidth) * cx + self.margin,
                                      (self.margin + self.tileHeight) * cy + self.margin,
                                      self.tileWidth, self.tileHeight))

            # horizontal check point
            for xx in range(len(self.dataMap)):
                if self.dataMap[xx] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                    self.score += 10
                    self.dataMap[xx] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # ????
            # for yy in range(len(self.dataMap[0])):
            #     cc = list(map(list, zip(*self.dataMap[::-1])))
            #     if cc[yy] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
            #         self.score += 10
            #         cc[yy] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # vertical check point
            for xx in range(len(self.dataMap[0])):
                if self.dataMap[0][xx] == 1 and self.dataMap[1][xx] == 1 and self.dataMap[2][xx] == 1 and \
                        self.dataMap[3][xx] == 1 and self.dataMap[4][xx] == 1 and self.dataMap[5][xx] == 1 and \
                        self.dataMap[6][xx] == 1 and self.dataMap[7][xx] == 1 and self.dataMap[8][xx] == 1 and \
                        self.dataMap[9][xx] == 1:
                    self.score += 10
                    self.dataMap[0][xx] = 0
                    self.dataMap[1][xx] = 0
                    self.dataMap[2][xx] = 0
                    self.dataMap[3][xx] = 0
                    self.dataMap[4][xx] = 0
                    self.dataMap[5][xx] = 0
                    self.dataMap[6][xx] = 0
                    self.dataMap[7][xx] = 0
                    self.dataMap[8][xx] = 0
                    self.dataMap[9][xx] = 0

            # demo
            for by in range(self.objHeight):
                for bx in range(self.objWidth):
                    if self.currentObj[by][bx] == 1:
                        pygame.draw.rect(self.win,
                                         self.colorPalette["demo"],
                                         (self.X * 49 + self.margin * 1.5 + bx * 49,
                                          self.Y * 49 + self.margin * 1.5 + by * 49,
                                          self.tileWidth - 10, self.tileHeight - 10))

            if not self.movesLeft():
                run = False

            # move demo and end game
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.X > 0:
                self.X -= 1
            if keys[pygame.K_RIGHT] and self.X < self.width - self.objWidth:
                self.X += 1
            if keys[pygame.K_UP] and self.Y > 0:
                self.Y -= 1
            if keys[pygame.K_DOWN] and self.Y < self.width - self.objHeight:
                self.Y += 1
            if keys[pygame.K_SPACE]:
                self.project(self.currentObj)
                self.objWidth = len(self.currentObj[0])
                self.objHeight = len(self.currentObj)
            if pygame.mouse.get_pressed()[0] and 575 < self.mousePos[0] < 725 and 400 < self.mousePos[1] < 460:
                run = False
            if keys[pygame.K_ESCAPE]:
                run = False

            pygame.display.update()
        print("you lost!!!")
        print("you scored: " + str(self.score))
        for m in self.dataMap:
            print(m)
        for n in self.currentObj:
            print(n)
        print()


    def new_figure(self):
        self.currentObj = self.nextOb
        self.nextOb = random.choice(self.blockVariety)

    def project(self, shape):
        if self.intersectionTest(shape, self.X, self.Y):
            return
        for a in range(self.objHeight):
            for b in range(self.objWidth):
                if shape[a][b] != 0:
                    self.dataMap[self.Y + a][self.X + b] = 1
        self.X = 0
        self.Y = 0
        self.new_figure()

    def intersectionTest(self, shape, X, Y):
        for aa in range(self.objHeight):
            for bb in range(self.objWidth):
                if self.dataMap[Y + aa][X + bb] == 1 and shape[aa][bb] == 1:
                    return True
        return False

    def textRenderer(self, text, location, color):
        self.win.blit(self.font.render(str(text), True, color), location)

    def movesLeft(self):
        cc = False
        for aa in range(self.height-self.objHeight):
            for bb in range(self.width-self.objWidth):
                if not self.intersectionTest(self.currentObj, bb, aa):
                    cc = True
        "no more moves"
        # if not cc:
        #     for aa in range(self.height-self.objHeight):
        #         for bb in range(self.width-self.objWidth):
        #             print(self.intersectionTest(self.currentObj, bb, aa))
        #     print(self.nextOb)
        return cc


Puzzle()
