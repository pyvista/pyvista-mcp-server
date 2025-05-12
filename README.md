# PyVista MCP Server

This repository contains a PyVista-based MCP (Model Context Protocol) server. It demonstrates the integration of PyVista for 3D visualization with MCP tools.

## Features

- **hello_world Tool**: A tool that generates and exports a 3x3 grid of 3D shapes (Cylinder, Arrow, Sphere, etc.) as an interactive HTML file.

## Output

The `hello_world` tool exports an HTML file named `a_basic.html` in the current working directory. Open this file in a web browser to view the interactive 3D visualization.

## Configuration

To configure the MCP server, use the following JSON structure in your settings:

```json
{
  "mcpServers": {
    "mcp-demo-server": {
      "disabled": false,
      "timeout": 600,
      "command": "<path-to-python-executable>",
      "args": ["<path-to-server-script>"],
      "transportType": "stdio"
    }
  }
}
```

This configuration specifies the command and arguments to run the MCP server, along with other settings like timeout and transport type.
