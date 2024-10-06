# Python `graph-tool` Module: Detailed Overview and Examples

The `graph-tool` module is a Python library for manipulation and statistical analysis of graphs (networks). It is designed to be fast and scalable, providing efficient algorithms for various graph operations and properties. The library leverages C++ for performance and provides a comprehensive API for Python users.

## Installation

To install `graph-tool`, you can use `pip`:

```sh
pip install graph-tool
```

Note: `graph-tool` has several dependencies and might require additional steps to install on some systems. For detailed installation instructions, refer to the [official documentation](https://graph-tool.skewed.de/download).

## Importing the `graph-tool` Module

```python
from graph_tool.all import *
```

## Creating and Manipulating Graphs

### Creating a Graph

#### Example

```python
from graph_tool.all import Graph

# Create a new directed graph
g = Graph(directed=True)
```

### Adding Vertices and Edges

#### Example

```python
# Add vertices
v1 = g.add_vertex()
v2 = g.add_vertex()

# Add an edge
e = g.add_edge(v1, v2)
```

### Accessing Vertices and Edges

#### Example

```python
# Iterate over vertices
for v in g.vertices():
    print(v)

# Iterate over edges
for e in g.edges():
    print(e)
```

## Properties

### Vertex and Edge Properties

#### Example

```python
# Add vertex property
vprop = g.new_vertex_property("string")
g.vp.name = vprop

# Set property values
g.vp.name[v1] = "Vertex 1"
g.vp.name[v2] = "Vertex 2"

# Add edge property
eprop = g.new_edge_property("int")
g.ep.weight = eprop

# Set property values
g.ep.weight[e] = 5
```

### Graph Properties

#### Example

```python
# Add graph property
gprop = g.new_graph_property("string")
g.gp.title = gprop

# Set property value
g.gp.title = "My Graph"
```

## Visualization

### Basic Plotting

#### Example

```python
from graph_tool.all import graph_draw

# Draw the graph
graph_draw(g, output_size=(400, 400), output="graph.png")
```

### Advanced Plotting

#### Example

```python
# Create a larger graph
g = Graph()
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
e1 = g.add_edge(v1, v2)
e2 = g.add_edge(v2, v3)

# Add properties
g.vp.size = g.new_vertex_property("double")
g.vp.size[v1] = 10
g.vp.size[v2] = 20
g.vp.size[v3] = 30

# Draw with custom properties
graph_draw(g, vertex_size=g.vp.size, output_size=(400, 400), output="graph_custom.png")
```

## Graph Algorithms

### Shortest Path

#### Example

```python
from graph_tool.all import shortest_path

# Create a graph
g = Graph()
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
e1 = g.add_edge(v1, v2)
e2 = g.add_edge(v2, v3)

# Calculate shortest path
dist, path = shortest_path(g, source=v1, target=v3)
print("Distance:", dist)
print("Path:", [int(v) for v in path])
```

### Clustering Coefficient

#### Example

```python
from graph_tool.all import global_clustering

# Create a graph
g = Graph()
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
e1 = g.add_edge(v1, v2)
e2 = g.add_edge(v2, v3)
e3 = g.add_edge(v3, v1)

# Calculate clustering coefficient
cc = global_clustering(g)
print("Global Clustering Coefficient:", cc)
```

### PageRank

#### Example

```python
from graph_tool.all import pagerank

# Create a graph
g = Graph(directed=True)
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
e1 = g.add_edge(v1, v2)
e2 = g.add_edge(v2, v3)
e3 = g.add_edge(v3, v1)

# Calculate PageRank
pr = pagerank(g)
for v in g.vertices():
    print(f"Vertex {int(v)}: {pr[v]}")
```

## Practical Examples

### Example 1: Social Network Analysis

```python
from graph_tool.all import Graph, graph_draw

# Create a graph
g = Graph()
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
v4 = g.add_vertex()
e1 = g.add_edge(v1, v2)
e2 = g.add_edge(v2, v3)
e3 = g.add_edge(v3, v4)
e4 = g.add_edge(v4, v1)

# Add vertex properties
g.vp.name = g.new_vertex_property("string")
g.vp.name[v1] = "Alice"
g.vp.name[v2] = "Bob"
g.vp.name[v3] = "Charlie"
g.vp.name[v4] = "Diana"

# Visualize the graph
graph_draw(g, vertex_text=g.vp.name, output_size=(400, 400), output="social_network.png")
```

### Example 2: Road Network Analysis

```python
from graph_tool.all import Graph, graph_draw

# Create a graph
g = Graph()
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
v4 = g.add_vertex()
e1 = g.add_edge(v1, v2)
e2 = g.add_edge(v2, v3)
e3 = g.add_edge(v3, v4)
e4 = g.add_edge(v4, v1)

# Add edge properties
g.ep.distance = g.new_edge_property("float")
g.ep.distance[e1] = 10.0
g.ep.distance[e2] = 20.0
g.ep.distance[e3] = 15.0
g.ep.distance[e4] = 25.0

# Visualize the graph
graph_draw(g, edge_text=g.ep.distance, output_size=(400, 400), output="road_network.png")
```

## Conclusion

The `graph-tool` module is a powerful library for graph manipulation and analysis in Python. It provides efficient algorithms and a flexible API for creating, modifying, and analyzing graphs. Whether you're working on social network analysis, road network analysis, or any other graph-related task, `graph-tool` offers the tools you need to perform your analysis effectively. By leveraging its advanced features and customization options, you can handle complex graph structures and derive meaningful insights from your data.