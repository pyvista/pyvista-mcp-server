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


@mcp.tool()
def cube(
    filename: Path,
    center: Sequence[float] = (0.0, 0.0, 0.0),
    x_length: float = 1.0,
    y_length: float = 1.0,
    z_length: float = 1.0,
) -> None:
    """Create a cube mesh and save it to a file.

    Parameters
    ----------
    filename : path
        Filename of mesh to be written.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    center : sequence[float], default: (0.0, 0.0, 0.0)
        Center in ``[x, y, z]``.

    x_length : float, default: 1.0
        Length of the cube in the x-direction.

    y_length : float, default: 1.0
        Length of the cube in the y-direction.

    z_length : float, default: 1.0
        Length of the cube in the z-direction.

    """
    cube = pv.Cube(
        center=center, x_length=x_length, y_length=y_length, z_length=z_length
    )
    cube.save(filename)


@mcp.tool()
def triangulate(
    filename: Path,
) -> None:
    """More complex polygons will be broken down into triangles.

    Parameters
    ----------
    filename : path
        Filename of mesh to be written.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    """
    mesh = pv.read(filename)
    mesh.triangulate().save(filename.with_suffix(".triangulated.vtk"))


@mcp.tool()
def boolian_difference(
    filename: Path,
    other_filename: Path,
    save_filename: Path,
) -> None:
    """Perform a boolean difference operation on two meshes.

    Parameters
    ----------
    filename : path
        Filename of mesh to be written.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    other_filename : path
        Second mesh to perform the boolean operation with.

    save_filename : path
        Output filename to save the result of the boolean operation.
    """
    mesh = pv.read(filename)
    other_mesh = pv.read(other_filename)
    result = mesh.boolean_difference(other_mesh)
    result.save(save_filename)


if __name__ == "__main__":
    mcp.run(transport="stdio")
