# MCP (Model Context Protocol) Notes

## What is MCP
Model Context Protocol is a standard that lets AI models like Claude connect to external tools, data sources, and workflows in a structured way.

## Three Primitives
- **Tools**: Actions the AI can perform (e.g. read a file, edit a document)
- **Resources**: Data the AI can read (e.g. docs://documents)
- **Prompts**: Reusable workflow templates users can trigger (e.g. summarize, format)

## MCP Server
- Built using FastMCP in Python
- Defines tools, resources, and prompts using decorators
- Runs via stdio transport

## MCP Client
- Connects to the server via stdio
- Can list tools, call tools, read resources, list prompts, get prompts
- Uses ClientSession from the mcp library

## Key Commands
- uv run mcp_server.py — starts the server
- uv run mcp_client.py — runs the client
- uv run main.py — runs the full app
- uv run mcp dev mcp_server.py — opens browser inspector

## How Tools Work
- Defined with @mcp.tool() decorator
- Take typed arguments using Field()
- Return a result that Claude can use

## How Resources Work
- Defined with @mcp.resource() decorator
- Identified by a URI like docs://documents
- Can return JSON or plain text

## How Prompts Work
- Defined with @mcp.prompt() decorator
- Return a list of messages (UserMessage or AssistantMessage)
- Used to trigger predefined workflows