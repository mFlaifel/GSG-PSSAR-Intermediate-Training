# Lesson 04 — Using AI as a Developer

> **Phase 1 — Foundations | Duration: 2 Hours | Updated: June 2026**
> **Level:** Beginner-Intermediate | **Prerequisites:** Lessons 01–03

---

## ⏱️ Session Roadmap (2 Hours)

| Block      | Time        | Topic                                          |
| ---------- | ----------- | ---------------------------------------------- |
| 🟦 Block 1 | 0:00 – 0:20 | Why AI matters + The modern AI ecosystem       |
| 🟩 Block 2 | 0:20 – 0:45 | How LLMs work + Context windows + Agents       |
| 🟨 Block 3 | 0:45 – 1:10 | Prompt engineering + Real workflows            |
| 🟥 Block 4 | 1:10 – 1:35 | Security, ethics, and dangers of over-reliance |
| ✅ Block 5 | 1:35 – 2:00 | Hands-on exercise + Summary + Q&A              |

---

## 🟦 Block 1 — Why This Lesson Matters (20 min)

### AI in 2026 Is Not Optional

In 2026, AI is no longer just autocomplete. It is a core part of how professional developers work.

A developer who ignores AI tools is like a developer who refuses to use version control.

But there is a real danger on the other side:

> **Developers who use AI without understanding fundamentals build fragile systems they cannot maintain, debug, or explain.**

This lesson teaches you to use AI **professionally, safely, and critically.**

[AI Layoff in 2026](https://chatgpt.com/share/6a11aec2-92d4-83e9-a9a7-dba4a6bd71a3)
[clickup layoff](https://americanbazaaronline.com/2026/05/22/clickup-cuts-22-workforce-as-ceo-zeb-evans-pushes-ai-first-strategy-481410/)

---

### What Modern AI Can Do

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI Developer Capabilities (2026)             │
├─────────────────┬───────────────────────────────────────────────┤
│  Write Code     │  Generate functions, classes, entire modules  │
│  Debug          │  Analyze errors, stack traces, suggest fixes  │
│  Explain        │  Break down concepts step-by-step             │
│  Refactor       │  Clean up and improve existing code           │
│  Test           │  Generate unit tests and edge cases           │
│  Document       │  Write README files, docstrings, API docs     │
│  Review         │  Check for security flaws and style issues    │
│  Act (Agents)   │  Run terminals, browse the web, modify files  │
└─────────────────┴───────────────────────────────────────────────┘
```

---

### The AI Developer Ecosystem (2026)

```
                    ┌─────────────────────────┐
                    │     AI TOOLS FOR DEVS   │
                    └──────────┬──────────────┘
                               │
            ┌──────────────────┼───────────────────┐
            ▼                  ▼                    ▼
   ┌─────────────────┐  ┌────────────────┐  ┌────────────────┐
   │  Chat Assistants│  │ IDE Assistants │  │   AI Agents    │
   │                 │  │                │  │                │
   │ • ChatGPT       │  │ • GitHub       │  │ • Claude Code  │
   │ • Claude        │  │   Copilot      │  │ • Devin        │
   │ • Gemini        │  │ • Cursor       │  │ • Cursor Agent │
   │ • Perplexity    │  │ • Windsurf     │  │ • Windsurf     │
   │                 │  │ • JetBrains AI │  │   Cascade      │
   └─────────────────┘  └────────────────┘  └────────────────┘
   Explain, debug,       Inline suggestions,  Multi-step tasks,
   architecture          autocomplete, tests  tool use, autonomy
```

#### Quick Comparison

| Tool Type       | Best For                           | Use When                          |
| --------------- | ---------------------------------- | --------------------------------- |
| Chat Assistants | Learning, explaining, architecture | You need to understand something  |
| IDE Assistants  | Writing code faster                | You are actively coding           |
| AI Agents       | Complex multi-step tasks           | You want AI to execute a workflow |

---

## 🟩 Block 2 — How AI Models Actually Work (25 min)

### What Is an LLM?

An **LLM (Large Language Model)** is a neural network trained to predict the next token in a sequence.

```
Input text ──► Tokenizer ──► Token IDs ──► Model ──► Next Token ──► Output
  "def greet"    splits        [1234,         LLM       "("          "def greet("
                 into           5678]
                 tokens
```

**A [token](https://tokenizer.model.box/?model=gpt-4o) is roughly:**

- A common word (`def`, `for`, `if`)
- Part of a longer word (`program` → `pro` + `gram`)
- Punctuation or code symbols

The model does **NOT**:

- Understand code like a compiler does
- Verify that its output is correct
- Know the current date or live data
- Execute logic while generating text

It **predicts statistically likely text** based on training patterns.

<details>
<summary>try this</summary>

ask deepseek and chatgpt

```
what happened on June 4, 1989 at tiananmen square?
```

</details>

<summary>

## </summary>

### Why AI Sometimes Gets It Wrong

This is called **hallucination** — the model generates confident but incorrect output.

```
┌─────────────────────────────────────────────────────┐
│                  HALLUCINATION TYPES                │
├─────────────────────────────────────────────────────┤
│ 🔴 Invented APIs     │ Calls functions that don't   │
│                      │ exist in the real library    │
├─────────────────────────────────────────────────────┤
│ 🔴 Outdated Syntax   │ Uses old library versions    │
│                      │ or deprecated methods        │
├─────────────────────────────────────────────────────┤
│ 🔴 Confident Errors  │ Gives wrong answer with      │
│                      │ full confidence              │
├─────────────────────────────────────────────────────┤
│ 🔴 Insecure Code     │ Generates SQL injection,     │
│                      │ weak passwords, bad crypto   │
└─────────────────────────────────────────────────────┘
```

> ⚠️ **Hallucination is not a bug to be fixed. It is a fundamental property of how these models work. Always verify critical output.**

### Context Windows

The **context window** is the maximum amount of text a model can process in one request — including your question, its response, and any files you share.

```
┌─────────────────────────────────────────────────────┐
│                    CONTEXT WINDOW                   │
│                                                     │
│   Your Prompt   +   Files/Code   +   AI Response   │
│   ───────────────────────────────────────────────  │
│   ◄──────────────────────────────────────────────► │
│            Total tokens must fit inside             │
└─────────────────────────────────────────────────────┘
```

Modern models (2026) support **very large** context windows — up to hundreds of thousands of tokens. But:

> More context does NOT always mean better reasoning. Provide only what is relevant.

![lost in middle](https://www.damiangalarza.com/images/posts/lost-in-the-middle.png)

- [optimal coding length](https://chatgpt.com/share/6a11d25f-e060-83ea-9748-8e8c4c33c116)

---

### AI Agents — The Big Change Since 2024

Traditional AI answered questions. **Modern AI agents perform workflows.**

```
Traditional AI:                    AI Agent:

User: "Write a login route"        User: "Add authentication to my project"
                                        │
AI: [returns code]                      ▼
                                   Agent: Reads your project files
                                        │
                                        ▼
                                   Agent: Plans the changes needed
                                        │
                                        ▼
                                   Agent: Writes the code
                                        │
                                        ▼
                                   Agent: Runs tests
                                        │
                                        ▼
                                   Agent: Reports back
```

An agent can:

- Read your files
- Run terminal commands
- Browse documentation
- Modify your project
- Retry after failure

Examples: **Claude Code**, **Cursor Agent**, **Devin**, **Windsurf Cascade**

---

### MCP — The Protocol Behind AI Tool Integration

**MCP (Model Context Protocol)** allows AI systems to connect to external tools and data.

Think of it as:

> **"USB for AI tools"**

```
                      ┌─────────────┐
                      │   AI Model  │
                      └──────┬──────┘
                             │  MCP Protocol
          ┌──────────────────┼───────────────────┐
          ▼                  ▼                    ▼
   ┌─────────────┐   ┌──────────────┐   ┌──────────────┐
   │   GitHub    │   │   Database   │   │ File System  │
   └─────────────┘   └──────────────┘   └──────────────┘
          ▼                  ▼                    ▼
   ┌─────────────┐   ┌──────────────┐   ┌──────────────┐
   │  Your Docs  │   │   APIs       │   │ Company Tools│
   └─────────────┘   └──────────────┘   └──────────────┘
```

MCP is why AI assistants in 2026 can work with your real project data.

---

### RAG — How AI Stays Up to Date

**RAG (Retrieval-Augmented Generation)** allows AI to search documents before generating a response.

```
Without RAG:                    With RAG:

User asks question              User asks question
      │                               │
      ▼                               ▼
Model uses only                 System searches
training data                   your documents
(may be outdated)                     │
      │                               ▼
      ▼                         Relevant chunks
Model answers                   injected into prompt
                                      │
                                      ▼
                                Model answers using
                                fresh, specific data
```

RAG is used in enterprise AI tools, documentation assistants, and customer support systems.

---

## 🟨 Block 3 — Using AI Effectively (25 min)

### The Core Skill: Prompt Engineering

**Prompt quality directly determines output quality.**

#### Anatomy of a Strong Development Prompt

```
┌──────────────────────────────────────────────────────────┐
│                  STRONG PROMPT STRUCTURE                 │
├──────────────────────────────────────────────────────────┤
│  1. CONTEXT     What language, framework, environment?   │
│  2. GOAL        What exactly should this code do?        │
│  3. CONSTRAINTS Flask/SQLite/bcrypt, no globals, etc.    │
│  4. I/O         What goes in? What comes out?            │
│  5. EDGE CASES  Empty input, invalid data, errors?       │
│  6. EXAMPLE     Show a sample input and expected output  │
└──────────────────────────────────────────────────────────┘
```

---

#### Prompt Comparison: Weak vs. Strong

**❌ Weak Prompt:**

```
Write a Python login system
```

Problems: No framework, no security requirements, no database, no error handling.

---

**✅ Strong Prompt:**

```
Build a Flask login endpoint.

Requirements:
- Use Flask and SQLite
- Hash passwords with bcrypt
- Use parameterized SQL queries (no string concatenation)
- Return JSON responses with proper HTTP status codes
- Handle: empty username, missing password, duplicate accounts
- Include type hints and docstrings
- Do not use global variables

Input: { "username": "ali", "password": "secure123" }
Output (success): { "status": "ok", "token": "..." }
Output (fail): { "status": "error", "message": "Invalid credentials" }
```

The second prompt produces dramatically safer, production-quality code.

---

### 5 High-Value AI Workflows

#### Workflow 1 — Learning (Use AI to build skill, not bypass it)

```
Step 1: Ask AI to explain the concept
        │
        ▼
Step 2: Implement it yourself (without AI)
        │
        ▼
Step 3: Ask AI to review your implementation
        │
        ▼
Step 4: Compare and understand the differences
```

> 🎯 Goal: AI accelerates learning. You still write the code.

---

#### Workflow 2 — Debugging

Provide the full context:

```
Error: TypeError: Object of type User is not JSON serializable

Expected behavior:
  GET /api/user/1 → returns { "id": 1, "name": "Ali" }

Actual behavior:
  Returns 500 Internal Server Error

Stack trace:
  [paste full traceback here]

Relevant code:
  [paste the route function here]

Explain the root cause and show the fix.
```

---

#### Workflow 3 — Code Review

```
Review this Python function for:
- Security vulnerabilities
- Performance issues
- Readability and naming
- Missing edge cases
- Python best practices (PEP 8)

[paste your function here]
```

---

#### Workflow 4 — Test Generation

Ask AI to generate:

- Unit tests for individual functions
- Integration tests for full flows
- Edge case tests (empty input, wrong types, boundary values)
- Mock objects for external dependencies

---

#### Workflow 5 — Documentation

AI can draft:

- README files
- Function docstrings
- API endpoint documentation
- Architecture summaries

> ⚠️ Always review AI-generated documentation. It may describe code incorrectly.

---

### Trust Matrix — When to Use AI Output Directly

```
┌──────────────────────────┬─────────────────────────────┐
│    HIGH TRUST ✅          │    MUST VERIFY CAREFULLY ⚠️  │
├──────────────────────────┼─────────────────────────────┤
│ Boilerplate code         │ Authentication systems       │
│ Regex patterns           │ Payment and billing logic    │
│ Test scaffolding         │ Database queries (raw SQL)   │
│ Docstring drafts         │ Cryptography implementations │
│ Explaining common APIs   │ Medical/legal software       │
│ Reformatting/refactoring │ Production infrastructure    │
│ Markdown/README drafts   │ New framework APIs           │
└──────────────────────────┴─────────────────────────────┘
```

---

## 🟥 Block 4 — Security, Ethics, and Dangers (25 min)

### AI-Generated Code Has Real Security Risks

AI models were trained on millions of open source repositories — including **insecure code**. They can generate dangerous patterns confidently.

#### Example: SQL Injection

```python
# ❌ DANGEROUS — AI may generate this
# Vulnerable to SQL injection attacks
query = f"SELECT * FROM users WHERE name = '{username}'"
cursor.execute(query)

# If username = "' OR '1'='1"
# The query becomes: SELECT * FROM users WHERE name = '' OR '1'='1'
# This returns ALL users — a serious security breach
```

```python
# ✅ CORRECT — Always use parameterized queries
cursor.execute(
    "SELECT * FROM users WHERE name = ?",
    (username,)
)
# The ? placeholder safely separates data from SQL logic
```

#### Common AI Security Mistakes

```
┌────────────────────────────────────────────────────────┐
│           SECURITY RISKS IN AI-GENERATED CODE          │
├────────────────────────────────────────────────────────┤
│ 🔴 SQL Injection       │ String formatting in queries  │
│ 🔴 Hardcoded Secrets   │ API keys in source code       │
│ 🔴 Weak Passwords      │ MD5 instead of bcrypt         │
│ 🔴 Insecure Auth       │ Missing token validation      │
│ 🔴 Path Traversal      │ Unsanitized file paths        │
│ 🔴 Exposed Debug Info  │ Stack traces in responses     │
└────────────────────────────────────────────────────────┘
```

> 🔑 **AI does not replace security knowledge. It gives you code that looks correct but may be dangerous.**

---

### Privacy: Never Paste This Into Public AI Tools

```
❌ NEVER share with public AI tools:
   • API keys and secrets
   • Passwords and tokens
   • Customer personal data
   • Medical or legal records
   • Proprietary source code
   • Database connection strings
   • Company financial data
```

Some organizations have policies **completely prohibiting** use of public AI tools with internal data. Always follow your organization's guidelines.

---

### The Biggest Danger: Skill Atrophy

```
The Dependency Trap:

Student copies AI code ──► Doesn't understand it
        │
        ▼
Submits code that works in one case
        │
        ▼
Bug appears in production
        │
        ▼
Cannot debug because they never understood the code
        │
        ▼
Pastes error into AI again ──► Gets another fix they don't understand
        │
        ▼
Cycle continues → No real skills developed
```

**Use AI to learn, not to avoid learning.**

---

### Academic and Professional Ethics

| ✅ Ethical Use                   | ❌ Unethical Use                             |
| -------------------------------- | -------------------------------------------- |
| Ask AI to explain a concept      | Submit work you cannot explain               |
| Use AI to review your code       | Use AI to fake understanding                 |
| Generate tests for your function | Claim AI work as your own without disclosure |
| Debug with AI assistance         | Bypass assignments to avoid learning         |
| Use AI to explore new topics     | Violate organizational AI policies           |

---

## ✅ Block 5 — Hands-On Exercise + Summary (25 min)

### Practical Exercise: Prompt Refinement Lab

**Goal:** Build a function that analyzes log files.

---

**Round 1 — Bad Prompt (write this on board):**

```
Write a log parser.
```

❌ Too vague. What logs? What output? What format?

---

**Round 2 — Better Prompt:**

```
Write a Python function that counts log severity levels.
```

Better, but still missing: file path, format, return type, error handling.

---

**Round 3 — Strong Prompt (the goal):**

```
Write a Python function with this signature:

    def count_log_levels(filepath: str) -> dict[str, int]

Requirements:
- Read file line-by-line (must handle files > 1GB)
- Parse severity from tags: [INFO], [WARNING], [ERROR]
- Ignore lines that don't match the format
- Return uppercase severity counts
- Raise FileNotFoundError if file doesn't exist
- Add type hints and a docstring

Example input (log.txt):
  2026-06-01 [ERROR] Database connection failed
  2026-06-01 [INFO] Server started on port 5000
  2026-06-01 [WARNING] Memory usage above 80%
  2026-06-01 [INFO] Request handled

Expected output:
  { "ERROR": 1, "INFO": 2, "WARNING": 1 }
```

**Exercise Steps:**

1. Give Round 1 prompt to an AI tool — note the quality of output
2. Give Round 3 prompt — compare the difference
3. Identify one security or edge case issue in the generated code
4. Fix it yourself

---

### Key Vocabulary Reference

| Term                   | Definition                                                         |
| ---------------------- | ------------------------------------------------------------------ |
| **LLM**                | Large Language Model — neural network trained to predict text      |
| **Token**              | Small text unit (word, part-word, symbol) processed by the model   |
| **Context Window**     | Maximum text a model can process in one request                    |
| **Hallucination**      | Confident but incorrect AI output — a natural property of LLMs     |
| **Prompt Engineering** | Crafting inputs to get better, more reliable outputs               |
| **Agentic AI**         | AI that plans, uses tools, and executes multi-step workflows       |
| **MCP**                | Model Context Protocol — connects AI systems to external tools     |
| **RAG**                | Retrieval-Augmented Generation — AI searches docs before answering |
| **Fine-Tuning**        | Training a base model further on specialized data                  |
| **SQL Injection**      | Attack where malicious SQL is inserted via unsanitized input       |

---

### Lesson Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    LESSON 04 SUMMARY                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✅ AI is a core part of professional development in 2026   │
│  ✅ LLMs predict text — they don't understand or verify     │
│  ✅ Hallucination is real — always review AI output         │
│  ✅ Agents can plan and execute multi-step tasks            │
│  ✅ MCP connects AI to real tools and data                  │
│  ✅ Strong prompts produce dramatically better results      │
│  ✅ Never trust AI for security-critical code blindly       │
│  ✅ Never share private data with public AI tools           │
│  ✅ Use AI to build skill — not to replace learning         │
│  ✅ The best developers use AI as a multiplier              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Recommended Follow-Up Activities

1. Ask Claude or ChatGPT to explain **binary search** in plain English
2. Implement binary search yourself **without AI help**
3. Ask AI to review your implementation and suggest improvements
4. Use GitHub Copilot or Cursor to generate unit tests for a function you wrote
5. Find and identify one security issue in AI-generated code
6. Read the OWASP Top 10 list — understand the most common web vulnerabilities

---

### Further Reading

- [Anthropic Claude Documentation](https://docs.anthropic.com)
- [OpenAI Developer Documentation](https://platform.openai.com/docs)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io)
- [Prompt Engineering Guide](https://www.promptingguide.ai)
- [OWASP Top 10 Security Risks](https://owasp.org/Top10)
- [Cursor Documentation](https://docs.cursor.com)
- [Prompt Engineering](https://drive.google.com/file/d/1ADc-526c7F42reuF6lKAEtGUy6X-kylH/view)

---

_Updated: June 2026 | Phase 1 — Foundations | Lesson 04 of 20_
_Next: Lesson 05 — Python Setup & First Steps_
