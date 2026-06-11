from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers together
    Args:
        a: the first number
        b: the second number
    """
    return a + b

