# What is the Model Context Protocol (MCP)?

https://modelcontextprotocol.io/docs/getting-started/intro

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

* Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant.
* Claude Code can generate an entire web app using a Figma design.
* Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat.
* AI models can create 3D designs on Blender and print them out using a 3D printer.

## Why does MCP matter?

Depending on where you sit in the ecosystem, MCP can have a range of benefits.

* **Developers**: MCP reduces development time and complexity when building, or integrating with, an AI application or agent.
* **AI applications or agents**: MCP provides access to an ecosystem of data sources, tools and apps which will enhance capabilities and improve the end-user experience.
* **End-users**: MCP results in more capable AI applications or agents which can access your data and take actions on your behalf when necessary.

## Start Building

- [Build servers](docs/develop/build-server.md): Create MCP servers to expose your data and tools
- [Build clients](docs/develop/build-client.md): Develop applications that connect to MCP servers

## Learn more

- [Understand concepts](docs/learn/architecture.md): Learn the core concepts and architecture of MCP
