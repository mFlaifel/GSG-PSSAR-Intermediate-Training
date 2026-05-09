# Lesson 01 — Introduction to Programming & Computational Thinking

> **Phase 1 — Foundations | Duration: 2 hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Articulate how programs are executed at a low level (beyond "the computer just runs it")
- Understand how memory, the CPU, and the OS interact during program execution
- Recognize why programming languages exist at different levels of abstraction
- Apply the programming mindset to decompose real-world problems into structured steps

---

## 1. What Is a Program, Really?

Most people think of a program as an app or a file you double-click. That's the surface level. At its core, **a program is a sequence of instructions that manipulates data in memory to produce a desired outcome**.

Every program — whether it's a web server, a mobile game, or a machine learning model — is ultimately (Input-Process-Output):

1. **Loading data** into memory (RAM)
2. **Processing it** using CPU instructions
3. **Outputting results** somewhere (screen, file, network, database)

### The Abstraction Stack

Modern software runs through multiple layers of abstraction. Understanding these layers prevents "magical thinking" about computers:

```
Your Python / JavaScript Code
        ↓
Interpreter / Compiler
        ↓
Machine Code (binary instructions)
        ↓
Operating System (OS) — manages resources
        ↓
CPU + RAM + I/O Hardware
```

When you write `x = 5 + 3` in Python:

- The interpreter parses the expression
- Allocates a memory address for `x`
- Performs integer addition via CPU arithmetic unit
- Stores the result (`8`) at that memory address

You never see this — and that's the point of abstraction. **Higher-level languages trade control for productivity**.

[preview](./abstraction_stack_1.html)

---

## 2. How Computers Actually Think — Binary and Memory

### Binary Basics (Beyond "1s and 0s")

Computers operate on binary because transistors have two stable states: **on (1)** and **off (0)**. Everything — text, images, audio, video, code — is encoded in binary.

| Concept       | Explanation                            |
| ------------- | -------------------------------------- |
| **Bit**       | Single binary digit: 0 or 1            |
| **Byte**      | 8 bits — can represent 256 values (2⁸) |
| **Integer**   | Typically 32 or 64 bits                |
| **Character** | Encoded as a number (ASCII / UTF-8)    |

Example — the letter `A`:

- ASCII value: 65
- Binary: `01000001`
- Hex: `0x41`

This matters when you encounter encoding bugs, file corruption, or work with low-level data parsing.

### Memory (RAM)

RAM is a massive array of byte-addressable locations. Each location has:

- A **memory address** (a number, usually in hexadecimal)
- A **value** stored at that address (bytes)

When you declare a variable, the OS+runtime allocate memory, record the address, and link your variable name to it. That's why languages that expose raw memory (like C) can be both powerful and dangerous — you're directly reading/writing those addresses.

```c
// C — Direct memory access (you won't write this, but understand what Python hides from you)
int x = 42;
int *ptr = &x;   // ptr holds the memory address of x
printf("%d", *ptr);  // reads the value at that address → 42
```

Python wraps all this in objects: every value in Python is an object with a type, reference count, and value — stored in heap memory managed automatically.

### The CPU — Fetch, Decode, Execute

The CPU runs on a cycle:

1. **Fetch** — retrieve the next instruction from memory
2. **Decode** — determine what operation it is (add, compare, jump, etc.)
3. **Execute** — perform the operation using registers and ALU

Modern CPUs execute **billions** of these cycles per second (GHz = billions of cycles/second). What feels "instant" is actually millions of sequential steps.

Key implication for programmers: **algorithms matter**. A poorly written algorithm wastes those cycles. We'll revisit this in Lesson 02.

---

## 3. Programming Languages — Levels of Abstraction

Not all languages are equal in terms of what they expose to you:

| Level           | Language           | Control                  | Abstraction | Use Case                      |
| --------------- | ------------------ | ------------------------ | ----------- | ----------------------------- |
| Low-level       | Assembly, C        | Full hardware control    | Minimal     | OS kernels, embedded systems  |
| Mid-level       | C++, Rust          | Manual memory, high perf | Moderate    | Game engines, system tools    |
| High-level      | Python, JavaScript | Managed automatically    | High        | Web, data science, automation |
| Domain-specific | SQL, HTML, CSS     | Narrow scope             | Very high   | Databases, web layout         |

**Why does this matter to you?** When Python code is "slow," it's often because:

- You're doing something Python's interpreter handles inefficiently
- A lower-level library (like NumPy, written in C) would be orders of magnitude faster
- Understanding the layers helps you make better tool choices

---

## 4. The Programming Mindset

The skill gap between a beginner and an experienced developer is not syntax — it's **thinking methodology**. Here are the four pillars:

### 4.1 Problem Decomposition

Break complex problems into smaller, independently solvable sub-problems.

**Example:** Build a login system

- Validate email format
- Check password strength
- Query the database for the user
- Compare hashed passwords
- Create a session token
- Return success/failure response

Each bullet is its own solvable problem. Trying to solve all at once leads to confusion and bugs.

### 4.2 Abstraction

Focus on **what** something does, not **how** it does it — until you need to know.

When you call `len(my_list)` in Python, you don't think about how Python internally tracks list size. That's abstraction. Good programmers build abstractions (functions, classes, APIs) so others (including their future selves) can work at the right level.

### 4.3 Pattern Recognition

Most software problems have been solved before. Recognizing patterns allows you to:

- Apply known algorithms (sorting, searching, caching)
- Use design patterns (observer, factory, MVC)
- Avoid reinventing solutions

A login system is a pattern. A shopping cart is a pattern. A notification queue is a pattern. Experience is largely the accumulation of recognized patterns.

### 4.4 Systematic Debugging

Debugging is not random guessing — it's a scientific process:

1. **Reproduce** — can you make the bug happen reliably?
2. **Isolate** — narrow down which part of the code causes it
3. **Hypothesize** — form a specific theory about the cause
4. **Test** — verify or refute the hypothesis
5. **Fix & Verify** — apply the fix and confirm the bug is gone

**Reading error messages is a skill.** Most beginners ignore the stack trace. Intermediate developers read it carefully — it tells you exactly what failed and where.

---

## 5. Practical: Thinking Through a Problem

Let's apply the programming mindset to a real scenario before writing any code.

**Scenario:** Build a system that checks if a username is available for registration.

**Step 1 — Decompose:**

- Receive a username input
- Validate it meets format requirements (length, allowed characters)
- Check against existing usernames in a data store
- Return an appropriate response

**Step 2 — Identify edge cases:**

- Empty string input
- Usernames with special characters (`@`, spaces)
- Case sensitivity (is `John` the same as `john`?)
- Very long inputs (potential buffer issues)

**Step 3 — Define data flow:**

```
Input: string
  → validate format → reject if invalid
  → normalize (lowercase)
  → lookup in database
  → return: { available: true/false, reason: string }
```

**Step 4 — Consider failure modes:**

- What if the database is unreachable?
- What if validation takes too long?
- What if two users request the same username simultaneously?

This kind of thinking — before a single line of code — is what separates good software from buggy software.

---

## 6. Key Vocabulary

| Term               | Definition                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Runtime**        | The environment in which code is executed (e.g., Python runtime, Node.js)                                                     |
| **Compilation**    | The process of translating high-level source code into machine code all at once before the program starts.                    |
| **Interpretation** | The process of translating and executing code "on the fly," line-by-line, by a source-code-reading program (the interpreter). |
| **Machine Code**   | The lowest-level instructions (binary) that a CPU can execute directly without further translation.                           |
| **Memory Address** | A unique identifier (usually hexadecimal) that points to a specific location in RAM where data is stored.                     |
| **Heap**           | Region of memory for dynamic allocation (objects, data structures)                                                            |
| **Stack**          | Region of memory for function calls and local variables                                                                       |
| **Abstraction**    | Hiding complexity behind a simplified interface                                                                               |

---

## Summary

- A program is a sequence of instructions that manipulates memory to produce output
- The abstraction stack (code → interpreter → machine code → CPU) is what makes modern programming tractable
- Binary is the foundation; every piece of data is ultimately stored as bytes
- The CPU's fetch-decode-execute cycle is what "running a program" actually means
- The programming mindset — decomposition, abstraction, pattern recognition, systematic debugging — is the real skill to develop
- High-level languages trade performance control for speed of development; the right choice depends on your constraints

---

## Further Exploration

- **"Code" by Charles Petzold** — the best book for understanding computers from transistors up
- **CS50x (Harvard / edX)** — covers the abstraction stack from C to Python to web
- Try: open Python's interactive shell and use `id(x)` on a variable — you're seeing a memory address

---

_Next: Lesson 02 — Algorithms & Problem Solving_
