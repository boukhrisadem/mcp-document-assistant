import os
from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("DocumentMCP", log_level="ERROR")

NOTES_DIR = "notes"


def get_docs() -> dict[str, str]:
    docs = {}
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
    for filename in os.listdir(NOTES_DIR):
        filepath = os.path.join(NOTES_DIR, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                docs[filename] = f.read()
    return docs


@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string"
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    docs = get_docs()
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]


@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the document content with a new string"
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace"),
    new_str: str = Field(description="The new text to insert in place of the old text")
):
    docs = get_docs()
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    updated_content = docs[doc_id].replace(old_str, new_str)
    filepath = os.path.join(NOTES_DIR, doc_id)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated_content)


@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(get_docs().keys())


@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    docs = get_docs()
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]


@mcp.prompt(
    name="format",
    description="Rewrites the contents of a document in Markdown format."
)
def format_document(
    doc_id=Field(description="Id of the document to format")
) -> list[base.Message]:
    
    docs = get_docs()
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    content = docs[doc_id]

    prompt = f"""Rewrite the contents of the document with id "{doc_id}" in clean Markdown format.
    Use appropriate headers, bullet points, bold text, and other Markdown elements where suitable.
    Return only the reformatted document content, nothing else.
    Document content:
    {content}
    """

    return [base.UserMessage(prompt)]


@mcp.prompt(
    name="summarize",
    description="Summarizes a document"
)
def summarize_document(
    doc_id=Field(description="Id of the document to summarize")
) -> list[base.Message]:
    docs = get_docs()
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    content = docs[doc_id]

    prompt = f"""Please read the document with id "{doc_id}" and provide a clear, concise summary.
    Include the main points, key findings, and any important conclusions.
    Keep the summary brief but informative.
    Document content:
    {content}
    """

    return [base.UserMessage(prompt)]


if __name__ == "__main__":
    mcp.run(transport="stdio")