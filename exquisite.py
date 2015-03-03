#! usr/bin/env python

import argparse
from functools import partial
import Tkinter
import math

class ExampleApp(Tkinter.Tk):
    def __init__(self, good_big, bad_big):
        Tkinter.Tk.__init__(self)
        self.label = Tkinter.Label(self, text="", width=10)
        self.label.grid(column=0, row=0)
        self.total = float(good_big + bad_big)
        for x in range(1, 11):
            for y in range(1, 11):
                #Choose a good or bad, place it appropriately
                button = Tkinter.Button(self, command=partial(self.callback, (x, y)))
                button.configure(bg="red")
                button.grid(column=x, row=y)
        self.remaining = 0
        self.countdown(10)

    def callback(self, nums):
        x, y = nums

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
            print(math.floor((good_big/self.total) * 100), math.ceil((bad_big/self.total) * 100))
            app.quit()
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
    app = ExampleApp(int(args.good_big), int(args.bad_big))
    app.mainloop()
