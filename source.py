from graphviz import Digraph


with open('input.txt') as file:
    lines = list()
    states = list(range(int(file.readline())))
    for line in file.readlines():
        lines.append([int(i) for i in line.split()])
    final_states, by_zero, by_one = lines

initial = Digraph()
minimal = Digraph()

if 0 in final_states:
    initial.node(name='0', label='0', shape='doublecircle', style='filled', fillcolor='grey')
else:
    initial.node(name='0', label='0', shape='doublecircle')

for state in states[1:]:
    if state in final_states:
        initial.node(name=str(state), label=str(state), shape='circle', style='filled', fillcolor='grey')
    else:
        initial.node(name=str(state), label=str(state), shape='circle')

for tail, head in enumerate(by_zero):
    initial.edge(tail_name=str(tail), head_name=str(head), label='0')

for tail, head in enumerate(by_one):
    initial.edge(tail_name=str(tail), head_name=str(head), label='1')

# initial.render('test-output/initial_graph.gv', view=True, format='png')

classes = [
    [(state, []) for state in states if state not in final_states],
    final_states
]

print(classes)
