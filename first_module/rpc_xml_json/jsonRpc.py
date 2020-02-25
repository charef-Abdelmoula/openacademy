import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8069
DB = 'odoo1'
USER = 'charefabdo732@gmail.com'
PASS = 'charefabdo'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
   # --dev=reload :watchdog
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

# create a new session
args = {
    'name': 'session 4',
    'course_id': 1,
}
note_id = call(url, "object", "execute", DB, uid, PASS, 'first_module.session', 'create', args)
