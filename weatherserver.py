from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")
@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather of location"""
    return f"It's always  raining in {location}"
# Stdio for local
# SSE for Server-Sent Events
# streamable-http for Web Protocol (Chunked Transfer)
if __name__== "__main__":
    mcp.run(transport="streamable-http")