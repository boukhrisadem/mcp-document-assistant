# Python Async Notes

## Why Async
- Allows code to pause and wait without blocking the entire program
- Essential for network requests, file I/O, and tool calls in MCP

## Key Keywords
- async def — defines a coroutine function
- await — pauses execution until the result is ready
- asyncio.run() — entry point to run async code

## AsyncExitStack
- Used to manage multiple async context managers
- enter_async_context() adds a new context
- Automatically cleans up all contexts on exit

## Common Patterns

### Running async code on Windows
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

### Async context manager
async with MCPClient(...) as client:
    result = await client.list_tools()

## Why MCP Uses Async
- MCP clients communicate with servers over stdio
- Waiting for server responses is I/O — perfect for async
- Multiple clients can be managed concurrently with AsyncExitStack