from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Demo", debug=True)


@mcp.tool()
def hello_world() -> str:
    """Hello world!"""
    return "Hello world!"


if __name__ == "__main__":
    mcp.run(transport="stdio")
