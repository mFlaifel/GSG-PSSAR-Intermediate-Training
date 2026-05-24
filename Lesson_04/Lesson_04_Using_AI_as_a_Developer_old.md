# Lesson 04 — Using AI as a Developer

> **Phase 1 — Foundations | Duration: 2 hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Use GitHub Copilot, Claude, and ChatGPT effectively as development tools
- Write high-quality prompts that produce accurate, production-relevant code
- Critically evaluate AI-generated code for correctness, security, and maintainability
- Understand the technical limitations of current LLMs and where they fail
- Apply ethical guidelines for AI use in professional development contexts

---

## 1. AI Tools in the Modern Developer Workflow

AI coding assistants have changed what's possible for individual developers. Tasks that previously required hours of research, boilerplate writing, or trial-and-error can now be accelerated significantly.

But acceleration amplifies both skill and ignorance. An experienced developer uses AI to move faster. A developer without a strong foundation uses AI to produce code they cannot understand, debug, or maintain.

> **AI tools raise the floor for beginners and raise the ceiling for experts. They do not replace the need to understand what you're building.**

### The Main Tools

| Tool | Type | Primary Strength | Best For |
|---|---|---|---|
| **GitHub Copilot** | IDE-integrated autocomplete | Context-aware in-editor suggestions | Boilerplate, function completion, inline code |
| **Claude** | Conversational AI | Long-context reasoning, explanations, analysis | Architecture decisions, code review, debugging complex logic |
| **ChatGPT (GPT-4o)** | Conversational AI | Broad knowledge, creative suggestions | Exploration, learning new concepts, drafting |

These are complementary, not interchangeable. Using the right tool for the right task matters.

---

## 2. How Large Language Models (LLMs) Actually Work

Understanding the underlying mechanics prevents misuse and calibrates expectations.

### What LLMs Are

LLMs are neural networks trained to **predict the next token** (roughly, the next word or subword) given a sequence of previous tokens. They are trained on massive datasets of text — including code — and learn statistical patterns about what text tends to follow what.

They are **not**:
- Databases (they don't "look up" facts — they generate them probabilistically)
- Reasoning engines (they simulate reasoning via learned patterns)
- Compilers (they don't execute or test code during generation)

They **are**:
- Pattern-matching systems with extraordinary breadth
- Context-sensitive text generators
- Probabilistic — the same prompt can produce different outputs
- Capable of being confidently wrong (hallucination)

### The Hallucination Problem

Because LLMs predict statistically plausible text, they will generate:
- **Non-existent library functions** (e.g., `pandas.read_sql_smart()`)
- **Outdated API signatures** that changed in recent versions
- **Subtly incorrect logic** that looks syntactically correct
- **Fabricated citations** (less relevant for code, but relevant for research)

This is not a bug that will be "fixed" — it is intrinsic to how these models work. The mitigation is **you**: a developer who understands the domain enough to spot the error.

### Context Windows

Every conversation with an AI model operates within a **context window** — a maximum number of tokens the model can consider at once. Beyond this window, the model has no memory of earlier content.

| Model | Context Window (approximate) |
|---|---|
| GPT-4o | 128K tokens (~96,000 words) |
| Claude Sonnet | 200K tokens (~150,000 words) |
| Copilot (in-editor) | Surrounding file + related files |

For long codebases, paste only the **relevant portions** plus sufficient context for the model to reason correctly.

---

## 3. GitHub Copilot — In-Editor Intelligence

### How It Works

Copilot uses your current file, surrounding context, and (in recent versions) related open files to suggest completions. It's most effective when:

- Your function name and parameters clearly communicate intent
- You've written a descriptive comment explaining what the function should do
- The code pattern you need is common in its training data

### Getting Good Suggestions

**Technique 1: Write intent before implementation**
```python
# Convert a list of transaction dictionaries to a CSV string
# Each row: date, description, amount (formatted as currency)
# Sort by date ascending
def transactions_to_csv(transactions: list[dict]) -> str:
    # Copilot will suggest the implementation here
```

**Technique 2: Provide type hints**
Type annotations dramatically improve suggestion quality — Copilot uses them to understand data shapes.

```python
# Vague — poor suggestions
def process(data):
    ...

# Clear — much better suggestions
def calculate_portfolio_return(
    holdings: dict[str, float],   # ticker: quantity
    prices: dict[str, float],      # ticker: current price
    cost_basis: dict[str, float]   # ticker: purchase price
) -> dict[str, float]:             # ticker: return percentage
    ...
```

**Technique 3: Complete the first line**
Copilot often gets "unstuck" if you write the first meaningful line of implementation and let it continue:

```python
def find_most_common(items: list) -> any:
    from collections import Counter
    # Copilot takes over here with a good suggestion
```

### What Copilot Gets Wrong

- **Security vulnerabilities**: Copilot has been shown to suggest insecure patterns (SQL injection-prone queries, weak cryptography, hardcoded credentials) because such patterns exist in its training data
- **Subtle algorithmic errors**: It will confidently produce code with off-by-one errors or incorrect boundary conditions
- **Deprecated APIs**: Suggestions for libraries it was trained on before major version changes

**Never commit Copilot output without reviewing it** the same way you'd review code from a junior developer.

---

## 4. Prompt Engineering for Code — Claude and ChatGPT

Unlike Copilot, conversational AI tools require you to construct prompts deliberately. The quality of your output is directly proportional to the quality of your input.

### The Anatomy of a High-Quality Code Prompt

A strong code prompt includes:

1. **Context** — what system/application is this for?
2. **Task** — what specifically needs to be built or fixed?
3. **Constraints** — language, framework, version, performance requirements
4. **Input/output specification** — what does the function receive and return?
5. **Edge cases** — what unusual inputs must be handled?
6. **Examples** — sample inputs and expected outputs

### Prompt Quality Examples

**Weak Prompt:**
```
Write a function to validate email addresses in Python
```

**Problems:** No context about what "validate" means (format only? or MX record check?), no error handling requirements, no output format specified.

**Strong Prompt:**
```
Write a Python function to validate email addresses with the following requirements:

Context: This will be used in a user registration API endpoint.

Function signature:
    def validate_email(email: str) -> tuple[bool, str]:
        # Returns (is_valid, error_message)
        # error_message is empty string if valid

Validation rules:
1. Must contain exactly one @ symbol
2. Local part (before @) must be 1-64 characters, alphanumeric + . _ -
3. Domain must have at least one dot, TLD must be 2-6 alpha characters
4. No consecutive dots allowed anywhere
5. Must not start or end with a dot or hyphen

Edge cases to handle:
- Empty string → (False, "Email cannot be empty")
- No @ symbol → (False, "Invalid email format")
- Multiple @ symbols → (False, "Invalid email format")

Do NOT use external libraries. Use only Python's re module.

Examples:
- "user@example.com" → (True, "")
- "user..name@example.com" → (False, "Consecutive dots not allowed")
- "@nodomain.com" → (False, "Invalid email format")
```

The second prompt eliminates ambiguity, gives the model everything it needs, and sets clear expectations.

### Prompt Patterns for Developers

**Pattern 1: The Explainer**
```
Explain what this code does, then identify any bugs or inefficiencies:

[paste code]

Explain as if talking to a senior developer, not a beginner.
```

**Pattern 2: The Reviewer**
```
Review this Python function for:
1. Correctness — does it handle all edge cases?
2. Security — are there any injection or overflow risks?
3. Performance — are there any O(n²) operations that could be O(n)?
4. Readability — does it follow PEP 8 and clean code principles?

[paste code]

For each issue found, show the problematic code and a corrected version.
```

**Pattern 3: The Refactorer**
```
Refactor this code to follow the Single Responsibility Principle.
The current function [describe what it does].

Requirements:
- Split into multiple focused functions
- Maintain identical external behavior
- Add type hints to all function signatures
- Don't change the logic

[paste code]
```

**Pattern 4: The Test Writer**
```
Write pytest unit tests for this function.

Include tests for:
- Normal inputs (happy path)
- Edge cases: [list them]
- Invalid inputs that should raise exceptions

Use descriptive test function names that explain what is being tested.
Mock any external dependencies (database, API calls, file I/O).

[paste function code]
```

**Pattern 5: The Debugger**
```
This code throws the following error:

[paste error + full stack trace]

The function is supposed to [describe expected behavior].
The input when the error occurs is: [describe input]

What is the root cause? Show a corrected version and explain what was wrong.
```

---

## 5. When to Trust AI — and When to Verify

### High-Trust Scenarios (AI is reliable)

- Generating boilerplate (file structure, class scaffolding, config files)
- Explaining well-established concepts (how HTTP works, what a hash table is)
- Translating between languages (Python to JavaScript, SQL to Pandas)
- Regular expressions (AI excels here — complex syntax, common patterns)
- Documenting existing code (writing docstrings, README sections)
- Writing test cases for well-defined functions

### Low-Trust Scenarios (Always verify carefully)

| Scenario | Risk | Mitigation |
|---|---|---|
| Security-critical code | Vulnerabilities in auth, crypto, input handling | Security review, use established libraries |
| Business logic | Subtle misunderstanding of requirements | Explicitly specify invariants, test thoroughly |
| Performance-sensitive paths | Algorithmically poor choices | Benchmark, check complexity |
| Cutting-edge or niche topics | Hallucination risk for less-common domains | Cross-reference documentation |
| Recent API changes | Training cutoff means outdated knowledge | Check official docs for version-specific details |
| Database queries | SQL injection risks, inefficient query plans | Review query structure, use parameterized queries |

### The Verification Checklist for AI-Generated Code

Before accepting AI output:

- [ ] Does it compile/run without errors?
- [ ] Does it produce the correct output for normal inputs?
- [ ] Does it handle the edge cases you specified?
- [ ] Are there any magic numbers without explanation?
- [ ] Does it import libraries that don't exist or have different APIs?
- [ ] Does it use any deprecated functions?
- [ ] Does it handle exceptions appropriately?
- [ ] Are there any obvious security issues (hardcoded secrets, string formatting in SQL)?
- [ ] Would you be comfortable explaining every line of this code in a code review?

---

## 6. AI as a Learning Accelerator

Beyond code generation, AI tools are powerful for accelerating understanding — if used correctly.

### Learning Patterns

**Explain-then-Implement:**
Ask Claude to explain a concept (e.g., binary search) in depth, then implement it yourself without AI assistance, then ask AI to review your implementation.

**Socratic Debugging:**
Instead of asking "what's wrong with this code," ask "what questions should I ask to find the bug in this code?" This builds debugging intuition.

**Concept Comparison:**
```
Compare Python's list comprehension vs. generator expressions.
Explain: when to use each, memory implications, performance differences.
Show examples where the choice matters.
```

**Code Walk-throughs:**
```
Walk me through this sorting algorithm step by step,
showing the state of the array at each iteration
for input: [5, 2, 8, 1, 9, 3]
```

### What AI Cannot Teach You

- The experience of tracking down a bug for 4 hours (patience, systematic thinking)
- The intuition built by reading thousands of lines of real code
- The judgment that comes from shipping software and seeing it fail in production
- The architectural instincts developed through iterative design and redesign

AI compresses the knowledge acquisition curve. It does not replace the experience curve.

---

## 7. Ethical Use of AI in Development

### Attribution and Transparency

Professional norms around AI-generated code are still evolving. Current best practices:

- Check your organization's or client's policy on AI tool use before using them
- For open-source contributions, many projects now require disclosure of AI assistance
- AI-generated code may have licensing implications depending on training data — know your context

### Over-Reliance Risk

The most dangerous pattern: a developer who uses AI to write code they cannot understand. This creates:

- **Invisible technical debt** — code that works but no one can maintain
- **Security blind spots** — vulnerabilities no one recognized because no one read the code carefully
- **Skill atrophy** — reduced ability to work effectively when AI tools are unavailable

The discipline: **understand before you merge**. If you couldn't write this code yourself (given enough time), you should not ship it without understanding it first.

### Bias in AI Output

AI models reflect their training data. Code generated for security-sensitive applications, user data handling, or anything involving fairness (hiring algorithms, credit scoring, etc.) may reflect or amplify problematic patterns. Apply critical analysis.

---

## 8. Practical: Prompt Refinement Exercise

**Original Task:** Build a function that parses log files and extracts error counts by severity level.

**Iteration 1 — Initial prompt:**
```
Write a Python function to parse log files
```

**Iteration 2 — Add structure:**
```
Write a Python function to parse a log file and count errors by severity.
Input: filepath (string)
Output: dictionary with severity levels as keys and counts as values
```

**Iteration 3 — Add constraints and edge cases:**
```
Write a Python function to parse a structured log file and return error counts by severity.

Log format (one entry per line):
2024-01-15 10:23:45 [ERROR] Database connection failed
2024-01-15 10:23:46 [WARNING] Retry attempt 1
2024-01-15 10:23:50 [INFO] Connection restored

Function signature:
    def count_log_severity(filepath: str) -> dict[str, int]:

Requirements:
- Parse severity from between square brackets
- Case-insensitive severity matching
- Ignore malformed lines (log them to stderr but don't crash)
- Handle FileNotFoundError with a descriptive exception
- Return dict with severity as key (uppercase), count as value
  e.g., {"ERROR": 12, "WARNING": 45, "INFO": 203}

Edge cases:
- Empty file → return {}
- File with no parseable lines → return {}
- Very large files (>1GB) — use line-by-line reading, not load-all-at-once
```

Notice how each iteration produces meaningfully better output. Iteration 3 would produce production-quality code; Iteration 1 would produce a toy example requiring significant rework.

---

## Key Vocabulary

| Term | Definition |
|---|---|
| **LLM** | Large Language Model — a neural network trained to predict text sequences |
| **Token** | The unit LLMs process — roughly a word or subword fragment |
| **Context Window** | Maximum amount of text an LLM can consider in one interaction |
| **Hallucination** | When an LLM generates plausible-sounding but factually incorrect content |
| **Prompt Engineering** | The practice of designing inputs to AI models to get optimal outputs |
| **Zero-shot** | Asking a model to perform a task without examples |
| **Few-shot** | Providing examples within the prompt to guide the model's output |
| **Temperature** | A parameter controlling randomness in LLM output (higher = more creative/unpredictable) |

---

## Summary

- AI coding tools (Copilot, Claude, ChatGPT) accelerate development but require a skilled operator to produce reliable output
- LLMs predict statistically plausible text — they don't "know" things, which is why hallucination occurs
- Copilot excels at in-editor completion; Claude/ChatGPT excel at reasoning, review, and explanation
- Prompt quality directly determines output quality — context, constraints, examples, and edge cases all matter
- Security-sensitive code, business logic, and anything involving recent APIs require careful verification
- The ethical risks of AI in development include over-reliance, invisible technical debt, and compliance issues
- AI accelerates knowledge acquisition — it does not replace the depth of experience built through practice

---

## Further Exploration

- **GitHub Copilot Documentation** — settings, privacy, and configuration for your IDE
- **Anthropic's Claude Usage Guide** — best practices for effective prompting
- **"Is GitHub Copilot a Threat to Security?"** — research papers on AI code vulnerability patterns
- **Prompt Engineering Guide** — promptingguide.ai — structured techniques for advanced prompting
- Try: Take a function you've already written, ask Claude to review it, then critically evaluate whether each suggestion is actually an improvement and why

---

*End of Phase 1 — Foundations*
*Next: Lesson 05 — Python Setup & First Steps*
