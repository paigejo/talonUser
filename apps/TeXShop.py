## John Paige
# commands for texshop

from talon.voice import Word, Context, Key, Rep, Str, press
import time
from talon import ctrl, tap

ctx = Context('TeXShop', bundle='TeXShop')


ctx.keymap({
    'typeset': Key('cmd-t'), 
})
