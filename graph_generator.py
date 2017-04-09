import networkx as nx
import pandas as pd
from networkx import draw
import matplotlib.pyplot as pyplot

indiv = 'STEVEN ROY WILLIAMSON'
l = ['JOSEPH RYAN STEMMLE:701', 'WILLIAM H SHIREY:4231', 'KEVIN D WILLIAMSON:7245', 'JOANN M STITH-MALONEY:1674', 'REBECCA E SHRINER:4231', 'BRAD AARON SWARTZWELDER:4231', 'BIVAS KANTI GHOSH:5327', 'KEVIN ALEXANDER MAUTTE:1006', 'JEFFREY NORMAN JONES:4231', 'ROBERT EUGENE SCHINSKY:4415', 'JONATHAN CHRISTOPHER WOOD:4109', 'SAMANTHA COLLIER WOOTON:4019', 'VICTOR MICHAEL DI VITTORIO:4231', 'JOHN BRADFORD SCOTT:4231', 'JEFF WAYNE ROHR:4231', 'CESAR R E MOREL:4231', 'PETER ANTONY MAROTTA:4231']
b = l[0:10]
print(a)

G = nx.Graph()
G.add_node(indiv)
for i in b:
    print(i.split(':'))
    a = i.split(':')
    G.add_node(a[0])
    #G.add_edge(indiv,a[0])
    print(int(a[1]))
    G.add_weighted_edges_from([(indiv,a[0],a[1])])
#G.add_weighted_edges_from()
G.nodes()

#import networkx as nx
#import matplotlib.pyplot as plt
#g1 = nx.petersen_graph()
pos = nx.spring_layout(G,k=5)
nx.draw(G,with_labels=1,font_size=8)
plt.show()
plt.savefig('test.png')