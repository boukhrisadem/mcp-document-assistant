# Agent Skills Notes

## What is an AI Agent
An AI agent is a system where an AI model can take actions, use tools, and complete multi-step tasks autonomously.

## Key Concepts

### Tool Use
- The AI receives a list of available tools
- It decides which tool to call based on the user query
- The result is sent back to the AI to continue reasoning

### Agentic Loop
1. User sends a query
2. AI decides to use a tool
3. Tool is executed
4. Result is returned to AI
5. AI either uses another tool or gives a final answer

### Stop Conditions
- finish_reason == "stop" — AI is done, gives final answer
- finish_reason == "tool_calls" — AI wants to call a tool

## Memory in Agents
- Agents have no memory between sessions by default
- Memory is simulated by passing the full conversation history each time
- messages list grows with each turn

## System Prompt
- Sets the behavior and personality of the agent
- Defined once at the start of the conversation
- Example: "You are a helpful assistant that answers questions using the provided tools."