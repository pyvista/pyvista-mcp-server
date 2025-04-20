from mcp import MCPServer
import pyvista as pv

# Initialize the MCP server
server = MCPServer()


@server.route("/render-sphere")
def render_sphere():
    # Create a PyVista sphere
    sphere = pv.Sphere()

    # Set up a plotter
    plotter = pv.Plotter()
    plotter.add_mesh(sphere, color="blue")
    plotter.show()


if __name__ == "__main__":
    # Start the MCP server
    server.run()
