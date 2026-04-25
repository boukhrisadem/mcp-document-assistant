## What I Built

This project uses MCP's three core primitives:

- **Tools** — `read_doc_contents`, `edit_document` — let Claude read and edit your documents
- **Resources** — `docs://documents` — exposes your documents collection to the agent
- **Prompts** — `summarize`, `format` — reusable workflows to summarize or reformat a document

I extended the MCP server (`mcp_server.py`) and MCP client (`mcp_client.py`) provided by the course — adding tools, resources, and prompts on top of the starter code. The CLI interface and agent loop (`core/`) were provided as part of the course scaffold.

## How It Works

1. You drop `.txt` or `.md` files into the `notes/` folder
2. You run the app and ask questions via the CLI
3. Claude uses MCP tools to read your documents and answer your questions

---

## Project Structure
mcp-document-assistant/
├── core/
│   ├── claude.py        # Anthropic API wrapper
│   ├── chat.py          # Agent loop
│   ├── cli.py           # CLI interface (course scaffold)
│   ├── cli_chat.py      # CLI chat handler
│   └── tools.py         # MCP tool execution
├── notes/               # Your documents go here (gitignored)
├── mcp_server.py        # MCP server — tools, resources, prompts
├── mcp_client.py        # MCP client — connects to the server
├── main.py              # Entry point
├── .env.example         # Environment variables template
├── pyproject.toml       # Project dependencies
└── README.md

---

## Setup

### Requirements
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager
- Anthropic API key — get one at [console.anthropic.com](https://console.anthropic.com)

### Installation

```bash
git clone https://github.com/boukhrisadem/mcp-document-assistant.git
cd mcp-document-assistant
uv sync
```

### Environment Variables

Create a `.env` file in the project root:
ANTHROPIC_API_KEY=your-api-key-here
CLAUDE_MODEL=claude-haiku-4-5-20251001
USE_UV=1

### Add Your Documents

Create a `notes/` folder and add your `.txt` or `.md` files:

```bash
mkdir notes
```

---

## Usage

```bash
uv run main.py
```

### Ask a question about a document

what are the key points? @mcp_notes.md


### Summarize a document

/summarize mcp_notes.md


### Format a document as Markdown

/format mcp_notes.md


### Exit

exit


---

## Tech Stack

- [MCP (Model Context Protocol)](https://modelcontextprotocol.io) — Anthropic's open protocol for AI tool use
- [Claude](https://anthropic.com) — Anthropic's AI model
- [FastMCP](https://github.com/jlowin/fastmcp) — Python framework for building MCP servers
- Python 3.13 / uv

---

## What I Learned

- How to build an MCP server with tools, resources, and prompts
- How Claude uses tool calling in an agentic loop
- How MCP clients connect to servers via stdio
- Managing async Python with `asyncio` and `AsyncExitStack`

---

## Author

**Adem Boukhris** — AI Engineering student