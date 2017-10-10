import json
from subprocess import call
import shlex

servers = json.loads(open('server.json').read().strip())
for i in servers:
    commond = 'git remote add ' + i['name'] + ' ' + i['username'] + '@' + i["ip"] + ":" + i['path']
    print("Running: " + commond)
    call(shlex.split(commond))
