import sys
from collections import OrderedDict
from pprint import pprint

class Graph():
	def __init__(self, vertice):
		self.nodes = nodes
		self.visited = set()
		self.queue = {}

	def find_shortest_path(self, start, goal):

		curr_node = start
		adj_nodes = self.nodes[curr_node]

		for data in adj_nodes:
			node = data[0]
			dist = data[1]
			self.queue[node] = (dist, start)
		
		self.visited.add(start)
		print(self.queue)
		while True:
			node_data = list(sorted(self.queue.items(), key=lambda x: x[1][0]))[0]
			node_name = node_data[0]
			dist_to_node = node_data[1][0]
			path_to_node = node_data[1][1] + "-" + node_name

			self.queue.pop(node_name)
			self.visited.add(node_name)
			adj_nodes = self.nodes[node_name]


			if goal in [x[0] for x in adj_nodes]:
				node_data = [x for x in adj_nodes if goal in x[0]] 
				node_name = node_data[0][0]
				node_dist = node_data[0][1]
				print("Found with a distance of {}".format(dist_to_node + node_dist))
				print("Path to goal is {}-{}".format(path_to_node, node_name))
				break
			
			for node in adj_nodes:
				adj_node_name = node[0]
				dist_to_adj = node[1]

				total_dist = dist_to_node + dist_to_adj

				if adj_node_name not in self.visited:
					if adj_node_name in self.queue:
					 
					 if total_dist < self.queue.get(adj_node_name)[0]:
							self.queue[adj_node_name] = (total_dist, path_to_node)

					else:
						self.queue[adj_node_name] = (total_dist, path_to_node)

			print(self.queue)
nodes = OrderedDict({
	'1': [('13',7), ('2', 3), ('4', 4)],
	'2': [('1', 3), ('4', 4), ('13', 2), ('8', 1)],
	'3': [('13', 3), ('12', 2)],
	'4': [('1', 4), ('2', 4), ('6', 1)],
	'5': [('7', 2), ('11', 3)],
	'6': [('4', 5), ('8', 3)],
	'7': [('8', 2), ('5', 2)],
	'8': [('7', 2), ('2', 1), ('6', 3)],
	'11': [('9', 4), ('10', 4)],
	'12':[('3', 2), ('9', 4), ('10', 4)],
	'13':[('1', 7), ('2', 2), ('3', 3)]
})

graph = Graph(nodes)

graph.find_shortest_path('4', '9')