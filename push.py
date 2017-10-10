import json
from subprocess import call
import shlex
import pexpect

servers = json.loads(open('server.json').read().strip())
for i in servers:
    commond = "git push " + i['name'] + " master"
    print("Running " + commond)
    child = pexpect.spawn(commond)
    child.expect('root')
    child.sendline(i['password'])
    output = str(child.read()).replace('\\n', '')
    for o in output.split('\\r'):
        print(o.strip())
    print("================================")

#git push production master
