import pygame
from colors import Color

class Button:

    def __init__(self, name, start_x, start_y) -> None:
        self.size_x = 30
        self.size_y = (len(name) + 1) * 10 + 3
        self.start_x = start_x
        self.start_y = start_y
        self.name = name
        
        if name != "manhattan ":
            self.color = Color.violet
        else:
            self.color = Color.orange
    
    def is_inside(self, y_pos, x_pos):
        if x_pos < self.start_x or x_pos > self.start_x + self.size_y:
            return False
        if y_pos < self.start_y or y_pos > self.start_y + self.size_x:
            return False
        return True
    
    def draw(self, win):
        pygame.init()
        pygame.draw.rect(win,self.color,[self.start_x,self.start_y, self.size_y, self.size_x])

        #text
        smallfont = pygame.font.SysFont('Verdana',16)
        text = smallfont.render(self.name , True , Color.white)
        win.blit(text, (self.start_x + 12, self.start_y + 5))
    
    def is_pushed(self):
        return self.color == Color.orange
    
    def set_pushed(self):
        self.color = Color.orange
    
    def set_not_pushed(self):
        self.color = Color.violet
    
    def get_name(self):
        return self.name


class ButtonHandler:
    b1 = None
    b2 = None
    b3 = None
    button_list = []

    @staticmethod
    def initialise_list(width):
        ButtonHandler.b1 = Button("manhattan ",20, width+10)
        ButtonHandler.b2 = Button("euclidean",160, width+10)
        ButtonHandler.b3 = Button("diagonal", 290, width+10) 
        ButtonHandler.button_list.append(ButtonHandler.b1)
        ButtonHandler.button_list.append(ButtonHandler.b2)
        ButtonHandler.button_list.append(ButtonHandler.b3)
    
    @staticmethod
    def draw_all_buttons(win):
        ButtonHandler.b1.draw(win)
        ButtonHandler.b2.draw(win)
        ButtonHandler.b3.draw(win)
    
    @staticmethod
    def click_proper_button(x_pos, y_pos):
        for button in ButtonHandler.button_list:
            if button.is_inside(x_pos, y_pos):
                for other_button in ButtonHandler.button_list:
                    other_button.set_not_pushed()
                button.set_pushed()
                return button.get_name()
        return None
