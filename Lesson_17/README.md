# Lesson 17 — HTML & CSS Basics

**Phase 4 — Frontend** | **Duration: 2 Hours** | **Session 17 of 20**

---

## Session Objectives

By the end of this session, students will be able to:

- Write a valid HTML document with proper structure (`<!DOCTYPE>`, `head`, `body`)
- Use common semantic HTML5 elements correctly
- Explain and apply the CSS box model
- Write CSS selectors to target elements by tag, class, and ID
- Style text, color, and basic layout
- Build a simple static personal profile webpage from scratch

---

## Big Idea

HTML and CSS are the first tools students use to create something visible in the browser.

- **HTML** answers: "What is on the page?"
- **CSS** answers: "How should it look?"

### Today's Build

Students will create a small personal profile page with:

- A heading and short bio
- A list of skills or interests
- Semantic page sections
- A linked `style.css` file
- At least one reusable CSS class

---

## Timed Breakdown

| Time      | Segment                              | Format                |
| --------- | -------------------------------------- | ----------------------- |
| 0:00–0:10 | Recap Lesson 16, frame today            | Discussion               |
| 0:10–0:35 | HTML document structure & tags          | Lecture + live coding    |
| 0:35–0:55 | Semantic HTML5 elements                 | Lecture + live coding    |
| 0:55–1:05 | **Break**                              | —                        |
| 1:05–1:20 | CSS basics: selectors & the box model   | Lecture + diagram        |
| 1:20–1:35 | Colors, fonts, and layout basics        | Lecture + live coding    |
| 1:35–1:55 | Hands-on: build a profile page          | Guided practice          |
| 1:55–2:00 | Wrap-up, homework                       | Discussion               |

---

## 1. HTML Document Structure (25 min)

Every HTML page follows the same basic skeleton. Type this live and explain each line as you go:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my first webpage.</p>
</body>
</html>
```

| Line                      | Purpose                                          |
| -------------------------- | -------------------------------------------------- |
| `<!DOCTYPE html>`          | Tells the browser "this is a modern HTML5 document" |
| `<html>`                   | The root — everything lives inside it              |
| `<head>`                   | Metadata — not visible on the page itself           |
| `<title>`                  | Text shown in the browser tab                       |
| `<body>`                   | Everything the user actually *sees*                 |

Plain-English summary: the `<head>` is information *about* the page; the `<body>` is the page itself.

### Tags Come in Pairs (Mostly)

```
<p>This is a paragraph.</p>
 ↑                        ↑
opening tag          closing tag
```

Some tags are **self-closing** — they don't wrap content: `<img>`, `<br>`, `<input>`, `<meta>`.

### Core Tags to Introduce

| Tag                | Purpose               |
| ------------------- | ----------------------- |
| `<h1>` – `<h6>`     | Headings, largest to smallest |
| `<p>`               | Paragraph               |
| `<a href="...">`    | Link                    |
| `<img src="..." alt="...">` | Image           |
| `<ul>` / `<ol>` / `<li>` | Unordered/ordered lists |
| `<div>`             | Generic block container |
| `<span>`            | Generic inline container |

> Emphasize: HTML describes *what things are*, not *how they look*. That's CSS's job — coming up in 45 minutes.

### Mini Practice

Ask students to write three lines of HTML:

1. Their name as a heading
2. One sentence about themselves
3. A link to a website they use often

This gives them a quick win before the longer profile-page activity.

### Nesting

```
<div>
    <h1>Title</h1>
    <p>Text inside a <span>highlighted</span> word.</p>
</div>
```

Draw the nesting as a tree on the board:

```
div
├── h1
└── p
    └── span
```

This tree structure is exactly what students saw in the DevTools Elements panel in Lesson 16 — connect the dots explicitly.

---

## 2. Semantic HTML5 Elements (20 min)

A page built entirely from `<div>` tags works, but tells the browser (and screen readers, and search engines) nothing about *meaning*. Semantic tags fix that.

| Semantic Tag  | Replaces (non-semantic) | Meaning                        |
| -------------- | ------------------------- | -------------------------------- |
| `<header>`     | `<div class="header">`    | Top section of a page or section |
| `<nav>`        | `<div class="nav">`       | Navigation links                  |
| `<main>`       | `<div class="main">`      | Primary content of the page       |
| `<section>`    | `<div class="section">`   | A thematic grouping of content    |
| `<article>`    | `<div class="article">`   | Self-contained content (blog post, card) |
| `<footer>`     | `<div class="footer">`    | Bottom section                    |

```
<body>
    <header>...</header>
    <nav>...</nav>
    <main>
        <section>...</section>
        <article>...</article>
    </main>
    <footer>...</footer>
</body>
```

**Why it matters**: semantic tags improve accessibility, help search engines understand the page, and make code easier for other developers to read.

Plain-English rule: use a semantic tag when the section has a clear meaning; use `<div>` when you only need a generic container.

---

## 3. CSS Basics: Selectors & the Box Model (15 min)

CSS rules follow this pattern:

```css
selector {
    property: value;
}
```

```css
p {
    color: blue;
    font-size: 16px;
}
```

### Three Ways to Connect CSS to HTML

```html
<!-- 1. Inline (avoid — hard to maintain) -->
<p style="color: blue;">Text</p>

<!-- 2. Internal -->
<head>
    <style>
        p { color: blue; }
    </style>
</head>

<!-- 3. External (best practice) -->
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

Recommend external stylesheets from day one — it mirrors separating logic across files, a habit already built in Python (Lesson 15, custom modules).

### Selectors

| Selector    | Targets                        | Example         |
| ------------ | -------------------------------- | ----------------- |
| Tag          | All elements of that type        | `p { }`           |
| Class        | Elements with `class="name"`     | `.highlight { }`  |
| ID           | The one element with `id="name"` | `#header { }`     |

```html
<p class="highlight">Special text</p>
<div id="main-box">Unique box</div>
```
```css
.highlight { background-color: yellow; }
#main-box   { border: 2px solid black; }
```

> Rule of thumb for students: **classes for anything reusable, IDs for anything unique.**

### Selector Practice

Given this HTML:

```html
<p class="warning" id="main-warning">Be careful.</p>
```

<details>
<summary><strong>Question:</strong> Which selector targets every paragraph?</summary>

`p`

</details>

<details>
<summary><strong>Question:</strong> Which selector targets the reusable class?</summary>

`.warning`

</details>

<details>
<summary><strong>Question:</strong> Which selector targets the unique ID?</summary>

`#main-warning`

</details>

### The Box Model

Every HTML element is a rectangular box made of four layers:

```
┌───────────────────────────────────┐
│              MARGIN                │
│   ┌─────────────────────────────┐  │
│   │           BORDER              │  │
│   │   ┌───────────────────────┐  │  │
│   │   │        PADDING          │  │  │
│   │   │   ┌───────────────┐   │  │  │
│   │   │   │    CONTENT      │   │  │  │
│   │   │   └───────────────┘   │  │  │
│   │   └───────────────────────┘  │  │
│   └─────────────────────────────┘  │
└───────────────────────────────────┘
```

| Layer      | What it is                              |
| ----------- | ------------------------------------------ |
| Content     | The actual text/image                       |
| Padding     | Space *inside* the border, around the content |
| Border      | The edge of the box                          |
| Margin      | Space *outside* the border, pushing other elements away |

```css
.box {
    padding: 10px;
    border: 2px solid black;
    margin: 20px;
}
```

This diagram is worth slowing down for because many beginner layout problems come from mixing up margin and padding.

### Box Model Check

<details>
<summary><strong>Question:</strong> If I want more space between the text and its border, should I use `padding` or `margin`?</summary>

Expected answer: `padding`.

</details>

<details>
<summary><strong>Question:</strong> If I want more space between this box and the next box, should I use `padding` or `margin`?</summary>

Expected answer: `margin`.

</details>

---

## 4. Colors, Fonts, and Layout Basics (15 min)

```css
body {
    font-family: Arial, sans-serif;
    color: #333333;
    background-color: #f5f5f5;
}

h1 {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
}
```

### Color Formats (brief)

| Format        | Example              |
| -------------- | ----------------------- |
| Named          | `color: red;`            |
| Hex            | `color: #ff0000;`        |
| RGB            | `color: rgb(255, 0, 0);` |

### Basic Layout: `display`

Mention just enough to unblock the activity. Full layout systems like Flexbox and Grid are beyond this lesson's scope, but students should know these two values:

```css
.inline-item { display: inline-block; }
.block-item  { display: block; }
```

---

## Hands-On Activity: Build a Personal Profile Page (20 min)

Students build a single-page HTML + CSS profile with:

- A `<header>` with their name as an `<h1>`
- A profile description in a `<p>`
- A `<ul>` list of 3 skills or interests
- At least one styled `.highlight` class
- An external `style.css` file linked properly

**Starter structure to project on screen:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Profile</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Your Name</h1>
    </header>
    <main>
        <p>A short bio goes here.</p>
        <ul>
            <li>Skill 1</li>
            <li>Skill 2</li>
            <li>Skill 3</li>
        </ul>
    </main>
</body>
</html>
```

Circulate during this time — this is the first moment students write HTML/CSS unassisted, so expect syntax errors (unclosed tags, missing semicolons) and use them as live teaching moments.

### Success Checklist

A complete first version should have:

- `index.html` and `style.css` in the same folder
- A working `<link rel="stylesheet" href="style.css">`
- At least one semantic element such as `<header>` or `<main>`
- At least one class used in both HTML and CSS
- Text that is readable against the background color

---

## Common Beginner Mistakes

- Forgetting to close tags (`<p>text</div>` instead of `</p>`)
- Confusing `class` (reusable, dot selector) with `id` (unique, hash selector)
- Forgetting the `<link>` tag, then wondering why CSS "isn't working"
- Margin/padding confusion — refer back to the box model diagram
- Missing `alt` attribute on `<img>` tags (mention accessibility briefly)
- Putting CSS inside the HTML file by accident after creating `style.css`
- Expecting the browser to refresh automatically — remind students to save the file, then reload the page

---

## Homework

1. Finish the personal profile page if not completed in class
2. Add at least one `<img>` tag and style it with CSS (width, border, or margin)
3. Change your page's color scheme using hex codes instead of named colors

### Exit Ticket

Before leaving, students answer:

<details>
<summary><strong>Question:</strong> What is one difference between a class selector and an ID selector?</summary>

- A class selector targets multiple elements and uses a dot (`.`) prefix
- An ID selector targets a single unique element and uses a hash (`#`) prefix

</details>

---
## Further Exploration

- [**HTML elements reference**](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements) 
- [**W3 school html**](https://www.w3schools.com/html/default.asp)
- [**Free code camp**](https://www.freecodecamp.org/)

## Looking Ahead

Lesson 18 adds **JavaScript** — the layer that makes the page in today's activity actually respond to clicks and change without a reload.
