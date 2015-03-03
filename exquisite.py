#! usr/bin/env python

import argparse
from functools import partial
import Tkinter
import math
from random import shuffle


class Game(Tkinter.Tk):
    def __init__(self, good_big, bad_big):
        Tkinter.Tk.__init__(self)
        self.label = Tkinter.Label(self, text="", width=10)
        self.label.grid(column=0, row=0)
        self.good_big = good_big
        self.bad_big = bad_big
        self.total = float(self.good_big + self.bad_big)
        self.good_percent = int(math.floor((self.good_big/self.total) * 100))
        self.bad_percent = int(math.ceil((self.bad_big/self.total) * 100))
        goods = ["O" for g in range(self.good_percent)]
        bads = ["X" for b in range(self.bad_percent)]
        all_choices = goods + bads
        shuffle(all_choices)
        self.buttons = {}
        button_num = 0
        for x in range(1, 11):
            for y in range(1, 11):
                text = all_choices.pop(-1)
                button = Tkinter.Button(self, text=text, command=partial(self.callback, (button_num)))
                self.buttons[button_num] = button
                button.grid(column=x, row=y)
                button_num += 1
        self.remaining = 0
        self.countdown(10)

    def callback(self, num):
        if self.buttons[num].config('text')[-1] == 'O':
            pass
        else:
            self.buttons[num].config(text='O')

    def get_score(self):
        score = 0
        for but in self.buttons.keys():
            if self.buttons[but].config('text')[-1] == 'O':
                score += 1
        return (score, 100-score)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.label.configure(text="Done!")
            print(self.get_score())
            game.quit()
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-good_big", "--good_big",
                        help="This is really good to have big")
    parser.add_argument("-bad_big", "--bad_big",
                        help="This is really bad to have big")
    args = parser.parse_args()
    game = Game(int(args.good_big), int(args.bad_big))
    game.wm_title("Exquisite Game")
    game.mainloop()
