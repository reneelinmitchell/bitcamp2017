"""Example of writing JSON format graph data and using the D3 Javascript library to produce an HTML/Javascript drawing.
"""
# Author: Aric Hagberg <aric.hagberg@gmail.com>

#    Copyright (C) 2011-2016 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.
import json
import networkx as nx
from networkx.readwrite import json_graph
import flask
import Master_Program
from flask import request
from flask import render_template
from networkx.readwrite import json_graph
"""
#Master_Program.master_program(user_input)
G = nx.barbell_graph(6,3)
# this d3 example uses the name attribute for the mouse-hover value,
# so add a name to each node
for n in G:
    G.node[n]['name'] = n
# write json formatted data
d = json_graph.node_link_data(G) # node-link format to serialize
# write json
json.dump(d, open('force/force.json','w'))
print('Wrote node-link JSON data to force/force.json')
"""
# Serve the file over http to allow for cross origin requests
app = flask.Flask(__name__, static_folder="force")

@app.route('/')
def mainpage(name=None):
    return render_template("index.html",name=name)



@app.route('/<path:path>',methods=['POST'])
def my_form_post(path):
    if request.method == 'POST':
        text = request.form['text']
        individual = text.upper()
        l = Master_Program.master_program(individual)
        G = nx.Graph()
        G.add_node(individual)
        for i in l:
            node = i.split(':')
            G.add_node(node[0])
            G.add_weighted_edges_from([(individual,node[0],node[1])])
        d = json_graph.node_link_data(G)  # node-link format to serialize
        # write json
        json.dump(d, open('force/force.json', 'w'))
        print('Wrote node-link JSON data to force/force.json')
    return app.send_static_file(path)

'''
@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)
'''
print('\nGo to http://localhost:8000/force.html to see the example\n')
app.run(port=8000)