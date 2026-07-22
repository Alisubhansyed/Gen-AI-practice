from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")
@mcp.tool()
def add(a:int, b:int)->int:
    """_summary_
    Add two number
    """
    return a+b
@mcp.tool()
def multiple(a:int, b:int)->int:
    """Multiply two  numbers"""
    return a*b
# Stdio for local
# SSE for Server-Sent Events
# streamable-http for Web Protocol (Chunked Transfer)
if __name__== "__main__":
    mcp.run(transport="stdio")