import networkx as nx
import matplotlib.pyplot as plt
from SQLconnection import cursor, connection


def findDeadlocks(transNo):
    G = nx.DiGraph()
    cursor.execute(f'''
    SELECT *
    FROM (SELECT TOP {transNo} src_id, rsv_id FROM transactions2
        ORDER BY trans_date DESC ) as transactions
    WHERE src_id IS NOT NULL and rsv_id IS NOT NULL
    ''')
    arr = []
    for i in cursor:
        tupl = (i[0],i[1])
        arr.append(tupl)

    G.add_edges_from(arr)
    #pos = nx.spring_layout(G)
    #nx.draw_networkx_nodes(G, pos, node_size=500)
    #nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    #nx.draw_networkx_labels(G, pos)
    #plt.show()
    cycles = list(nx.simple_cycles(G))

    deadlocks = []
    deadlock = []
    for cycle in cycles:
        deadlock = []
        for src in cycle:
            for rsv in cycle:
                print(src, rsv)
                query=f'''SELECT trans_no FROM (SELECT TOP {transNo} * FROM transactions2
                ORDER BY trans_date DESC ) as transactions
                WHERE src_id = {str(src)} and rsv_id = {str(rsv)}'''
                cursor.execute(query)
                trans_no = cursor.fetchone()
                #row = cursor.fetchone()
                if trans_no :
                    deadlock.append(trans_no.trans_no)
        deadlocks.append(deadlock)

    return deadlocks
#findDeadlocks(15)

#print(deadlocks)


