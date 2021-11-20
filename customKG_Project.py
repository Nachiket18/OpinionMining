from networkx.algorithms.efficiency_measures import efficiency
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib


#Summary of what I have done:
# I took a closer look at matplotlib and networkx for any customizations for the graph and so far it seems simple to.
# Networkx customizations is based on the IDs of the given nodes and the edges as well. I could easily implement a counter
# to set the sizes of the nodes and the edges based on the amount of positive/negative comments of the object. 
# However, it would take awhile to run since it'll be index based. I've been looking for another library to see if it can do the 
# same thing but more efficient else we can go with this as long as runtime for this isn't an issue. Below I have the code
# create a simple graph where the phone is the main subject and its features.

# Set overall figure size
f = plt.figure(figsize=(20,20))
f.tight_layout()

# Specify data and attributes
# relationships = pd.DataFrame({'from': ['A', 'A', 'A', '1', '2', '3', '1', 'Center', 'Center', 
#                                        'Center', 'Center', 'Center', 'Center', 'Center'], 
#                               'to': ['B', 'C', 'D', 'C', 'C', 'A', '3', '1', '3', '2', 'A', 'B', 
#                                      'C', 'D']})

relationships = pd.DataFrame({'from': ['phone', 'phone', 'phone', 'phone'], 
                              'to': ['screen', 'battery', 'software', 'durability']})

# Create DF for node characteristics
# carac = pd.DataFrame({'ID':['A', 'B', 'C', 'D', '1', '2', '3', 'Center'], 
#                       'type':['Letter','Letter', 'Letter', 'Letter', 'Number', 'Number', 
#                               'Number', 'Center']})

carac = pd.DataFrame({'ID':['phone', 'screen', 'battery', 'software', 'durability'], 
                      'type':['Object','Feature', 'Feature', 'Feature', 'Feature']})

# Create graph object
G = nx.from_pandas_edgelist(relationships, 'from', 'to', create_using=nx.Graph())

# Make types into categories
carac= carac.set_index('ID')
carac=carac.reindex(G.nodes())

carac['type']=pd.Categorical(carac['type'])
carac['type'].cat.codes

# Set node colors
cmap = matplotlib.colors.ListedColormap(['dodgerblue', 'lightgray', 'darkorange'])

# Set node sizes
node_sizes = [4000 if entry != 'Letter' else 1000 for entry in carac.type]

# Create Layouts

# Set edge colors
edge_colors = ['green', 'red', 'green', 'red']

# Set edge widths
edge_widths = [0.1, 1, 2, 3, 5]

# Subplot 1
plt.subplot(2, 2, 1)
nx.draw(G, with_labels=True, node_color=carac['type'].cat.codes, cmap=cmap, 
        node_size = node_sizes, width=edge_widths,edge_color=edge_colors)
plt.title('Spring Layout (Default)', fontsize=18)

# Subplot 2
# plt.subplot(2, 2, 2)
# nx.draw_random(G, with_labels=True, node_color=carac['type'].cat.codes, cmap=cmap, 
#                node_size = node_sizes, edgecolors='gray')
# plt.title('Random Layout', fontsize=18)

# # Subplot 3
# plt.subplot(2, 2, 3)
# nx.draw_shell(G, with_labels=True, node_color=carac['type'].cat.codes, cmap=cmap, 
#             node_size = node_sizes, edgecolors='gray')
# plt.title('Shell Layout', fontsize=18)

# # Subplot 4
# plt.subplot(2, 2, 4)
# nx.draw_spectral(G, with_labels=True, node_color=carac['type'].cat.codes, cmap=cmap, 
#             node_size = node_sizes, edgecolors='gray')
plt.title('Spectral Layout', fontsize=18)
plt.show()
plt.savefig('project.png')