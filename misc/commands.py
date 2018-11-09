from talon import voice

from collections import defaultdict
import json
import os

try:
    from user import std
    alnum = std.alpha_alt
except Exception:
    alnum = []

response = {'contexts': {}}
response['alnum'] = alnum

for name, ctx in voice.talon.subs.items():
    d = response['contexts'][ctx.name] = {
        'active': ctx in voice.talon.active,
        'commands': [],
    }
    commands = d['commands']
    for trigger, rule in ctx.triggers.items():
        if trigger.split(' ')[-1] in alnum:
            continue
        actions = ctx.mapping[rule]
        if not isinstance(actions, (list, tuple)):
            actions = [actions]
        if len(actions) > 1 and all(isinstance(a, voice.Key) for a in actions):
            if len(set(a.data for a in actions)) == 1:
                commands.append((trigger, f'key({actions[0].data}) * {len(actions)}'))
                continue
        pretty = []
        for action in actions:
            if isinstance(action, voice.Key):
                keys = action.data.split(' ')
                if len(keys) > 1 and len(set(keys)) == 1:
                    pretty.append(f'key({keys[0]}) * {len(keys)}')
                else:
                    pretty.append(f'key({action.data})')
            elif isinstance(action, voice.Str):
                pretty.append(f'"{action.data}"')
            elif isinstance(action, voice.Rep):
                pretty.append(f'repeat({action.data})')
            elif isinstance(action, voice.RepPhrase):
                pretty.append(f'repeat_phrase({action.data})')
            elif isinstance(action, str):
                pretty.append(f'"{action}"')
            elif callable(action):
                pretty.append(f'{action.__name__}()')
            else:
                pretty.append(str(action))
        if len(pretty) == 1:
            pretty = pretty[0]
        commands.append((trigger, pretty))

with open(os.path.expanduser('~/.talon/commands.json'), 'w') as f:
    json.dump(response, f)
