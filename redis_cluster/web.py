#!/usr/bin/env python3
import os
import time
from flask import Flask
from flask import render_template
from rediscluster import StrictRedisCluster

app = Flask(__name__)

startup_nodes = [{'host': 'localhost', 'port': '7000'}]
r = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)


@app.route("/")
def web(dbsize=None, count=None, total=None, used_memory=None):

    start_time = 0
    if r.get('start_time'): start_time = r.get('start_time')
    run_time = int(time.time() - float(start_time))

    info_memory = r.info(section='memory')
    tmp_memory = 0
    for key, value in info_memory.items():
        tmp_memory += int(value['used_memory'])
    used_memory = ("{:,}".format(tmp_memory))

    dbsize = r.dbsize()
    tmp_total=sum(dbsize.values())
    num_keys = ("{:,}".format(tmp_total))

    ops_per_sec = int(tmp_total / run_time)

    return render_template('web.html', 
        dbsize=dbsize, 
        num_nodes=len(dbsize), 
        num_keys=num_keys, 
        used_memory=used_memory,
        run_time = run_time,
        ops_per_sec = ops_per_sec
        )
    # return str(run_time)


@app.route("/info")
def info():
    return(str(r.cluster('info')))


@app.route("/nodes")
def nodes():
    return(str(r.cluster('nodes')))


@app.route("/slots")
def slots():
    return(str(r.cluster('slots')))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')