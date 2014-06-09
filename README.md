### simple-zookeeper-viewer

A simple ZooKeeper viewer. Enough said.

#### Setup

Requires [kazoo](https://github.com/python-zk/kazoo) and [Flask](https://github.com/mitsuhiko/flask)

Requirements can be installed via pip and the provided INSTALL file.

    $ pip install -r INSTALL

#### Configuration

Change the ZK_HOSTS value to point to the ZooKeeper servers you want to view in viewer.py

#### Usage

To run simple-zookeeper-viewer, execute

    $ python viewer.py [host] [port]

Then navigate to http://localhost:5000/zk to view the root of the ZooKeeper server.

* Click on a node to view data and metadata on that node
* Double click on a node to view that node and its children
