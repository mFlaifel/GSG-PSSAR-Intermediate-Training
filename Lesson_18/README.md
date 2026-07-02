# Lesson 18 — JavaScript Basics & DOM

**Phase 4 — Frontend** | **Duration: 2 Hours** | **Session 18 of 20**

---

## Session Objectives

By the end of this session, students will be able to:

- Declare variables in JavaScript using `let` and `const`
- Write basic JavaScript functions
- Explain what the DOM is and why it matters
- Select HTML elements using `document.querySelector()`
- Change page content and styles using JavaScript
- Handle a click event with `onClick`
- Compare Python and JavaScript syntax side by side

---

## Timed Breakdown

| Time      | Segment                                | Format               |
| --------- | ----------------------------------------- | ----------------------- |
| 0:00–0:10 | Recap Lesson 17, frame today               | Discussion              |
| 0:10–0:30 | JavaScript basics: variables & functions   | Lecture + live coding   |
| 0:30–0:40 | Python vs. JavaScript comparison           | Lecture + discussion    |
| 0:40–1:05 | What is the DOM? Selecting elements        | Lecture + diagram + live coding |
| 1:05–1:15 | **Break**                                 | —                       |
| 1:15–1:40 | Changing content & handling click events   | Live coding              |
| 1:40–1:55 | Hands-on: interactive counter/button        | Guided practice           |
| 1:55–2:00 | Wrap-up, homework                          | Discussion               |

---

## 1. JavaScript Basics (20 min)

JavaScript is the third layer from Lesson 17's house analogy — it's what makes a page *do* things. Unlike HTML/CSS, JavaScript is a real programming language, and students already know one: Python. Lean into that.

### Variables

```javascript
let age = 25;          // can be reassigned
const name = "Sara";   // cannot be reassigned
```

| Keyword | Behavior                     |
| -------- | ------------------------------- |
| `let`    | Value can change later          |
| `const`  | Value is locked once set        |
| `var`    | Old style — mention it exists, tell students to avoid it |

### Data Types (quick pass — mostly familiar)

```javascript
let age = 25;              // number
let name = "Sara";          // string
let isStudent = true;       // boolean
let skills = ["HTML", "CSS", "JS"];  // array
let person = { name: "Sara", age: 25 };  // object
```

### Functions

```javascript
function greet(name) {
    return "Hello, " + name + "!";
}

console.log(greet("Sara"));
```

Modern shorthand (mention, don't over-teach):

```javascript
const greet = (name) => {
    return "Hello, " + name + "!";
};
```

---

## 2. Python vs. JavaScript — Side by Side (10 min)

Put this table on screen and let it do the teaching — students map new syntax onto concepts they already own.

| Concept          | Python                          | JavaScript                        |
| ----------------- | --------------------------------- | ------------------------------------ |
| Print to console  | `print("Hi")`                     | `console.log("Hi")`                  |
| Variable           | `age = 25`                        | `let age = 25;`                      |
| Function           | `def greet(name):`                | `function greet(name) {`             |
| If statement       | `if age > 18:`                    | `if (age > 18) {`                    |
| For loop           | `for i in range(5):`              | `for (let i = 0; i < 5; i++) {`      |
| List/Array         | `skills = ["a", "b"]`             | `let skills = ["a", "b"];`           |
| Dict/Object        | `person = {"name": "Sara"}`       | `let person = {name: "Sara"};`       |
| Line endings       | Newline / indentation matters      | Semicolons; curly braces `{ }`       |
| Comments           | `# comment`                        | `// comment`                          |

> Key framing line: "You already know how to think in code. Today you're learning a new *accent*, not a new *language of thought*."

---

## 3. What Is the DOM? (25 min)

The **DOM (Document Object Model)** is how JavaScript "sees" and interacts with an HTML page — as a tree of objects it can read and change.

```
              document
                 │
              <html>
                 │
        ┌────────┴────────┐
      <head>            <body>
                            │
                 ┌──────────┼──────────┐
              <h1>         <p>       <button>
              "Hello"    "Text"     "Click me"
```

This is the *exact same tree* students saw in the DevTools Elements panel back in Lesson 16 — JavaScript is simply a way to reach into that tree programmatically and change it.

### Selecting Elements

```javascript
// Select the first matching element
const heading = document.querySelector("h1");

// Select by ID
const box = document.querySelector("#main-box");

// Select by class
const item = document.querySelector(".highlight");

// Select ALL matching elements (returns a list)
const allItems = document.querySelectorAll("li");
```

`querySelector` uses the exact same selector syntax as CSS from Lesson 17 — another deliberate connection to draw out loud.

---

## 4. Changing Content & Handling Events (25 min)

### Reading and Changing Content

```javascript
const heading = document.querySelector("h1");

console.log(heading.textContent);   // read current text
heading.textContent = "New Title";  // change it
```

### Changing Styles

```javascript
heading.style.color = "blue";
heading.style.fontSize = "40px";
```

### Handling Clicks

```html
<button id="myButton">Click Me</button>
```

```javascript
const button = document.querySelector("#myButton");

button.addEventListener("click", function() {
    alert("Button was clicked!");
});
```

Or inline (simpler for first exposure, mention `addEventListener` is the more scalable long-term pattern):

```html
<button onclick="alert('Clicked!')">Click Me</button>
```

### Live Demo: Build a Counter

Type this live, explaining each line:

```html
<p id="count">0</p>
<button id="incrementBtn">+1</button>
```

```javascript
let count = 0;
const countDisplay = document.querySelector("#count");
const button = document.querySelector("#incrementBtn");

button.addEventListener("click", function() {
    count = count + 1;
    countDisplay.textContent = count;
});
```

Walk through what happens on each click: JavaScript variable updates → DOM element's text is reassigned → browser re-renders. This is the "behavior" layer from Lesson 17 made concrete.

---

## Hands-On Activity: Interactive Counter or Button (15 min)

Building on the profile page from Lesson 17, students add one interactive element. Options (offer as choices, not requirements):

1. A counter button (like the live demo)
2. A button that changes the page's background color on click
3. A button that shows/hides a paragraph of text

**Minimum requirement**: one `<button>`, one `addEventListener`, one DOM change (text or style).

Circulate and help debug — this is the first time students connect JS to HTML live, so expect `null` errors from mistyped selectors (a great moment to reinforce reading error messages from Lesson 03).

---

## Common Beginner Mistakes

- Forgetting `let`/`const` when declaring a variable
- Missing semicolons (JS is more forgiving than students expect, but flag it as good practice)
- Selecting an element with the wrong selector (e.g., `.myButton` instead of `#myButton`)
- Putting the `<script>` tag before the HTML it targets exists — the DOM isn't loaded yet, so `querySelector` returns `null`. Fix: place `<script>` at the end of `<body>`, or use an event listener for `DOMContentLoaded`
- Confusing `=` (assignment) with `==`/`===` (comparison) — a mistake Python students often carry over correctly, but worth a one-line reminder

---

## Homework

1. Add two more interactive elements to your profile page from Lesson 17
2. Use `console.log()` at least twice to practice reading output in DevTools' Console tab
3. In your own words (2–3 sentences): what is the DOM, and how is it different from the HTML file itself?

---

## Looking Ahead

Lesson 19 flips the picture from Lesson 16's diagram — instead of being the client requesting data, students will build the **server** side: a Flask API that responds to requests.
