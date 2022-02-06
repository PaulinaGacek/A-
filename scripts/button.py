import pygame

class Button:

    def __init__(self, name) -> None:
        self.size_x = 20
        self.size_y = 20
        self.name = name
        self.pushed = False
    
    def draw(self, win, width, start_x, start_y):
        pygame.init()
        length = (len(self.name)+1)*10 + 3
        pygame.draw.rect(win,(119,125,167),[start_x,start_y,length,30])

        #text
        color = (255,255,255)
        smallfont = pygame.font.SysFont('Verdana',16)
        text = smallfont.render(self.name , True , color)
        win.blit(text, (start_x + 12, start_y + 5))


class ButtonHandler:
    b1,b2,b3 = Button("manhattan "), Button("euclidean"), Button("diagonal") 
    button_list = []

    def initialise_list():
        ButtonHandler.button_list.append(ButtonHandler.b1)
        ButtonHandler.button_list.append(ButtonHandler.b2)
        ButtonHandler.button_list.append(ButtonHandler.b3)
    
    @staticmethod
    def draw_all_buttons(win,width):
        ButtonHandler.b1.draw(win, width, 20, width+10)
        ButtonHandler.b2.draw(win, width, 160, width+10)
        ButtonHandler.b3.draw(win, width, 290, width+10)