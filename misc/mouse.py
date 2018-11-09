# from https://github.com/talonvoice/examples
# jsc added shift-click, command-click, and voice code compatibility

# import eye
import time
from talon import ctrl, tap
from talon.voice import Context
from .. import utils

ctx = Context("mouse")

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None


def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True


tap.register(tap.MMOVE, on_move)


def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]


def delayed_click(m, button=0, times=1):
    # old = eye.config.control_mouse
    # eye.config.control_mouse = False
    # x, y = click_pos(m)
    # ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    # time.sleep(0.032)
    # eye.config.control_mouse = old


# jsc added
def press_key_and_click(m, key, button=0, times=1, wait=16000):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(x, y, button=button, times=times, wait=wait)
    ctrl.key_press(key, up=True)


# jsc added
def shift_click(m, button=0, times=1):
    press_key_and_click(m, "shift", button, times)


def command_click(m, button=0, times=1):
    press_key_and_click(m, "cmd", button, times)

def control_click(m, button=0, times=1):
    press_key_and_click(m, "cntrl", button, times)

def delayed_right_click(m):
    delayed_click(m, button=1)


def delayed_dubclick(m):
    delayed_click(m, button=0, times=2)


def delayed_tripclick(m):
    delayed_click(m, button=0, times=3)


def mouse_scroll(amount):
    def scroll(m):
        ctrl.mouse_scroll(y=amount)

    return scroll

def mouse_scroll_up_custom(amount):
    amount = utils.m_to_number(amount)
    def scroll(m):
        ctrl.mouse_scroll(y=amount)

    return scroll

def mouse_scroll_down_custom(amount):
    amount = utils.m_to_number(amount)
    def scroll(m):
        ctrl.mouse_scroll(y=-amount)

    return scroll

def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, down=True)


def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, up=True)

def adv_click(button, *mods, **kwargs):

    def click(e):
        for key in mods:
            ctrl.key_press(key, down=True)
        delayed_click(e)
        for key in mods[::-1]:
            ctrl.key_press(key, up=True)

    return click

def mouse_down(amount=200):
    
    def move(m):
        x, y = click_pos(m)
        ctrl.mouse(x, y, dy=amount)
    
    return move

keymap = {
    # jsc modified with some voice-code compatibility
    "(righty | chipper)": delayed_right_click,
    "(click | chiff)": delayed_click,
    "(dubclick | duke)": delayed_dubclick,
    "(tripclick | triplick)": delayed_tripclick,
    "drag": mouse_drag,
    "release": mouse_release,
    # jsc added
    "(shift click | shicks)": adv_click(0, "shift"),
    "(command click | chom lick)": adv_click(0, "cmd"),
    "(control click | chomp)": adv_click(0, "ctrl"),
    "wheel down": mouse_scroll(200),
    "wheel up": mouse_scroll(-200),
    "mouse down": mouse_down(200),
    
    # doesn't seem to work
    "wheel down" + utils.numerals: mouse_scroll_up_custom,
    "wheel up" + utils.numerals: mouse_scroll_down_custom,
}

ctx.keymap(keymap)
