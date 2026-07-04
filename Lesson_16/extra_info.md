# Why Many Websites Don't Work Correctly When Accessed by IP Address

When you type a domain name such as `google.com`, the browser sends **more than just the IP address** to the server.

## 1. Multiple Websites Can Share One IP Address (Virtual Hosting)
https://dnschecker.org/#A/google.com

A single server may host hundreds of websites on the same IP.

Example:

```text
203.0.113.10
├── example.com
├── myblog.com
├── shop.com
└── api.com
```

If you visit:

```text
http://203.0.113.10
```

the server doesn't necessarily know which website you want.

When you visit:

```text
http://example.com
```

your browser sends:

```http
Host: example.com
```

and the server serves the correct website.

---

## 2. HTTPS Certificates Are Issued for Domain Names

Suppose Google's server has a certificate for:

```text
google.com
*.google.com
```

If you browse to:

```text
https://142.251.163.139
```

the browser expects a certificate for:

```text
142.251.163.139
```

but receives one for:

```text
google.com
```

The names don't match, so the browser shows a security warning.

---

## 3. Load Balancers and CDNs

Large websites often use the same IP address for many customers or services.

Examples:

* Google
* Cloudflare
* Amazon

The server decides where to send your request based on the domain name (using HTTP Host headers and TLS SNI information).

Without the domain name, the request may end up at:

* A default page
* An error page
* The wrong website

---

## 4. Redirects and Application Logic

Some websites are configured to work only with their official domain.

For example, visiting an IP may trigger:

```text
400 Bad Request
```

or:

```text
Please use www.example.com
```

because the application checks the hostname and rejects requests that do not use the expected domain.

---

# Why DNS Still Exists

If typing an IP address were enough, we wouldn't need DNS.

DNS provides several benefits:

* Human-friendly names (`google.com`)
* The ability to move websites to new servers without changing the public address users remember
* Load balancing across many servers
* HTTPS certificates tied to recognizable domain names

## Summary

Every website ultimately runs on one or more IP addresses, but modern web infrastructure relies heavily on the **domain name** being sent along with the request.

Because of virtual hosting, HTTPS certificates, load balancers, CDNs, and application-level hostname checks, directly typing the IP address often does not work or may produce unexpected results.


### Exit Ticket

Before leaving, students answer in one sentence:

> What is one thing your browser does after it receives HTML from a server?