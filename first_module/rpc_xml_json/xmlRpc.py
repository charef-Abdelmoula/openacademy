import functools
import xmlrpc.client
HOST = 'localhost'
PORT = 8069
DB = 'odoo1'
USER = 'charefabdo732@gmail.com'
PASS = 'charefabdo'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print("Logged in as %s (uid:%d)" % (USER,uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
# 2. Read the sessions
sessions = call('first_module.session','search_read', [], ['name','seats'])
for session in sessions:
    print("Session %s (%s seats)" % (session['name'], session['seats']))

# 3.create a new session for the "Functional" course
# 3.create a new session
session_id = call('first_module.session', 'create', {
    'name' : 'My session',
    'course_id' : 2,
})
print(call('first_module.course', 'search', [('name','ilike','COURSE 1')])[0])

for session in sessions:
    print("Session %s (%s seats)" % (session['name'], session['seats']))