from mcp.server.fastmcp import FastMCP
import pyvista as pv
from pathlib import Path
from typing import Sequence


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


@mcp.tool()
def sphere(
    filename: Path,
    radius: float = 0.5,
    center: Sequence[float] = (0.0, 0.0, 0.0),
) -> None:
    """Create a sphere mesh and save it to a file.

    Parameters
    ----------
    filename : Path
        Filename of mesh to be written.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    radius : float, default: 0.5
        Sphere radius.

    center : sequence[float], default: (0.0, 0.0, 0.0)
        Center coordinate vector in ``[x, y, z]``.

    """
    sphere = pv.Sphere(radius=radius, center=center)
    sphere.save(filename)


if __name__ == "__main__":
    mcp.run(transport="stdio")
