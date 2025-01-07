import pygame


class Disc:
    """
    A class for representing a disc.

    Attributes:
        width (int): Disc's width
        height (int): Disc's height
        color ((int, int, int)): Disc's color
    """

    def __init__(self, width: int, height: int, color: tuple) -> None:
        """
        Constructor for Disc which makes object's pygame.Rect
        """
        self.color = color
        self.width = width
        self.height = height
        self.x = 300
        self.y = 200
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def is_clicked(self, event: pygame.event) -> bool:
        """
        A method which checks if this disc object is clicked
        """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

    def get_above(self, screen: pygame.display) -> None:
        """
        A method which draws a rectangle disc above the columns
        to imitate holding it up
        """
        rect1 = pygame.Rect(450 - self.width//2, 150, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect1)


class Column:
    """
    A class for representing a column.

    Attributes:
        x (int): Column's rectangle x position
    """
    def __init__(self, x: int) -> None:
        """
        Constructor for column object which makes empty list od discs on column
        """
        self.discs = []
        self.x = x
        self.y = 400

    def rem(self):
        """
        A method which removes disc the highest on the column and returns it
        """
        disc = self.discs[-1]
        self.discs.pop(-1)
        return disc

    def add(self, disc: Disc) -> None:
        """
        A method which add Disc object to column's list with discs
        """
        self.discs.append(disc)

    def drawDiscs(self, screen: pygame.display) -> None:
        """
        A method which draws on screen every disc from the biggest
        to the smallest on column
        """
        for i in range(len(self.discs)):
            self.discs[i].rect = pygame.Rect(self.x-self.discs[i].width//2, 375 - (i*25), self.discs[i].width, self.discs[i].height)
            pygame.draw.rect(screen, self.discs[i].color, self.discs[i].rect)



