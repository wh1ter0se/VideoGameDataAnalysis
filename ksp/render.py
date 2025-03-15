from graphviz import Source

with open('ksp/Grapevine-V1.dot') as file:
    text_from_file = file.read()

src = Source(text_from_file)
src.render("ksp/Grapvevine-V1")