import nbformat
from nbconvert import SlidesExporter
from nbconvert.postprocessors import ServePostProcessor

with open("main.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

# Need to increase default slide width
exporter = SlidesExporter()
exporter.reveal_width = '"95%"'
exporter.reveal_theme = "white"

# Convert the notebook to slides HTML
body, resources = exporter.from_notebook_node(nb)

# Write output to a file
with open("slides.html", "w") as f:
    f.write(body)

serve_post = ServePostProcessor()
serve_post.port = 3000
serve_post.postprocess("slides.html")
# serve_post
