from graphviz import Digraph


with open('input.txt') as file:
    lines = []
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

marked_states = []
for state in states:
    if state in final_states:
        marked_states.append((1, (None, None)))
    else:
        marked_states.append((0, (None, None)))

# for i, state in enumerate(marked_states):
#     print(i, state)

old_len_unique = len(set(marked_states))

while True:
    classes = [(state, cl[0]) for state, cl in enumerate(marked_states)]

    for i, state in enumerate(marked_states):
        marked_states[i] = (state[0], (marked_states[by_zero[i]][0], marked_states[by_one[i]][0]))

    unique = list(set(marked_states))
    for i, state in enumerate(marked_states):
        marked_states[i] = (unique.index(state), (None, None))

    if len(unique) == old_len_unique:
        break

    old_len_unique = len(unique)

print(classes)

