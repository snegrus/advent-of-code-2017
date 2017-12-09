import sys
import numpy
import hashlib

ARGUMETNS = sys.argv
if len(ARGUMETNS) != 2:
    sys.exit("Usage: one argument needed, the name of the input file")

graph = {}

def process_node(node_description):
    name = node_description[0]
    weight = int(node_description[1].strip('()'))
    children = []
    if len(node_description) > 2:
        children = [x.strip(',') for x in node_description[3:]]
    node = {
        "weight": weight,
        "children": children,
        "inbound": 0
    }
    graph[name] = node

def compute_inbound():
    for node in graph.itervalues():
        children = node["children"]
        for child in children:
            current_inbound_c = graph[child]["inbound"]
            graph[child]["inbound"] = current_inbound_c + 1

def get_root():
    for name, node in graph.iteritems():
        if node["inbound"] == 0:
            return name

def dfs_search(root):
    children = graph[root]["children"]
    weight = graph[root]["weight"]
    local_stats = {}
    for child in children:
        local_stats[child] = dfs_search(child)
    graph[root]["children_weight"] = sum(local_stats.itervalues())
    local_values = list(local_stats.itervalues())
    local_values.sort()
    if len(set(local_values)) > 1:
        expected_value = local_values[(len(local_values) + 1) / 2 - 1]
        wrong_value = 0
        print local_values
        if expected_value != local_values[0]:
            wrong_value = local_values[0]
        else:
            wrong_value = local_values[-1]
        for node in local_stats:
            if local_stats[node] == wrong_value:
                print expected_value - graph[node]["children_weight"]
                exit()
    return weight + sum(local_stats.itervalues())

INPUT_FILE_NAME = sys.argv[1]
with open(INPUT_FILE_NAME, "r") as input_file:
    for input_line in input_file:
        process_node(input_line.split())
    compute_inbound()
    root = get_root()
    dfs_search(root)
