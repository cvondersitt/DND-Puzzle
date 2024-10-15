from graphics import *
import sys
import os

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 900
win = GraphWin("Puzzle", WINDOW_WIDTH, WINDOW_HEIGHT)



def resource_path(relative_path):
    """ Get the absolute path to the resource, works for PyInstaller bundles. """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Example usage in your script:


def buttons():
    abj = Rectangle(Point(0, 600), Point(300, 900))  # points are ordered ll, ur
    conj = Rectangle(Point(300, 600), Point(600, 875))
    div = Rectangle(Point(600, 600), Point(900, 900))
    enc = Rectangle(Point(0, 300), Point(300, 600))
    evo = Rectangle(Point(300, 300), Point(600, 600))
    hae = Rectangle(Point(600, 300), Point(900, 600))
    ill = Rectangle(Point(0, 0), Point(300, 300))
    necro = Rectangle(Point(300, 0), Point(600, 300))
    tra = Rectangle(Point(600, 0), Point(900, 300))
    reset = Rectangle(Point(300, 875), Point(600, 900))

    reset.setFill("Blue")
    abj.setFill("White")
    conj.setFill("White")
    div.setFill("White")
    enc.setFill("White")
    evo.setFill("White")
    hae.setFill("White")
    ill.setFill("White")
    necro.setFill("White")
    tra.setFill("White")

    abj.draw(win)
    conj.draw(win)
    div.draw(win)
    enc.draw(win)
    evo.draw(win)
    hae.draw(win)
    ill.draw(win)
    necro.draw(win)
    tra.draw(win)   
    reset.draw(win)

    return abj, conj, div, enc, evo, hae, ill, necro, tra, reset

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def sigils():
    """ Adds sigils to board"""
    abj = Image(Point(150, 750), resource_path('sigils/abj.png'))
    conj = Image(Point(450, 750), resource_path('sigils/conj.png'))
    div = Image(Point(750, 750), resource_path('sigils/div.png'))
    enc = Image(Point(150, 450), resource_path('sigils/enc.png'))
    evo = Image(Point(450, 450), resource_path('sigils/evo.png'))
    hae = Image(Point(750, 450), resource_path('sigils/hae.png'))
    ill = Image(Point(150, 150), resource_path('sigils/ill.png'))
    necro = Image(Point(450, 150), resource_path('sigils/necro.png'))
    tra = Image(Point(750, 150), resource_path('sigils/tra.png'))

    abj.draw(win)
    conj.draw(win)
    div.draw(win)
    enc.draw(win)
    evo.draw(win)
    hae.draw(win)
    ill.draw(win)
    necro.draw(win)
    tra.draw(win)

def sigiltext():
    abj = Text(Point(150, 610), "Abjuration")
    conj = Text(Point(450, 610), "Conjuration")
    div = Text(Point(750, 610), "Divination")
    enc = Text(Point(150,310 ), "Enchantry")
    evo = Text(Point(450,310 ), "Evocation")
    hae = Text(Point(750,310 ), "Haemomancy")
    ill = Text(Point(150,10 ), "Illusion")
    necro = Text(Point(450,10), "Necromancy")
    tra = Text(Point(750,10), "Transmutation")
    reset = Text(Point(450,885), "Reset")

    abj.draw(win)
    conj.draw(win)
    div.draw(win)
    enc.draw(win)
    evo.draw(win)
    hae.draw(win)
    ill.draw(win)
    necro.draw(win)
    tra.draw(win)
    reset.draw(win)

abj, conj, div, enc, evo, hae, ill, necro, tra, resetbut = buttons()

sigils()
sigiltext()

def reset():
    abj.setFill("White")
    conj.setFill("White")
    div.setFill("White")
    enc.setFill("White")
    evo.setFill("White")
    hae.setFill("White")
    ill.setFill("White")
    necro.setFill("White")
    tra.setFill("White")
    curr.clear()

text = Text(Point(450, 450), "Select a Sigil")

solution = [9, 1, 3, 4, 5, 7, 8, 2, 6]
curr = []

wrong = Text(Point(450, 600), "Your solution is incorrect! Press reset")
correct = Text(Point(450, 600), "You answered the puzzle correctly!")

while True:
    clickPoint = win.getMouse()

    if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
        text.draw(win)
    elif inside(clickPoint, abj):
        text.undraw()
        abj.setFill("Grey")
        if 7 not in curr:
            curr.append(7)
    elif inside(clickPoint, conj):
        text.undraw()
        conj.setFill("Grey")
        if 8 not in curr:
            curr.append(8)
    elif inside(clickPoint, div):
        text.undraw()
        div.setFill("Grey")
        if 9 not in curr:
            curr.append(9)
    elif inside(clickPoint, enc):
        text.undraw()
        enc.setFill("Grey")
        if 4 not in curr:
            curr.append(4)
    elif inside(clickPoint, evo):
        text.undraw()
        evo.setFill("Grey")
        if 5 not in curr:
            curr.append(5)
    elif inside(clickPoint, hae):
        text.undraw()
        hae.setFill("Grey")
        if 6 not in curr:
            curr.append(6)
    elif inside(clickPoint, ill):
        text.undraw()
        ill.setFill("Grey")
        if 1 not in curr:
            curr.append(1)
    elif inside(clickPoint, necro):
        text.undraw()
        necro.setFill("Grey")
        if 2 not in curr:
            curr.append(2)
    elif inside(clickPoint, tra):
        text.undraw()
        tra.setFill("Grey")
        if 3 not in curr:
            curr.append(3)
    elif inside(clickPoint, resetbut):
        reset()
        correct.undraw()
        wrong.undraw()

    else:
        text.undraw()
    if curr == solution:
        correct.setSize(36)
        correct.setStyle("bold")
        correct.setOutline("White")
        abj.setFill("Green")
        conj.setFill("Green")
        div.setFill("Green")
        enc.setFill("Green")
        evo.setFill("Green")
        hae.setFill("Green")
        ill.setFill("Green")
        necro.setFill("Green")
        tra.setFill("Green")
        correct.draw(win)

    if len(curr) == len(solution) and curr != solution:
        wrong.setSize(36)
        wrong.setStyle("bold")
        wrong.setTextColor("Black")
        wrong.setOutline("White")
        abj.setFill("Red")
        conj.setFill("Red")
        div.setFill("Red")
        enc.setFill("Red")
        evo.setFill("Red")
        hae.setFill("Red")
        ill.setFill("Red")
        necro.setFill("Red")
        tra.setFill("Red")
        wrong.draw(win)
        
    



win.close()