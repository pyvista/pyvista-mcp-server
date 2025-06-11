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
    radius: float = 0.5,
    center: Sequence[float] = (0.0, 0.0, 0.0),
    filename: Path = Path("sphere_mesh.vtk"),
) -> Path:
    """Create a sphere mesh and save it to a file.

    Parameters
    ----------
    radius : float, default: 0.5
        Sphere radius.

    center : sequence[float], default: (0.0, 0.0, 0.0)
        Center coordinate vector in ``[x, y, z]``.

    filename : Path, default: Path("sphere_mesh.vtk")
        Filename of mesh to be written.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    Returns
    -------
    Path
        The path to the output mesh file.
    """
    sphere = pv.Sphere(radius=radius, center=center)
    output_path = Path.cwd() / "sphere_mesh.vtk"
    sphere.save(output_path)
    return output_path


@mcp.tool()
def add(a: Path, b: Path) -> Path:
    """Add two mesh files together.

    Parameters
    ----------
    a : Path
        The first mesh file.

    b : Path
        The second mesh file.

    Returns
    -------
    Path
        The path to the output mesh file.
    """
    mesh_a = pv.read(a)
    mesh_b = pv.read(b)
    mesh_c = mesh_a + mesh_b
    output_path = Path.cwd() / "output_mesh.vtk"
    mesh_c.save(output_path)
    return output_path


if __name__ == "__main__":
    mcp.run(transport="stdio")
