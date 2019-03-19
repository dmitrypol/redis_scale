#!/usr/bin/env python3
import os
from flask import Flask
from flask import render_template
from rediscluster import StrictRedisCluster

app = Flask(__name__)

startup_nodes = [{'host': 'localhost', 'port': '7000'}]
r = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)


@app.route("/")
def web(dbsize=None, count=None, total=None, used_memory=None):

    info_memory = r.info(section='memory')
    tmp_memory = 0
    for key, value in info_memory.items():
        tmp_memory += int(value['used_memory'])
    format_memory = ("{:,}".format(tmp_memory))

    dbsize = r.dbsize()
    tmp_total=sum(dbsize.values())
    format_total = ("{:,}".format(tmp_total))

    return render_template( 'web.html', dbsize=dbsize, count=len(dbsize), total=format_total, used_memory=format_memory )
    # return str(dbsize)


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