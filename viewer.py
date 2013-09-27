import json
from flask import Flask, render_template, g, jsonify, request
from kazoo.client import KazooClient
app = Flask(__name__)

# Host string of the ZooKeeper servers to connect to
ZK_HOSTS = '127.0.0.1:2181'

# Node metadata to view
ZNODESTAT_ATTR = [
    'aversion',
    'ctime',
    'czxid',
    'dataLength',
    'ephemeralOwner',
    'mtime',
    'mzxid',
    'numChildren',
    'version']

@app.before_request
def before_request():
    if request.path.startswith('/nodes/') or request.path.startswith('/data/'):
        g.zk = KazooClient(hosts=ZK_HOSTS, read_only=True)
        g.zk.start()

@app.teardown_request
def teardown_request(exception):
    if 'zk' in g:
        g.zk.stop()
        g.zk.close()

@app.route('/zk/', defaults={'path': ''})
@app.route('/zk/<path:path>')
def view(path):
    return render_template('zk.html', path=path, host=ZK_HOSTS)

@app.route('/nodes/', defaults={'path': ''})
@app.route('/nodes/<path:path>')
def nodes(path):
    ancestors = []
    full_path = ''
    ancestors.append({
        'name': '/',
        'full_path': '/'})
    for ancestor in path.split('/'):
        if ancestor != '':
            full_path += '/' + ancestor
            ancestors.append({
                'name': ancestor,
                'full_path': full_path})
    children = sorted(g.zk.get_children(path))
    return render_template('_nodes.html',
        path=full_path + '/',
        children=children,
        ancestors=ancestors)

@app.route('/data/', defaults={'path': ''})
@app.route('/data/<path:path>')
def data(path):
    node = g.zk.get(path)
    meta = {}
    for attr in ZNODESTAT_ATTR:
        meta[attr] = getattr(node[1], attr)
    if path.endswith('/'):
        path = path[:-1]
    data = parse_data(node[0])
    return render_template('_data.html',
        path='/' + path,
        data=data,
        is_dict=type(data) == dict,
        meta=meta);

def parse_data(raw_data):
    try:
        data = json.loads(raw_data)
        return data
    except:
        return raw_data

if __name__ == '__main__':
    app.run()
