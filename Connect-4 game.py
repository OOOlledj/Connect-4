from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.config import Config

from kivy.uix.button import Button

from utilities import getsxy, makexy, iscolor,\
    find_end_dots, find_end_steps, BCOLOR, RED, BLU

import math

Config.set("graphics","resizable","0")
Config.set("graphics","width","700")
Config.set("graphics","height","600")

class gameapp(App):

    def connect4(self, gbtn):
        '''initialize game process'''

        gbtn.background_color = BCOLOR[self.switch]
        gbtn.disabled = True
        self.gPickedbtn.append(gbtn)

        for elem in self.GameButtons:
           elemx, elemy = getsxy(elem)
           gbtnx, gbtny = getsxy(gbtn)
           if (elemy == gbtny) and (elemx == gbtnx - 1):
                elem.disabled = False
                self.gAvailable.append(elem)

        for elem in self.gPickedbtn:
            foundflag = False
            playercolor = elem.background_color
            x,y = getsxy(elem)
            fdots = find_end_dots(x,y)
            steps = find_end_steps(x, y, fdots)

            for pair in steps:
                ix, iy = pair[0], pair[1]
                bx, by = x, y
                i = 0
                colorcount = 0

                while i < 3:
                    bx+= ix
                    by+= iy
                    bxby = makexy(bx,by)
                    for button in self.GameButtons:
                        if button.text == bxby:
                            compare = button
                            break
                    if compare.background_color == elem.background_color:
                        colorcount+= 1
                    i += 1

                if colorcount == 3:
                    foundflag = True
                    break
            if foundflag:
                for elem in self.GameButtons:
                    elem.disabled = True
                break

        if not self.switch:
            self.switch = 1
            self.status.text = 'Blue player turn'
            self.status.color = BLU
        else:
            self.switch = 0
            self.status.text = 'Red player turn'
            self.status.color = RED

        self.rounds+= 1
        if self.rounds == 42:
            self.status.text = 'Draw'
            self.status.color = [1,1,1,1]
        if foundflag:
            self.status.text = '{} player won'.format(iscolor(playercolor))
            self.status.color = playercolor



    def resetgame(self, *args):
        '''starts game from beginning;
        used in self.build to initialaze basic sequences and params'''
        self.GameButtons = []
        self.gAvailable = []
        self.gPickedbtn = []

        for index in range(56):
            self.WidgetButtons[index].color = [0, 0, 0, .1] if not ((index % 8 == 0 or index < 8)) else [1,1,1,1]
            self.WidgetButtons[index].disabled = True
            self.WidgetButtons[index].font_size = 24
            self.WidgetButtons[index].background_color = [.9, .9, .9, 1] if not ((index % 8 == 0 or index < 8)) else [.1,.1,.1,1]


            if len(self.WidgetButtons[index].text) == 3:
                self.GameButtons.append(self.WidgetButtons[index])

        #reset button
        self.WidgetButtons[0].color = [.01, .01, .02, 1]
        self.WidgetButtons[0].background_color = [.91, .91, .91, 1]
        self.WidgetButtons[0].disabled = False
        self.WidgetButtons[0].font_size = 18
        self.WidgetButtons[0].text = "RESET"

        for btn in self.GameButtons:
            if len(btn.text) == 3:
                x,y = getsxy(btn)
                if x == 6 and y > 0:
                    btn.disabled = False
                    self.gAvailable.append(btn)

        self.rounds = 0
        self.status.text = 'Start from red player!'
        self.switch = 0

    def build(self):
        '''initializing kivy interface'''
        self.title = "Connect 4"
        self.icon = '4.png'

        root = BoxLayout(orientation="vertical", padding=3)
        grid = GridLayout(cols=8)

        self.GameButtons = []
        self.WidgetButtons = []

        for index in range(56):
            define_text = ''
            if index == 0:       pass
            elif index % 8 == 0: define_text = str(int(index/8))
            elif index < 8:      define_text = str(index)
            else:                define_text = str(math.trunc(index/8)) + ' ' + str(index % 8)

            self.WidgetButtons.append(Button(
                    text =  define_text,
                    on_press = self.connect4 if index != 0 else self.resetgame
                ))

            grid.add_widget(self.WidgetButtons[index])

        self.status = Label(
            size_hint = [1,.1],
            font_size = 28,
            color = RED
            )
        self.resetgame()

        root.add_widget(grid)
        root.add_widget(self.status)

        return root

if __name__ == "__main__":
    gameapp().run()