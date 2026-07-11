# Lesson 18 - JavaScript for Front-End Web Development

**Phase 4 - Frontend** | **Duration: 2 Hours** | **Session 18 of 20**

---

## From Last Lecture to This Lecture

In Lesson 17, you built a page with **HTML** and **CSS**:

- **HTML** creates the page structure.
- **CSS** controls how the page looks.

In this lesson, we add the third front-end layer:

- **JavaScript** controls how the page behaves.

Think of a web page like this:

```text
HTML        = content and structure
CSS         = visual style
JavaScript  = interaction and behavior
```

Without JavaScript, a page can show information. With JavaScript, a page can respond to the user.

---

## Learning Objectives

By the end of this lesson, you should be able to:

- Explain what JavaScript does in the browser
- Connect a JavaScript file to an HTML page
- Use `console.log()` to test code
- Create variables with `let` and `const`
- Write a basic JavaScript function
- Select HTML elements using `document.querySelector()`
- Change text, styles, or classes from JavaScript
- Use `addEventListener()` to respond to a button click
- Understand the DOM at a beginner level

---

## 1. What Is JavaScript?

JavaScript is a programming language that runs inside the browser.

You already know many programming ideas from Python:

- variables
- strings and numbers
- functions
- conditions
- loops
- debugging

JavaScript uses the same ideas, but the syntax is different.

Example:

```javascript
const name = "Sara";
let age = 25;

console.log(name);
console.log(age);
```

`console.log()` is like Python's `print()`. It prints information in the browser console.

---

## 2. Connecting JavaScript to HTML

Create three files in the same folder:

```text
index.html
style.css
script.js
```

In your HTML file, connect CSS inside the `<head>` and JavaScript at the end of the `<body>`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JavaScript Demo</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>My Interactive Page</h1>
    <p id="message">Click the button to change this text.</p>
    <button id="changeBtn">Click Me</button>

    <script src="script.js"></script>
</body>
</html>
```

Place the `<script>` tag near the end of the `<body>` so the HTML elements exist before JavaScript tries to find them.

---

## 3. JavaScript Basics

### Variables

Use `const` when the value should not be reassigned.

```javascript
const studentName = "Sara";
```

Use `let` when the value needs to change.

```javascript
let score = 0;
score = score + 1;
```

Avoid `var` in new JavaScript code.

### Data Types

```javascript
const name = "Sara";                  // string
const age = 25;                       // number
const isStudent = true;               // boolean
const skills = ["HTML", "CSS", "JS"]; // array
const profile = { name: "Sara", age: 25 }; // object
```

### Functions

```javascript
function greet(name) {
    return "Hello, " + name + "!";
}

console.log(greet("Sara"));
```

---

## 4. Python vs JavaScript

| Concept | Python | JavaScript |
| --- | --- | --- |
| Print output | `print("Hi")` | `console.log("Hi")` |
| Variable | `age = 25` | `let age = 25;` |
| Constant-style variable | usually naming convention | `const age = 25;` |
| Function | `def greet(name):` | `function greet(name) { }` |
| If statement | `if age > 18:` | `if (age > 18) { }` |
| List / Array | `skills = ["HTML", "CSS"]` | `const skills = ["HTML", "CSS"];` |
| Dictionary / Object | `{"name": "Sara"}` | `{ name: "Sara" }` |
| Comment | `# comment` | `// comment` |

The biggest visual difference is that JavaScript uses curly braces `{ }` to group code.

```javascript
if (age >= 18) {
    console.log("Adult");
}
```

---

## 5. The DOM

The **DOM** stands for **Document Object Model**.

The DOM is the browser's live version of your HTML page. JavaScript can use the DOM to read and change the page.

HTML file:

```html
<body>
    <h1>Hello</h1>
    <p>Welcome to my page.</p>
    <button>Click Me</button>
</body>
```

DOM tree:

```text
document
+-- html
    +-- body
        +-- h1
        +-- p
        +-- button
```

Important idea:

The HTML file is the original code. The DOM is the page as the browser currently understands it.

JavaScript changes the DOM, and the browser updates what the user sees.

---

## 6. Selecting HTML Elements

To change something on the page, JavaScript must select it first.

```javascript
const heading = document.querySelector("h1");
const message = document.querySelector("#message");
const card = document.querySelector(".card");
```

`querySelector()` uses the same selector syntax you learned in CSS:

| Selector | Meaning | Example |
| --- | --- | --- |
| `h1` | Select by tag | `document.querySelector("h1")` |
| `.card` | Select by class | `document.querySelector(".card")` |
| `#message` | Select by ID | `document.querySelector("#message")` |

Practice:

```html
<p id="intro" class="highlight">Welcome!</p>
```

```javascript
document.querySelector("p");          // selects by tag
document.querySelector(".highlight"); // selects by class
document.querySelector("#intro");     // selects by ID
```

---

## 7. Changing Page Content

After selecting an element, you can change it.

```javascript
const message = document.querySelector("#message");

message.textContent = "The text has changed!";
```

You can also change styles:

```javascript
message.style.color = "blue";
message.style.fontSize = "24px";
```

But for bigger style changes, it is usually better to use CSS classes.

```css
.important {
    color: white;
    background-color: darkblue;
    padding: 10px;
}
```

```javascript
message.classList.add("important");
```

Important concept:

JavaScript should control **when** something changes. CSS should usually control **how** it looks.

---

## 8. Events

An **event** is something that happens in the browser.

Examples:

- the user clicks a button
- the user types in an input
- the page finishes loading
- the user moves the mouse

JavaScript can listen for events and run code when they happen.

```javascript
const button = document.querySelector("#changeBtn");

button.addEventListener("click", function() {
    console.log("Button clicked");
});
```

This means:

1. Find the button.
2. Listen for a click.
3. Run the function when the click happens.

---

## 9. Full Example: Change Text on Click

Use the HTML from section 2.

In `script.js`:

```javascript
const message = document.querySelector("#message");
const button = document.querySelector("#changeBtn");

button.addEventListener("click", function() {
    message.textContent = "JavaScript changed the page!";
});
```

What happens:

1. JavaScript selects the paragraph.
2. JavaScript selects the button.
3. The browser waits for a click.
4. When the button is clicked, JavaScript changes the paragraph text.

---

## 10. Full Example: Counter Button

HTML:

```html
<p>Count: <span id="count">0</span></p>
<button id="increaseBtn">Increase</button>
```

JavaScript:

```javascript
let count = 0;

const countDisplay = document.querySelector("#count");
const increaseBtn = document.querySelector("#increaseBtn");

increaseBtn.addEventListener("click", function() {
    count = count + 1;
    countDisplay.textContent = count;
});
```

Important concept:

`count` is JavaScript state. It remembers information while the page is running.

Every click changes the state, then updates the DOM.

```text
click -> update variable -> update DOM -> user sees new page
```

---

## 11. Mini Project: Make Your Profile Page Interactive

Use your profile page from Lesson 17.

Add at least one interactive feature:

- A button that changes your bio text
- A button that changes the background color
- A button that shows or hides your skills list
- A counter that tracks how many times someone clicked a button

Minimum requirements:

- One `<button>`
- One JavaScript file connected with `<script src="script.js"></script>`
- One `document.querySelector()`
- One `addEventListener("click", ...)`
- One visible change on the page

---

## 12. Example Mini Project

HTML:

```html
<section class="profile-card">
    <h1 id="name">Sara Ahmed</h1>
    <p id="bio">I am learning front-end web development.</p>
    <button id="bioBtn">Update Bio</button>
</section>
```

CSS:

```css
.profile-card {
    border: 1px solid #cccccc;
    padding: 20px;
    max-width: 400px;
}

.active {
    background-color: #e6f2ff;
}
```

JavaScript:

```javascript
const bio = document.querySelector("#bio");
const button = document.querySelector("#bioBtn");
const card = document.querySelector(".profile-card");

button.addEventListener("click", function() {
    bio.textContent = "I can now make a web page respond to clicks.";
    card.classList.add("active");
});
```

---

## 13. Debugging Checklist

If your JavaScript does not work, check these first:

- Is `script.js` saved?
- Is the script connected correctly in HTML?
- Is the `<script>` tag at the end of the `<body>`?
- Does your selector match the HTML exactly?
- Did you use `#` for an ID and `.` for a class?
- Did you open the browser console and read the error?

Common error:

```text
Cannot read properties of null
```

This usually means JavaScript could not find the element you tried to select.

Example problem:

```html
<button id="saveBtn">Save</button>
```

```javascript
const button = document.querySelector("#saveButton");
```

The JavaScript asks for `#saveButton`, but the HTML ID is `saveBtn`. The names must match.

---

## Key Takeaways

- JavaScript is the behavior layer of the front end.
- The DOM is the browser's live version of the HTML page.
- Use `document.querySelector()` to select elements.
- Use `textContent`, `style`, or `classList` to change elements.
- Use `addEventListener()` to respond to user actions.
- Use `console.log()` and the browser console to debug.
- A common front-end pattern is:

```text
select element -> listen for event -> update state -> update DOM
```

---

## Homework

Continue your Lesson 17 profile page and add two JavaScript interactions.

Your page should include:

- `index.html`
- `style.css`
- `script.js`
- At least two buttons
- At least two event listeners
- At least one text change
- At least one style or class change

Write a short answer:

> What is the DOM, and why does JavaScript need it?
