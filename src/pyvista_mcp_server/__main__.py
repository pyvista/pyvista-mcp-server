from mcp import MCPServer  # type: ignore[import]
import pyvista as pv  # type: ignore[import]

# Initialize the MCP server
server = MCPServer()


@server.route("/render-sphere")  # type: ignore[misc]
def render_sphere() -> None:
    """
    Render a sphere using PyVista and return the rendered image.

    This function is called when the "/render-sphere" endpoint is accessed.
    """
    # Create a PyVista sphere
    sphere = pv.Sphere()

    # Set up a plotter
    plotter = pv.Plotter()
    plotter.add_mesh(sphere, color="blue")
    plotter.show()


if __name__ == "__main__":
    # Start the MCP server
    server.run()
