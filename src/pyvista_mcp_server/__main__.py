from mcp.server.fastmcp import FastMCP
import pyvista as pv
from pathlib import Path


mcp = FastMCP("Demo", debug=True)


@mcp.tool()
def hello_world() -> Path:
    """Hello world!"""
    cyl = pv.Cylinder()
    arrow = pv.Arrow()
    sphere = pv.Sphere()
    plane = pv.Plane()
    line = pv.Line()
    box = pv.Box()
    cone = pv.Cone()
    poly = pv.Polygon()
    disc = pv.Disc()
    p = pv.Plotter(shape=(3, 3))
    # Top row
    p.subplot(0, 0)
    p.add_mesh(cyl, color="tan", show_edges=True)
    p.subplot(0, 1)
    p.add_mesh(arrow, color="tan", show_edges=True)
    p.subplot(0, 2)
    p.add_mesh(sphere, color="tan", show_edges=True)
    # Middle row
    p.subplot(1, 0)
    p.add_mesh(plane, color="tan", show_edges=True)
    p.subplot(1, 1)
    p.add_mesh(line, color="tan", line_width=3)
    p.subplot(1, 2)
    p.add_mesh(box, color="tan", show_edges=True)
    # Bottom row
    p.subplot(2, 0)
    p.add_mesh(cone, color="tan", show_edges=True)
    p.subplot(2, 1)
    p.add_mesh(poly, color="tan", show_edges=True)
    p.subplot(2, 2)
    p.add_mesh(disc, color="tan", show_edges=True)
    # Render all of them
    # p.show()
    # Export this plotter as an interactive scene to a HTML file.
    p.export_html("a_basic.html")
    return Path.cwd() / "a_basic.html"


if __name__ == "__main__":
    mcp.run(transport="stdio")
