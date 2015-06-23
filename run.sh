#!/bin/bash
CLUSTER=$1
: ${CLUSTER:=localhost}
ZK_HOSTS="$CLUSTER:2181"
python -mwebbrowser 'http://localhost:5000'
python viewer.py
