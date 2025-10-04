[← Documentation Map](documentation-map.md)

Source: https://modelcontextprotocol.io/docs/getting-started/intro

# What is the Model Context Protocol (MCP)?

MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems.

Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.

Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

```mermaid
graph LR
    subgraph AI_GROUP ["AI applications"]
        direction TB
        A1["<b>AI assistants</b><br/>Claude, ChatGPT"]
        A2["<b>Chat interfaces</b><br/>Claude Desktop, LibreChat"]
        A3["<b>IDEs and code editors</b><br/>Claude Code, Goose"]
        A4["<b>Other AI applications</b><br/>5ire, Superinterface"]
    end
    
    %% Central MCP Protocol
    MCP["<b>MCP</b><br/>Model Context Protocol<br/><i>Open-source standard</i><br/><i>Like USB-C for AI apps</i>"]
    
    subgraph DATA_GROUP ["Data sources"]
        direction TB
        D1["<b>Data and file systems</b><br/>PostgreSQL, SQLite, GDrive<br/>Local files, databases"]
        D5["<b>Workflows</b><br/>Specialized prompts"]
    end
    
    subgraph TOOLS_GROUP ["Tools"]
        direction TB
        D2["<b>Development tools</b><br/>Git, Sentry, etc."]
        D3["<b>Productivity tools</b><br/>Slack, Google Maps, etc."]
        D4["<b>Search & calculation tools</b><br/>Search engines, calculators"]
    end
    
    %% Bidirectional connections from AI applications to MCP
    A1 <--> MCP
    A2 <--> MCP
    A3 <--> MCP
    A4 <--> MCP
    
    %% Bidirectional connections from MCP to data sources/tools
    MCP <--> D1
    MCP <--> D2
    MCP <--> D3
    MCP <--> D4
    MCP <--> D5
    
    %% Styling
    classDef aiApps fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef mcpCenter fill:#e1f5fe,stroke:#0277bd,stroke-width:3px
    classDef dataTools fill:#f9f9f9,stroke:#333,stroke-width:2px
    
    class A1,A2,A3,A4 aiApps
    class MCP mcpCenter
    class D1,D2,D3,D4,D5 dataTools
```

## What can MCP enable?

| Use Case | Tools Used | What Happens | Outcome |
|----------|-------------|--------------|---------|
| **Personal Assistant** | Google Calendar, Notion | Agents access data | More personalized AI |
| **Web Development** | Claude Code, Figma | Generate from design | Complete web app |
| **Enterprise Analysis** | Multiple org databases | Chatbots connect all | Data analysis via chat |
| **3D Manufacturing** | Blender, 3D printer | AI designs + prints | Physical 3D objects |

## Why does MCP matter?

Depending on where you sit in the ecosystem, MCP can have a range of benefits.

| Stakeholder | Current Pain | MCP Benefit | Result |
|-------------|--------------|-------------|--------|
| **Developers** | Complex AI integration | Reduces dev time/complexity | Faster AI app builds |
| **AI Applications** | Limited capabilities | Access to data/tools ecosystem | Enhanced user experience |
| **End Users** | Basic AI functionality | AI gets data access + actions | More capable AI assistants |

## Start Building

| Build What | Purpose | Details | Guide |
|------------|---------|---------|-------|
| **MCP Servers** | Expose your data/tools | Make resources available to AI | [Build Guide](docs/develop/build-server.md) |
| **MCP Clients** | Connect to servers | Apps that use MCP servers | [Build Guide](docs/develop/build-client.md) |

## Learn more

| Topic | What You'll Learn | Resource |
|-------|------------------|----------|
| **Core Concepts** | MCP architecture & how it works | [Architecture Guide](docs/learn/architecture.md) |
