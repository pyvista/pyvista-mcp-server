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
    result = mesh - other_mesh
    result.save(save_filename)


@mcp.tool()
def boolean_union(
    filename: Path,
    other_filename: Path,
    save_filename: Path,
) -> None:
    """Perform a boolean union operation on two meshes.

    Parameters
    ----------
    filename : str, Path
        First mesh file to be read.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    other_filename : str, Path
        Second mesh file to be read.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    save_filename : str, Path
        Filename of mesh to be written.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    """
    mesh = pv.read(filename)
    other_mesh = pv.read(other_filename)
    result = mesh | other_mesh
    result.save(save_filename)


@mcp.tool()
def boolean_intersection(
    filename: Path,
    other_filename: Path,
    output_filename: Path,
) -> None:
    """Perform a boolean intersection of two meshes.

    Parameters
    ----------
    filename : path
        First mesh file to read.

    other_filename : path
        Second mesh file to read.

    output_filename : path
        Filename of mesh to be written.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    """
    mesh = pv.read(filename)
    other_mesh = pv.read(other_filename)
    result = mesh & other_mesh
    result.save(output_filename)


@mcp.tool()
def is_all_triangules(
    filename: Path,
) -> bool:
    """Return if all the faces of the :class:`pyvista.PolyData` are triangles.

    Parameters
    ----------
    filename : path
        Filename of mesh to be checked.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    Returns
    -------
    bool
        ``True`` if all the faces of the :class:`pyvista.PolyData`
        are triangles and does not contain any vertices or lines.

    """
    mesh = pv.read(filename)
    return mesh.is_all_triangles()


@mcp.tool()
def plot(
    filename: Path,
) -> None:
    """Plot a mesh in a PyVista plotter.

    Parameters
    ----------
    filename : path
        Filename of mesh to be plotted.  File type is inferred from
        the extension of the filename unless overridden with
        ftype.  Can be one of many of the supported  the following
        types (``'.ply'``, ``'.vtp'``, ``'.stl'``, ``'.vtk``, ``'.geo'``,
        ``'.obj'``, ``'.iv'``).

    Returns
    -------
    StringIO
        Returns the HTML as a StringIO object.

    """
    mesh = pv.read(filename)
    p = pv.Plotter()
    p.add_mesh(mesh, color="tan", show_edges=True)
    return p.export_html()


if __name__ == "__main__":
    mcp.run(transport="stdio")
