### simple-zookeeper-viewer

A simple ZooKeeper viewer. Enough said.

#### Setup

Requires [kazoo](https://github.com/python-zk/kazoo) and [Flask](https://github.com/mitsuhiko/flask)

Requirements can be installed via pip and the provided INSTALL file.

    $ pip install -r INSTALL

#### Configuration

Change the ZK_HOSTS value to point to the ZooKeeper servers you want to view in viewer.py

#### Usage

* Click on a node to view data and metadata on that node
* Double click on a node to view that node and its children
