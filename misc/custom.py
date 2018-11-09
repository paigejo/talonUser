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
})
