import json
from subprocess import call
import shlex

servers = json.loads(open('server.json').read().strip())
for i in servers:
    commond = 'git remote add ' + i['name'] + ' root@' + i["ip"] + ":proj"
    print(commond)
    call(shlex.split(commond))
