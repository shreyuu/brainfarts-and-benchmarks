import itertools as it
import time

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# ══════════════════════════════════════════════════════════════════════════════
# Graph 1: Random Geometric Graph
# ══════════════════════════════════════════════════════════════════════════════

G1 = nx.random_geometric_graph(200, 0.125, seed=896803)
pos1 = nx.get_node_attributes(G1, "pos")

dmin = 1
ncenter = 0
for n in pos1:
    x, y = pos1[n]
    d = (x - 0.5) ** 2 + (y - 0.5) ** 2
    if d < dmin:
        ncenter = n
        dmin = d

p = nx.single_source_shortest_path_length(G1, ncenter)

# ══════════════════════════════════════════════════════════════════════════════
# Graph 2: Edge-Colored Complete Graph
# ══════════════════════════════════════════════════════════════════════════════

node_dist_to_color = {
    1: "tab:red",
    2: "tab:orange",
    3: "tab:olive",
    4: "tab:green",
    5: "tab:blue",
    6: "tab:purple",
}

nnodes = 13
G2 = nx.complete_graph(nnodes)

n = (nnodes - 1) // 2
ndist_iter = list(range(1, n + 1))
ndist_iter += ndist_iter[::-1]


def cycle(nlist, n):
    return nlist[-n:] + nlist[:-n]


nodes = list(G2.nodes())
for i, nd in enumerate(ndist_iter):
    for u, v in zip(nodes, cycle(nodes, i + 1)):
        G2[u][v]["color"] = node_dist_to_color[nd]

pos2 = nx.circular_layout(G2)

# ── Plot Graphs 1 & 2 side by side ──────────────────────────────────────────

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.set_title("Random Geometric Graph", fontsize=14)
nx.draw_networkx_edges(G1, pos1, alpha=0.4, ax=ax1)
nx.draw_networkx_nodes(
    G1,
    pos1,
    nodelist=list(p.keys()),
    node_size=80,
    node_color=list(p.values()),
    cmap="Reds_r",
    ax=ax1,
)
ax1.set_xlim(-0.05, 1.05)
ax1.set_ylim(-0.05, 1.05)
ax1.set_axis_off()

ax2.set_title("Edge-Colored Complete Graph (K13)", fontsize=14)
node_opts = {"node_size": 500, "node_color": "w", "edgecolors": "k", "linewidths": 2.0}
nx.draw_networkx_nodes(G2, pos2, ax=ax2, **node_opts)
nx.draw_networkx_labels(G2, pos2, font_size=14, ax=ax2)
edge_colors = [edgedata["color"] for _, _, edgedata in G2.edges(data=True)]
nx.draw_networkx_edges(G2, pos2, width=2.0, edge_color=edge_colors, ax=ax2)
ax2.set_axis_off()

fig1.tight_layout()

# ══════════════════════════════════════════════════════════════════════════════
# Graph 3: Spring Layout Method Comparison (force / energy / sfdp)
# ══════════════════════════════════════════════════════════════════════════════

negative_weight_graph = nx.complete_graph(4)
negative_weight_graph[0][2]["weight"] = -1

graphs = [
    (nx.grid_2d_graph(15, 15), "grid_2d"),
    (negative_weight_graph, "negative_weight"),
    (nx.gnp_random_graph(100, 0.005, seed=0), "gnp_random"),
]

fig2, axes = plt.subplots(3, 3, figsize=(9, 9))
colors = {"force": "tab:blue", "energy": "tab:orange", "sfdp": "tab:green"}

for i, (G, name) in enumerate(graphs):
    results = []

    t0 = time.perf_counter()
    pos = nx.spring_layout(G, method="force", seed=0)
    dt = time.perf_counter() - t0
    results.append(("force", pos, dt))

    t0 = time.perf_counter()
    pos = nx.spring_layout(G, method="energy", seed=0)
    dt = time.perf_counter() - t0
    results.append(("energy", pos, dt))

    t0 = time.perf_counter()
    pos = nx.nx_agraph.graphviz_layout(G, prog="sfdp")
    dt = time.perf_counter() - t0
    results.append(("sfdp", pos, dt))

    for j, (mname, pos, dt) in enumerate(results):
        nx.draw(G, pos=pos, ax=axes[j, i], node_color=colors[mname], node_size=20)
        title = (f"{name}\n" if j == 0 else "") + f"{dt:.2f}s"
        axes[j, i].set_title(title, fontsize=20)

handles = [mpatches.Patch(color=color, label=key) for key, color in colors.items()]
fig2.legend(handles=handles, loc="upper center", ncol=3, fontsize=25)

fig2.tight_layout(rect=(0, 0, 1, 0.9))

# ══════════════════════════════════════════════════════════════════════════════
# Graph 4: Labeled MultiDiGraph
# ══════════════════════════════════════════════════════════════════════════════


def draw_labeled_multigraph(G, attr_name, ax=None):
    """
    Length of connectionstyle must be at least that of a maximum number of edges
    between pair of nodes. This number is maximum one-sided connections
    for directed graph and maximum total connections for undirected graph.
    """
    connectionstyle = [f"arc3,rad={r}" for r in it.accumulate([0.15] * 4)]

    pos = nx.shell_layout(G)
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=20, ax=ax)
    nx.draw_networkx_edges(
        G, pos, edge_color="grey", connectionstyle=connectionstyle, ax=ax
    )

    labels = {
        tuple(edge): f"{attr_name}={attrs[attr_name]}"
        for *edge, attrs in G.edges(keys=True, data=True)
    }
    nx.draw_networkx_edge_labels(
        G,
        pos,
        labels,
        connectionstyle=connectionstyle,
        label_pos=0.3,
        font_color="blue",
        bbox={"alpha": 0},
        ax=ax,
    )


multi_nodes = "ABC"
prod = list(it.product(multi_nodes, repeat=2))
pair_dict = {f"Product x {i}": prod * i for i in range(1, 5)}

fig3, axes3 = plt.subplots(2, 2)
for (name, pairs), ax in zip(pair_dict.items(), np.ravel(axes3)):
    G = nx.MultiDiGraph()
    for i, (u, v) in enumerate(pairs):
        G.add_edge(u, v, w=round(i / 3, 2))
    draw_labeled_multigraph(G, "w", ax)
    ax.set_title(name)
fig3.tight_layout()

plt.show()
