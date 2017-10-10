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
    print(child.read())

#git push production master
