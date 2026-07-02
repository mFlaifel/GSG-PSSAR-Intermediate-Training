# Lesson 16 — How the Web Works

**Phase 4 — Frontend** | **Duration: 2 Hours** | **Session 16 of 20**

---

## Session Objectives

By the end of this session, students will be able to:

- Explain the client-server model in their own words
- Describe what happens, step by step, from typing a URL to seeing a page render
- Identify the roles that HTML, CSS, and JavaScript each play in a webpage
- Read a basic HTTP request/response pair (method, status code, headers)
- Open the browser DevTools and locate the Elements, Console, and Network tabs

---

## Big Idea

So far, most of the course has focused on one program running on one machine. The web changes that mental model: **two computers talk to each other over a network, and each one has a different job.**

> "Every time you've ever loaded a webpage, two strangers' computers had a conversation in under a second, and one of them sent code the other didn't have."

### Today's Roadmap

In this lesson, students answer four practical questions:

1. Who asks for a webpage?
2. Who sends the webpage back?
3. What exactly travels across the network?
4. How can we inspect that conversation in the browser?

---

## Timed Breakdown

| Time      | Segment                                      | Format              |
| --------- | --------------------------------------------- | -------------------- |
| 0:00–0:10 | Recap Phase 3, frame Phase 4                  | Discussion            |
| 0:10–0:35 | The Client-Server Model                       | Lecture + diagram     |
| 0:35–1:05 | Anatomy of a Request: what happens when you type a URL | Lecture + diagram |
| 1:05–1:15 | **Break**                                     | —                     |
| 1:15–1:40 | HTTP: verbs, status codes, headers            | Lecture + live demo    |
| 1:40–1:55 | DevTools walkthrough                          | Live demo, students follow along |
| 1:55–2:00 | Wrap-up, homework                             | Discussion            |

---

## 1. The Client-Server Model (25 min)

Every website involves at least two machines:

```
        REQUEST
   ┌──────────────────────────────►
┌─────────┐                    ┌─────────┐
│ CLIENT  │                    │ SERVER  │
│(browser)│                    │(remote  │
│         │                    │ computer)│
└─────────┘                    └─────────┘
   ◄──────────────────────────────┘
        RESPONSE
```

- **Client**: the browser (Chrome, Firefox, Safari) running on a laptop or phone. Its job is to *ask* for things and *render* what comes back.
- **Server**: a computer somewhere else — often in a data center — that *listens* for requests and *responds* with data.

Key point: **the server usually does not need to know what kind of device is asking.** It could be a laptop, a phone, or another program. The server receives a request and sends a response. The browser is responsible for displaying what comes back.

**Analogy**: Ordering at a restaurant.
- You (client) don't cook — you request.
- The kitchen (server) doesn't seat guests — it prepares and sends back what was ordered.
- The waiter carrying the ticket back and forth is the *network*.

### Quick Check

Ask: "When you watch a YouTube video, which machine is the client and which is the server?"

Expected answer:
- Your device/browser = client
- YouTube's computers = server

---

## 2. What Happens When You Type a URL (30 min)

Walk through this sequence on the board or in an ASCII diagram, one step at a time. Use a concrete example: `www.example.com`.

```
1. You type www.example.com and hit Enter
        │
        ▼
2. DNS LOOKUP — "What's the IP address for this name?"
   Browser asks a DNS server, like a phonebook lookup
        │
        ▼
3. DNS returns an IP address, e.g. 93.184.216.34
        │
        ▼
4. Browser opens a CONNECTION to that IP address
   (TCP handshake — a quick "are you there? / yes" exchange)
        │
        ▼
5. Browser SENDS an HTTP REQUEST
   "GET / HTTP/1.1 — please send me the homepage"
        │
        ▼
6. Server processes the request, prepares a RESPONSE
        │
        ▼
7. Server SENDS BACK an HTTP RESPONSE
   Status code + HTML (+ links to CSS/JS files)
        │
        ▼
8. Browser RECEIVES the HTML and starts building the page
        │
        ▼
9. Browser sees <link> and <script> tags → sends MORE requests
   for CSS files, JS files, images
        │
        ▼
10. Browser RENDERS the final page — this is what you see
```

### Plain-English Version

When you type a URL, the browser:

1. Finds the server's address
2. Connects to that server
3. Asks for a specific page
4. Receives files back
5. Builds the visible page from those files

### DNS — The Internet's Phonebook

Explain that computers only understand IP addresses (e.g. `93.184.216.34`), not names like `google.com`. DNS (Domain Name System) is the lookup service that converts a human-friendly name into the machine address needed to actually connect.

```
   www.example.com  ──DNS Lookup──►  93.184.216.34
   (what you type)                   (what the computer uses)
```

### The Roles of HTML, CSS, and JavaScript

These are the three core frontend technologies students will use in Lessons 17–18. A useful house-building analogy:

| Technology | Role                         | Analogy              |
| ---------- | ---------------------------- | --------------------- |
| **HTML**   | Structure and content         | The frame and rooms of a house |
| **CSS**    | Appearance and layout         | Paint, furniture, decoration |
| **JavaScript** | Behavior and interactivity | Electricity — makes things move, respond, react |

A page with only HTML is a plain, unstyled house. CSS makes it look intentional. JavaScript makes it *do* things — respond to clicks, update without reloading, validate a form.

### Check for Understanding

Ask students to complete these sentences:

- HTML controls the page's ___.
- CSS controls the page's ___.
- JavaScript controls the page's ___.

Expected answers: structure/content, appearance/layout, behavior/interactivity.

---

## 3. HTTP: Verbs, Status Codes, and Headers (25 min)

### HTTP Verbs (a preview — full depth comes in Lesson 19)

| Verb   | Meaning                  | Example                     |
| ------ | ------------------------- | ---------------------------- |
| GET    | "Give me data"            | Loading a webpage             |
| POST   | "Here's new data, save it" | Submitting a signup form      |
| PUT    | "Update this existing data" | Editing a profile            |
| DELETE | "Remove this data"        | Deleting a post                |

### Status Codes — The Server's Way of Saying What Happened

| Code Range | Meaning        | Common Example                   |
| ---------- | --------------- | ---------------------------------- |
| 2xx        | Success         | `200 OK`                            |
| 3xx        | Redirect        | `301 Moved Permanently`             |
| 4xx        | Client error    | `404 Not Found`                     |
| 5xx        | Server error    | `500 Internal Server Error`         |

> Almost every student has seen a 404 page. Ask: "What do you think that number means now?" Let them connect it back to the table above.

### Headers (brief mention)

Headers are extra information attached to a request or response — metadata, not the actual content. Example: a response header might say `Content-Type: text/html`, telling the browser "what follows is HTML, render it as a page."

Keep this light — headers get revisited in Lesson 19 when students build their own Flask server.

### Tiny Example: Request and Response

```http
GET / HTTP/1.1
Host: example.com
```

```http
HTTP/1.1 200 OK
Content-Type: text/html
```

Read this as: "The client asked for the homepage. The server said the request worked and sent back HTML."

---

## 4. Live Demo: Browser DevTools (15 min)

Open any website (use a simple one — `example.com` or a personal blog). Walk through each tab live while students follow along on their own machines.

1. **Open DevTools** — right-click → "Inspect", or `F12` / `Cmd+Option+I`
2. **Elements tab** — show the live HTML structure; hover over an element in the panel and watch it highlight on the page
3. **Console tab** — type `console.log("hello")` and hit Enter; show that this is where JavaScript errors and output appear
4. **Network tab** — reload the page with Network open; point out:
   - The list of requests (HTML, CSS, JS, images — each a separate request)
   - Status column (mostly `200`s)
   - Time column — how long each request took

> This is the moment the "what happens when you type a URL" diagram becomes real. Every row in the Network tab is one request/response pair from the diagram in Section 2.

---

## Hands-On Activity (bundled into the demo time)

Have students, on their own laptops:

1. Open DevTools on any website of their choice
2. Find and screenshot (or note down):
   - One request with status `200`
   - The `Content-Type` of the main HTML response
   - How many total requests the page made to load

### Success Checklist

By the end of the activity, each student should be able to point to:

- One row in the Network tab and say, "This is one request/response pair."
- One status code and explain whether it means success or error.
- The main HTML document request that started the page load.

---

## Common Points of Confusion

- **"Is the internet the same as the web?"** No — the internet is the physical/network infrastructure; the web (HTTP, browsers, websites) is one application that runs on top of it, like email or gaming.
- **"Why does the same URL sometimes show a different page?"** Servers can return different content based on the request (login state, location, time) — the URL is a request, not a guarantee of fixed content.
- **Confusing client and server direction** — reinforce with the restaurant analogy if this comes up.
- **"Is HTML a programming language?"** HTML describes structure and content. It does not contain logic like Python or JavaScript.

---

## Homework

1. Pick any three websites you use regularly. For each, open DevTools → Network tab, reload the page, and write down:
   - How many total requests were made
   - One HTML request and its status code
2. In 2–3 sentences, explain in your own words what a "client" and a "server" are — no copying definitions, use your own analogy.

### Exit Ticket

Before leaving, students answer in one sentence:

> What is one thing your browser does after it receives HTML from a server?

---

## Looking Ahead

Lesson 17 zooms into the first layer from today's house analogy: **HTML and CSS** — building the structure and appearance of a real webpage from scratch.
