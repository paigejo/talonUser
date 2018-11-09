from talon import keychain
from talon.voice import Context, Key, Str

def insert(service, user=None):
    if user is None:
        user = service
    def wrapper(m):
        pw = keychain.find(service, user)
        Str(pw)(None)
    return wrapper

ctx = Context('passwords')
ctx.keymap({
    'password computer': insert('computer', 'paigejo'),
    'password amazon': insert('amazon', 'paigejo'),
    'password apple': insert('apple', 'paigejo'),
    'password fidelity': insert('fidelity', 'paigejo24'),
    'password school': insert('school', 'paigejo'),
    'password auto fill': Key('cmd-\\'),
})
