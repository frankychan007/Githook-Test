import json
from subprocess import call
import shlex
import pexpect

servers = json.loads(open('server.json').read().strip())
for i in servers:
    commond = "git  " + i['name'] + " master "
    child = pexpect.spawn(commond)
    #child.expect ('Name .*: ')
    child.sendline (i['password'])
