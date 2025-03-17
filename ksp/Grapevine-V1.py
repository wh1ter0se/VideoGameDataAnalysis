import graphviz as gv

dot = gv.Digraph('Grapvevine-V1')

dot.attr(fontname='Helvetica,Arial,sans-serif')
dot.attr(overlap='false')
# dot.attr(splines='curved')
dot.attr('node', fontname='Helvetica,Arial,sans-serif')
dot.attr('edge', fontname='Helvetica,Arial,sans-serif')
dot.attr(rankdir='LR')
dot.attr('node', fontsize='16', shape='ellipse')

dot.node('node0', label='<f0> 0x10ba8| <f1> other', shape='record', group='kerbin')


dot.view()