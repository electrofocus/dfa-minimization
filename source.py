from graphviz import Digraph


with open('input.txt') as file:
    lines = list()
    n_states = int(file.readline())
    for line in file.readlines():
        lines.append(line.split())
    final_states, by_zero, by_one = lines

initial = Digraph()
minimal = Digraph()

for state in range(n_states):
    initial.node(name=str(state), label=str(state))

for tail, head in enumerate(by_zero):
    initial.edge(tail_name=str(tail), head_name=head, label='0')

for tail, head in enumerate(by_one):
    initial.edge(tail_name=str(tail), head_name=head, label='1')

initial.render('test-output/my_graph.gv', view=True, format='png')
