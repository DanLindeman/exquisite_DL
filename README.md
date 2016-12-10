# exquisite_DL
The exquisite corpse game 

# About
This is an incredibly simple game, inspired by the Surrealist game Exquisite Corpse:
http://en.wikipedia.org/wiki/Exquisite_corpse

Instead of lines to continue a picture, exquisite games pass command-line arguments to one-another.

Since this is the first iteration of Exquisite Game that I know of, we chose something simple to pass.
For this iteration, a pair of integers.

On a very high level each individual game does something like this:

(12, 1004) -> *Exquisite Game Alters the values* -> (333, 10)

and so on...

One set of guidelines used for creating this game was that one of the numbers should be good if big, the other bad.

# Example Usage:
```
python exquisite.py -good_big 42 -bad_big 66
```
# Objective
You have ten seconds! There will be a number of X labeled buttons, click them to turn them to an O button! Convert as many as you can!

![Image of Exquisite Game](https://github.com/DanLindeman/exquisite_DL/blob/master/Exquisite_Game.png)
```
>>>(78, 22)
```
