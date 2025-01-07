import pygame


class Button:
    """
    A class for representing a button.

    Attributes:
        x (int): left top corner x position of the button
        y (int): left top corner y position of the button
        width (int): Button's width
        height (int): Button's height
        text (str): Button's text
        font (pygame.Font): The text on the button will be written in that font
        color ((int, int, int)): Button's color
        hover_color ((int, int, int)): Button's color when mouse position is on button
    """
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font: pygame.font, color=(150, 150, 150), hover_color=(200, 200, 200)) -> None:
        """
        Constructor for button object which makes rect object as a button
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, screen: pygame.display) -> None:
        """
        A method which draws a button as a rect with text on it on screen
        """
        pygame.draw.rect(screen, self.hover_color if self.is_hovered else self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_collision(self, mouse_pos: tuple) -> None:
        """
        A method which checks if mouse position is already inside button
        """
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event: pygame.event) -> bool:
        """
        A method which checks if button is clicked
        """
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered
