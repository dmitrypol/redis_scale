#!/usr/bin/env python3
import subprocess
import jinja2

num_redis_hosts = 3

#   create proxy config file
template = open('proxy/envoy.yaml.j2').read()
config = jinja2.Template(template).render(num_redis_hosts = num_redis_hosts)
envoy_yaml = open('proxy/envoy.yaml', 'w')
envoy_yaml.write(config)

#   start containers
shell_cmd = 'docker-compose up --build -d --scale redis={}'.format(num_redis_hosts)
print(shell_cmd)
# subprocess.run(shell_cmd, shell=True, check=True)
