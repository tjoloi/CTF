from nclib import netcat
import json

nc = netcat.Netcat(('challenges.unitedctf.ca', 3005))
r = nc.recv()
data = json.loads(r)

child = data['child']['child']
child['grandparent'] = data['name']

nc.send(json.dumps(child))
print(nc.recv().decode())