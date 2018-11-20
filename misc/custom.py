## John Paige
# custom user commands

from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

ctx = Context('custom')
ctx.keymap({
    'new document': [Key('cmd-n')], 
    'marco': [Key('cmd-f')], 
    'olly': Key('cmd-a'), 
    'sky koosh': Key('shift-space'), 
    'prome': Key('home'), 
    'prend': Key('end'), 
    'dot calm': '.com', 
    'dot edu': '.edu', 
    'dot gov': '.gov', 
    'quit this application': Key('cmd-q'), 
    
    'dose': '2', 
    'quads': '4', 
    'hundred': '00', 
    'thousand': '000', 
})
