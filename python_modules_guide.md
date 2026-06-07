# 🐍 Python Important Modules — Developer Reference Guide

> A practical reference covering the most essential Python standard library modules and patterns, with real-world examples and use cases for developers.

---

## Table of Contents

1. [File System & OS — `os`, `pathlib`, `shutil`](#1-file-system--os)
2. [System & Runtime — `sys`](#2-system--runtime)
3. [Data Serialization — `json`, `csv`, `pickle`](#3-data-serialization)
4. [Date & Time — `datetime`, `time`](#4-date--time)
5. [Math & Numbers — `math`, `decimal`, `random`, `statistics`](#5-math--numbers)
6. [Text & Regex — `re`, `string`, `textwrap`](#6-text--regex)
7. [Collections & Itertools — `collections`, `itertools`, `functools`](#7-collections--itertools)
8. [Concurrency — `threading`, `multiprocessing`, `asyncio`](#8-concurrency)
9. [Networking — `urllib`, `http`, `socket`](#9-networking)
10. [Logging & Debugging — `logging`, `pdb`, `traceback`](#10-logging--debugging)
11. [Type System — `typing`, `dataclasses`, `enum`](#11-type-system)
12. [Context Managers — `contextlib`](#12-context-managers)
13. [CLI & Config — `argparse`, `configparser`](#13-cli--config)
14. [Database — `sqlite3`](#14-database)
15. [Compression — `zipfile`, `gzip`, `tarfile`](#15-compression)
16. [Testing — `unittest`, `doctest`](#16-testing)
17. [Environment — `os.environ`, `subprocess`](#17-environment--subprocess)

---

## 1. File System & OS

### `os` — Operating System Interface

**Use cases:** Directory traversal, file checks, environment variables, process control.

```python
import os

# Check and navigate paths
print(os.getcwd())                     # Current working directory
os.chdir('/tmp')                       # Change directory

# File / directory checks
os.path.exists('config.yaml')         # True / False
os.path.isfile('app.py')              # Is it a file?
os.path.isdir('logs/')                # Is it a directory?

# Build paths safely (cross-platform)
config_path = os.path.join('config', 'settings.json')

# Directory operations
os.makedirs('logs/2024/june', exist_ok=True)   # mkdir -p
os.rename('old_name.txt', 'new_name.txt')
os.remove('temp.txt')
os.rmdir('empty_dir/')

# Walk directory tree
for root, dirs, files in os.walk('src/'):
    for file in files:
        if file.endswith('.py'):
            full_path = os.path.join(root, file)
            print(full_path)

# Environment variables
db_url = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
os.environ['DEBUG'] = 'true'

# File metadata
stat = os.stat('app.py')
print(f"Size: {stat.st_size} bytes")
print(f"Modified: {stat.st_mtime}")
```

---

### `pathlib` — Object-Oriented File Paths ⭐ Modern Preferred

**Use cases:** Any path manipulation; cleaner than `os.path`, fully cross-platform.

```python
from pathlib import Path

base = Path('/project')

# Path composition with /  operator
config = base / 'config' / 'settings.json'
print(config)                   # /project/config/settings.json
print(config.name)              # settings.json
print(config.stem)              # settings
print(config.suffix)            # .json
print(config.parent)            # /project/config

# Read and write text / bytes
config.write_text('{"debug": true}')
data = config.read_text()

# Existence checks
if not config.exists():
    config.parent.mkdir(parents=True, exist_ok=True)
    config.touch()

# Glob patterns
py_files   = list(Path('src').glob('**/*.py'))       # recursive
test_files = list(Path('tests').glob('test_*.py'))

# Home directory & resolution
home = Path.home()                  # /home/user  or  C:\Users\user
cwd  = Path.cwd()
real = Path('../../app.py').resolve()   # absolute, no dots

# Iterating a directory
for entry in Path('logs').iterdir():
    if entry.is_file():
        print(entry, entry.stat().st_size)

# Rename / delete
config.rename(config.with_name('settings.bak.json'))
config.unlink(missing_ok=True)      # delete file
```

---

### `shutil` — High-Level File Operations

**Use cases:** Copy/move files & directories, create archives, disk usage.

```python
import shutil

# Copy
shutil.copy('src.txt', 'dst.txt')              # copy file
shutil.copy2('src.txt', 'dst.txt')             # copy + preserve metadata
shutil.copytree('src_dir/', 'dst_dir/')        # copy entire directory

# Move / delete
shutil.move('old/path', 'new/path')
shutil.rmtree('dir_to_delete/')                # rm -rf

# Archives
shutil.make_archive('backup', 'zip', 'project/')
shutil.unpack_archive('backup.zip', 'extracted/')

# Disk usage
usage = shutil.disk_usage('/')
print(f"Free: {usage.free / 1e9:.1f} GB")

# Find an executable on PATH
python_path = shutil.which('python3')
```

---

## 2. System & Runtime

### `sys` — System Parameters and Functions

**Use cases:** CLI args, stdin/stdout, import hooks, exit codes.

```python
import sys

# Command-line arguments  (sys.argv[0] = script name)
script, *args = sys.argv

# Standard streams
sys.stdout.write('Hello\n')
sys.stderr.write('Error: something went wrong\n')
data = sys.stdin.readline()

# Python version check
if sys.version_info < (3, 10):
    raise RuntimeError('Requires Python 3.10+')

print(sys.platform)             # 'linux', 'darwin', 'win32'
print(sys.executable)           # Path to Python interpreter

# Module search path
sys.path.insert(0, '/my/custom/lib')

# Exit with code
sys.exit(0)    # success
sys.exit(1)    # failure

# Object size in bytes
import sys
x = [1, 2, 3]
print(sys.getsizeof(x))

# Recursion limit
sys.setrecursionlimit(5000)
```

---

## 3. Data Serialization

### `json` — JSON Encode / Decode

**Use cases:** APIs, config files, inter-service communication.

```python
import json

# Serialize (Python → JSON string)
data = {'name': 'Alice', 'age': 30, 'active': True, 'scores': [95, 87]}
json_str = json.dumps(data, indent=2, sort_keys=True)
print(json_str)

# Deserialize (JSON string → Python)
obj = json.loads(json_str)

# File I/O
with open('config.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('config.json') as f:
    config = json.load(f)

# Custom encoder for types JSON can't handle natively
from datetime import datetime, date

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)

payload = {'created_at': datetime.now(), 'name': 'Bob'}
print(json.dumps(payload, cls=DateEncoder))
```

---

### `csv` — CSV File Reading and Writing

**Use cases:** Data imports/exports, spreadsheet interop, ETL pipelines.

```python
import csv

# Write
rows = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'São Paulo'],
    ['Bob',   25, 'Rio'],
]
with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read
with open('users.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)    # rows as dicts keyed by header
    for row in reader:
        print(row['Name'], row['Age'])

# Write dicts
fields = ['Name', 'Age', 'City']
records = [{'Name': 'Carol', 'Age': 28, 'City': 'Curitiba'}]
with open('out.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)
```

---

### `pickle` — Python Object Serialization

**Use cases:** Caching ML models, session data, complex Python objects.

```python
import pickle

# Serialize any Python object
model = {'weights': [0.1, 0.5], 'bias': 0.3, 'version': 2}

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model.pkl', 'rb') as f:
    loaded = pickle.load(f)

# In-memory (bytes)
data_bytes = pickle.dumps(model)
restored   = pickle.loads(data_bytes)

# ⚠️  Security: never unpickle data from untrusted sources.
```

---

## 4. Date & Time

### `datetime` — Dates, Times, Timedeltas

**Use cases:** Timestamps, scheduling, date arithmetic, formatting.

```python
from datetime import datetime, date, time, timedelta, timezone

# Now
now_local = datetime.now()
now_utc   = datetime.now(tz=timezone.utc)

# Construction
dt = datetime(2024, 6, 15, 9, 30, 0)
d  = date(2024, 6, 15)
t  = time(9, 30, 0)

# Formatting
print(now_utc.strftime('%Y-%m-%d %H:%M:%S'))    # '2024-06-15 09:30:00'
print(now_utc.isoformat())                       # ISO 8601

# Parsing
parsed = datetime.strptime('2024-06-15', '%Y-%m-%d')
from_iso = datetime.fromisoformat('2024-06-15T09:30:00+00:00')

# Arithmetic
tomorrow   = now_local + timedelta(days=1)
two_weeks  = now_local + timedelta(weeks=2)
in_90_mins = now_local + timedelta(minutes=90)

delta = datetime(2024, 12, 31) - datetime.now()
print(f'{delta.days} days until New Year')

# Timestamps (UNIX epoch)
ts = datetime.now().timestamp()          # float seconds
dt = datetime.fromtimestamp(ts)

# Timezone-aware
import zoneinfo
sp = zoneinfo.ZoneInfo('America/Sao_Paulo')
now_sp = datetime.now(tz=sp)
```

---

## 5. Math & Numbers

### `math` — Mathematical Functions

```python
import math

math.sqrt(16)           # 4.0
math.pow(2, 10)         # 1024.0
math.log(math.e)        # 1.0
math.log10(1000)        # 3.0
math.log2(8)            # 3.0

math.ceil(4.2)          # 5
math.floor(4.8)         # 4
math.fabs(-3.7)         # 3.7

math.pi                 # 3.141592653589793
math.e                  # 2.718281828459045
math.tau                # 6.283185307179586
math.inf                # infinity

math.gcd(48, 64)        # 16
math.factorial(10)      # 3628800
math.isfinite(math.inf) # False
math.isnan(float('nan'))# True

# Trigonometry (radians)
math.sin(math.pi / 2)   # 1.0
math.cos(0)             # 1.0
math.degrees(math.pi)   # 180.0
math.radians(180)       # pi
```

---

### `decimal` — Precise Decimal Arithmetic

**Use cases:** Financial calculations — avoids floating-point errors.

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Floating-point trap
print(0.1 + 0.2)                    # 0.30000000000000004

# Decimal fix
print(Decimal('0.1') + Decimal('0.2'))   # 0.3

# Precision
getcontext().prec = 10
result = Decimal('1') / Decimal('3')     # 0.3333333333

# Rounding (financial)
price = Decimal('19.4567')
rounded = price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(rounded)     # 19.46

# Currency
TAX_RATE = Decimal('0.075')
subtotal = Decimal('1250.00')
tax      = (subtotal * TAX_RATE).quantize(Decimal('0.01'))
total    = subtotal + tax
```

---

### `random` — Random Number Generation

```python
import random

random.random()                         # float [0.0, 1.0)
random.uniform(1.5, 6.5)               # float in range
random.randint(1, 6)                    # int inclusive both ends
random.randrange(0, 100, 5)            # step 5

items = ['a', 'b', 'c', 'd']
random.choice(items)                    # single random item
random.choices(items, k=3)             # with replacement
random.sample(items, k=2)             # without replacement
random.shuffle(items)                  # in-place shuffle

# Reproducible results
random.seed(42)

# Gaussian / Normal distribution
random.gauss(mu=0, sigma=1)

# Secure random (cryptography)
import secrets
token  = secrets.token_hex(32)         # 64-char hex string
pin    = secrets.randbelow(10000)      # int [0, 10000)
```

---

### `statistics` — Statistical Functions

```python
from statistics import (
    mean, median, mode, stdev, variance,
    fmean, geometric_mean, harmonic_mean,
    quantiles, NormalDist
)

data = [2, 4, 4, 4, 5, 5, 7, 9]

mean(data)          # 5.0
median(data)        # 4.5
mode(data)          # 4
stdev(data)         # 2.0
variance(data)      # 4.0

# Percentiles / quartiles
q = quantiles(data, n=4)    # [Q1, Q2, Q3]

# Normal distribution
dist = NormalDist(mu=100, sigma=15)   # IQ example
dist.pdf(100)                          # density at mean
dist.cdf(130)                          # P(X ≤ 130)
dist.inv_cdf(0.95)                     # 95th percentile
```

---

## 6. Text & Regex

### `re` — Regular Expressions

**Use cases:** Validation, parsing, search & replace, log analysis.

```python
import re

text = 'Contact us at support@example.com or sales@company.org'

# Search (first match)
match = re.search(r'[\w.+-]+@[\w-]+\.\w+', text)
if match:
    print(match.group())        # support@example.com

# Find all
emails = re.findall(r'[\w.+-]+@[\w-]+\.\w+', text)

# Named groups
log = '2024-06-15 ERROR: connection refused'
m = re.match(r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+): (?P<msg>.+)', log)
if m:
    print(m.group('level'))     # ERROR
    print(m.groupdict())        # {'date': ..., 'level': ..., 'msg': ...}

# Replace
clean = re.sub(r'\s+', ' ', '  too   many    spaces  ').strip()

# Split
tokens = re.split(r'[,;\s]+', 'one,two; three four')

# Pre-compile for performance in loops
EMAIL_RE = re.compile(r'[\w.+-]+@[\w-]+\.\w+', re.IGNORECASE)
for line in open('log.txt'):
    for hit in EMAIL_RE.finditer(line):
        print(hit.group(), hit.start())

# Common patterns
PHONE_BR = re.compile(r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}')
CPF_RE   = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
URL_RE   = re.compile(r'https?://[^\s]+')
```

---

### `textwrap` — Text Wrapping & Formatting

```python
import textwrap

long_text = "Python is an interpreted, high-level, general-purpose programming language."

# Wrap at column width
wrapped = textwrap.fill(long_text, width=40)

# Dedent (remove common leading whitespace)
code = """
    def hello():
        print("world")
"""
print(textwrap.dedent(code))

# Indent
indented = textwrap.indent(long_text, prefix='    ')

# Shorten with ellipsis
short = textwrap.shorten(long_text, width=30, placeholder=' ...')
```

---

## 7. Collections & Itertools

### `collections` — Specialized Container Types ⭐

**Use cases:** Counting, ordered maps, default dicts, named tuples.

```python
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap

# --- Counter ---
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
c = Counter(words)
print(c)                        # Counter({'apple': 3, 'banana': 2, ...})
c.most_common(2)                # [('apple', 3), ('banana', 2)]

# Count characters
char_freq = Counter('mississippi')

# Arithmetic
a = Counter({'x': 3, 'y': 1})
b = Counter({'x': 1, 'z': 2})
print(a + b)                    # Counter({'x': 4, 'z': 2, 'y': 1})

# --- defaultdict ---
graph = defaultdict(list)
graph['A'].append('B')         # no KeyError for missing keys
graph['A'].append('C')

word_indices = defaultdict(set)
for i, w in enumerate('the cat sat on the mat'.split()):
    word_indices[w].add(i)

# --- deque (double-ended queue) ---
dq = deque(maxlen=5)           # fixed-size sliding window
for i in range(10):
    dq.append(i)
print(dq)                      # deque([5, 6, 7, 8, 9], maxlen=5)

dq.appendleft(99)              # O(1) prepend
dq.rotate(2)                   # rotate right
dq.popleft()                   # O(1) pop from left

# --- namedtuple ---
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)                # 10 20
print(p._asdict())             # {'x': 10, 'y': 20}

# --- ChainMap (layered dicts, first match wins) ---
defaults  = {'color': 'red', 'size': 10}
overrides = {'size': 20}
merged = ChainMap(overrides, defaults)
print(merged['color'], merged['size'])   # red  20
```

---

### `itertools` — Fast, Memory-Efficient Iterators

```python
import itertools

# --- Infinite iterators ---
counter = itertools.count(start=1, step=2)   # 1, 3, 5, 7 ...
cycler  = itertools.cycle('ABC')             # A B C A B C ...
repeater= itertools.repeat(42, times=3)      # 42 42 42

# --- Combinatorics ---
list(itertools.permutations('ABC', 2))       # AB AC BA BC CA CB
list(itertools.combinations('ABCD', 2))      # AB AC AD BC BD CD
list(itertools.combinations_with_replacement('AB', 2))  # AA AB BB
list(itertools.product([0,1], repeat=3))     # all 3-bit combinations

# --- Grouping ---
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))     # A [(A,1),(A,2)]  B [(B,3),(B,4)]

# --- Slicing & chaining ---
first_5 = list(itertools.islice(counter, 5))   # [1, 3, 5, 7, 9]
chained = list(itertools.chain([1,2], [3,4], [5]))   # [1,2,3,4,5]
flattened = list(itertools.chain.from_iterable([[1,2],[3,4]]))

# --- Practical: sliding window ---
def sliding_window(iterable, n):
    it = iter(iterable)
    window = deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)
```

---

### `functools` — Higher-Order Functions

```python
from functools import reduce, partial, lru_cache, wraps, cached_property

# --- lru_cache (memoization) ---
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))          # instant; without cache would take forever
print(fib.cache_info()) # CacheInfo(hits=48, misses=51, ...)

# --- partial (freeze arguments) ---
from functools import partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube   = partial(power, exp=3)
print(square(5), cube(3))      # 25  27

# --- reduce ---
product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])   # 120

# --- wraps (preserve docstrings in decorators) ---
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Before')
        result = func(*args, **kwargs)
        print('After')
        return result
    return wrapper

# --- cached_property (compute once per instance) ---
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        import math
        return math.pi * self.radius ** 2
```

---

## 8. Concurrency

### `threading` — Thread-Based Parallelism

**Use cases:** I/O-bound tasks — network requests, file reads (GIL-limited for CPU tasks).

```python
import threading
import time

# Basic thread
def worker(name, delay):
    time.sleep(delay)
    print(f'[{name}] done')

threads = [threading.Thread(target=worker, args=(f'T{i}', i)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()   # wait for all

# Thread with return value via subclass
class ResultThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        self.func, self.args = func, args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

# Lock — prevent race conditions
counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    with lock:
        counter += 1

# Event — signal between threads
event = threading.Event()

def waiter():
    event.wait()          # blocks until set
    print('Received signal!')

threading.Thread(target=waiter).start()
time.sleep(1)
event.set()               # wake the waiter

# ThreadPoolExecutor (recommended for I/O pools)
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    import urllib.request
    with urllib.request.urlopen(url) as r:
        return r.read()

urls = ['https://httpbin.org/get'] * 3
with ThreadPoolExecutor(max_workers=5) as ex:
    futures = [ex.submit(fetch, u) for u in urls]
    results = [f.result() for f in futures]
```

---

### `multiprocessing` — Process-Based Parallelism

**Use cases:** CPU-bound tasks — image processing, data crunching, ML training.

```python
from multiprocessing import Pool, Process, Queue, cpu_count
import os

print(f'CPUs: {cpu_count()}')

# Pool map — distribute work across CPUs
def square(n):
    return n * n

with Pool(processes=4) as pool:
    results = pool.map(square, range(10))    # [0, 1, 4, 9, ...]

# Async pool
with Pool() as pool:
    async_result = pool.map_async(square, range(100))
    output = async_result.get(timeout=10)

# Shared Queue between processes
def producer(q):
    for i in range(5):
        q.put(i)
    q.put(None)   # sentinel

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f'PID {os.getpid()} consumed {item}')

q = Queue()
p1 = Process(target=producer, args=(q,))
p2 = Process(target=consumer, args=(q,))
p1.start(); p2.start()
p1.join();  p2.join()
```

---

### `asyncio` — Async / Await Concurrency ⭐

**Use cases:** High-concurrency I/O — web servers, WebSockets, APIs.

```python
import asyncio
import aiohttp   # pip install aiohttp

# Basic coroutines
async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f'Hello, {name}!')

async def main():
    # Run concurrently
    await asyncio.gather(
        greet('Alice', 1),
        greet('Bob',   2),
        greet('Carol', 0.5),
    )

asyncio.run(main())

# HTTP with aiohttp
async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, u) for u in urls]
        return await asyncio.gather(*tasks)

# asyncio Queue (producer-consumer)
async def producer(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'Got {item}')
        queue.task_done()

async def run():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

# Timeout
async def slow_op():
    await asyncio.sleep(10)

async def with_timeout():
    try:
        async with asyncio.timeout(3):
            await slow_op()
    except asyncio.TimeoutError:
        print('Operation timed out')
```

---

## 9. Networking

### `urllib` — URL Handling (Standard Library)

```python
from urllib import request, parse, error

# GET
with request.urlopen('https://httpbin.org/get') as resp:
    body = resp.read().decode('utf-8')

# POST with data
data = parse.urlencode({'key': 'value'}).encode()
req = request.Request('https://httpbin.org/post', data=data, method='POST')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
with request.urlopen(req) as resp:
    print(resp.status, resp.reason)

# URL parsing
from urllib.parse import urlparse, urlencode, urljoin, quote

parsed = urlparse('https://api.example.com/v1/users?page=2&limit=20')
print(parsed.scheme)    # https
print(parsed.netloc)    # api.example.com
print(parsed.path)      # /v1/users
print(parsed.query)     # page=2&limit=20

# Build URL with query string
base = 'https://api.example.com/search?'
params = {'q': 'python async', 'page': 1, 'sort': 'date'}
url = base + urlencode(params)

# Encode path segments
safe_name = quote('São Paulo/Brasil')
```

---

## 10. Logging & Debugging

### `logging` — Application Logging ⭐

**Use cases:** Production logging, structured logs, file rotation.

```python
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# Basic setup
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

logger = logging.getLogger(__name__)

logger.debug('Verbose detail for debugging')
logger.info('Normal application events')
logger.warning('Unexpected but recoverable')
logger.error('Serious issue — function failed')
logger.critical('System-level failure')

# Exception logging (includes traceback)
try:
    1 / 0
except ZeroDivisionError:
    logger.exception('Division failed')

# Structured setup for production
def setup_logging(level='INFO', log_file='app.log'):
    fmt = logging.Formatter(
        '%(asctime)s %(levelname)-8s %(name)-20s %(message)s'
    )

    root = logging.getLogger()
    root.setLevel(getattr(logging, level))

    # Console
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    root.addHandler(ch)

    # File with rotation (10 MB, keep 5 backups)
    fh = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    fh.setFormatter(fmt)
    root.addHandler(fh)

# Suppress noisy libraries
logging.getLogger('urllib3').setLevel(logging.WARNING)

# Per-module loggers (best practice)
# Each module: logger = logging.getLogger(__name__)
```

---

### `traceback` — Stack Trace Utilities

```python
import traceback

try:
    raise ValueError('Something broke')
except Exception:
    # Print to stderr
    traceback.print_exc()

    # Capture as string
    tb_str = traceback.format_exc()

    # Structured info
    exc_type, exc_value, exc_tb = sys.exc_info()
    frames = traceback.extract_tb(exc_tb)
    for frame in frames:
        print(f'{frame.filename}:{frame.lineno} in {frame.name}')
        print(f'  {frame.line}')
```

---

## 11. Type System

### `typing` — Type Hints ⭐

**Use cases:** Documentation, IDE auto-complete, mypy/pyright static analysis.

```python
from typing import (
    Any, Optional, Union, List, Dict, Tuple, Set,
    Callable, Iterator, Generator, TypeVar, Generic,
    ClassVar, Final, Literal, TypedDict, Protocol
)

# Basic hints
def greet(name: str, times: int = 1) -> str:
    return (f'Hello, {name}! ' * times).strip()

# Optional (value or None)
def find_user(user_id: int) -> Optional[dict]:
    return None

# Union (multiple types)  — Python 3.10+ can use int | str
def process(value: Union[int, str]) -> str:
    return str(value)

# Containers
def summarize(items: List[int]) -> Dict[str, float]:
    return {'mean': sum(items) / len(items)}

# Callable
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# TypeVar for generics
T = TypeVar('T')

def first(items: List[T]) -> Optional[T]:
    return items[0] if items else None

# TypedDict — typed dict shapes
class UserProfile(TypedDict):
    name: str
    age: int
    email: Optional[str]

# Literal — restrict to specific values
def set_log_level(level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR']) -> None:
    pass

# Protocol — structural subtyping (duck typing with types)
class Drawable(Protocol):
    def draw(self) -> None: ...

# Final — constant
MAX_RETRIES: Final = 3
```

---

### `dataclasses` — Data Classes ⭐

**Use cases:** DTOs, value objects, configuration classes.

```python
from dataclasses import dataclass, field, asdict, astuple, replace
from typing import List, Optional

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: 'Point') -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

@dataclass(frozen=True)   # immutable (hashable)
class Color:
    r: int
    g: int
    b: int

    def __post_init__(self):
        for v in (self.r, self.g, self.b):
            if not 0 <= v <= 255:
                raise ValueError(f'RGB value {v} out of range')

@dataclass
class Config:
    host: str = 'localhost'
    port: int = 8080
    debug: bool = False
    tags: List[str] = field(default_factory=list)
    _secret: str = field(default='', repr=False)   # hidden in repr

@dataclass(order=True)     # enables <, >, <= >=
class Version:
    major: int
    minor: int
    patch: int = 0

# Usage
p1 = Point(0, 0)
p2 = Point(3, 4)
print(p2.distance_to(p1))       # 5.0

c = Config(host='db.example.com', port=5432)
print(asdict(c))                # dict representation
c2 = replace(c, port=5433)     # copy with changes (immutable pattern)

v1 = Version(1, 2, 3)
v2 = Version(2, 0)
print(v1 < v2)                  # True
```

---

### `enum` — Enumerations

```python
from enum import Enum, IntEnum, Flag, auto, unique

@unique
class Status(Enum):
    PENDING  = 'pending'
    ACTIVE   = 'active'
    INACTIVE = 'inactive'
    DELETED  = 'deleted'

    @classmethod
    def from_str(cls, value: str) -> 'Status':
        try:
            return cls(value.lower())
        except ValueError:
            raise ValueError(f'{value!r} is not a valid Status')

    @property
    def is_live(self) -> bool:
        return self == Status.ACTIVE

class Permission(Flag):
    READ    = auto()
    WRITE   = auto()
    EXECUTE = auto()
    ADMIN   = READ | WRITE | EXECUTE

# Usage
s = Status.ACTIVE
print(s.value)          # 'active'
print(s.name)           # 'ACTIVE'
print(s.is_live)        # True

perm = Permission.READ | Permission.WRITE
print(Permission.READ in perm)      # True
print(Permission.EXECUTE in perm)   # False
```

---

## 12. Context Managers

### `contextlib` — Context Manager Utilities

**Use cases:** Resource management, exception suppression, timed blocks.

```python
from contextlib import contextmanager, suppress, nullcontext, ExitStack
import time

# --- Custom context manager via decorator ---
@contextmanager
def timer(label=''):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f'{label}: {elapsed:.4f}s')

with timer('DB query'):
    time.sleep(0.1)

# --- Suppress specific exceptions ---
with suppress(FileNotFoundError):
    import os
    os.remove('file_that_may_not_exist.txt')

# --- ExitStack — dynamic number of context managers ---
files_to_open = ['a.txt', 'b.txt', 'c.txt']
with ExitStack() as stack:
    handles = [stack.enter_context(open(f, 'w')) for f in files_to_open]
    for h in handles:
        h.write('hello\n')

# --- Class-based context manager ---
class DatabaseConnection:
    def __init__(self, url):
        self.url = url
        self.conn = None

    def __enter__(self):
        print(f'Connecting to {self.url}')
        self.conn = 'mock_connection'
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Closing connection')
        self.conn = None
        return False   # propagate exceptions

with DatabaseConnection('postgresql://localhost/mydb') as conn:
    print(f'Using {conn}')
```

---

## 13. CLI & Config

### `argparse` — Command-Line Argument Parsing

```python
import argparse

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='My awesome CLI tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example: python tool.py process -i data.csv -o out.json -v'
    )

    # Positional argument
    parser.add_argument('command', choices=['run', 'process', 'validate'])

    # Optional flags
    parser.add_argument('-i', '--input',  required=True,  help='Input file path')
    parser.add_argument('-o', '--output', default='out.json', help='Output file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    parser.add_argument('-n', '--count',   type=int, default=10, help='Batch size')
    parser.add_argument('--format', choices=['json','csv','xml'], default='json')

    return parser

if __name__ == '__main__':
    args = build_parser().parse_args()
    if args.verbose:
        print(f'Input: {args.input}, Output: {args.output}')
```

---

### `configparser` — INI Configuration Files

```python
import configparser

# Read
config = configparser.ConfigParser()
config.read('settings.ini')

host = config['database']['host']
port = config.getint('database', 'port', fallback=5432)
debug = config.getboolean('app', 'debug', fallback=False)

# Write
config['database'] = {
    'host': 'localhost',
    'port': '5432',
    'name': 'myapp',
}
config['app'] = {
    'debug': 'false',
    'log_level': 'INFO',
}
with open('settings.ini', 'w') as f:
    config.write(f)

# Sample settings.ini output:
# [database]
# host = localhost
# port = 5432
# name = myapp
#
# [app]
# debug = false
# log_level = INFO
```

---

## 14. Database

### `sqlite3` — Embedded SQL Database

**Use cases:** Local apps, prototyping, testing, embedded databases.

```python
import sqlite3
from contextlib import closing

DB_PATH = 'app.db'

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row    # rows as dict-like objects
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

# Schema setup
def init_db():
    with closing(get_connection()) as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT    NOT NULL,
                email   TEXT    UNIQUE NOT NULL,
                created TEXT    DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS posts (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER REFERENCES users(id),
                title   TEXT    NOT NULL,
                body    TEXT
            );
        ''')
        conn.commit()

# CRUD
def create_user(name: str, email: str) -> int:
    with closing(get_connection()) as conn:
        cur = conn.execute(
            'INSERT INTO users (name, email) VALUES (?, ?)', (name, email)
        )
        conn.commit()
        return cur.lastrowid

def get_user(user_id: int) -> dict | None:
    with closing(get_connection()) as conn:
        row = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        return dict(row) if row else None

def list_users(limit: int = 100) -> list[dict]:
    with closing(get_connection()) as conn:
        rows = conn.execute('SELECT * FROM users LIMIT ?', (limit,)).fetchall()
        return [dict(r) for r in rows]

def update_email(user_id: int, email: str):
    with closing(get_connection()) as conn:
        conn.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))
        conn.commit()

def delete_user(user_id: int):
    with closing(get_connection()) as conn:
        conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()

# Parameterized batch insert
def bulk_insert(users: list[tuple]):
    with closing(get_connection()) as conn:
        conn.executemany('INSERT INTO users (name, email) VALUES (?, ?)', users)
        conn.commit()
```

---

## 15. Compression

### `zipfile`, `gzip`, `tarfile`

```python
import zipfile, gzip, tarfile, shutil

# --- ZIP ---
# Create
with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('file.txt')
    zf.write('data/report.csv', arcname='report.csv')  # custom path in zip

# Extract
with zipfile.ZipFile('archive.zip') as zf:
    zf.extractall('output/')
    names = zf.namelist()           # list contents

# --- GZIP (single file) ---
# Compress
with open('data.json', 'rb') as fin, gzip.open('data.json.gz', 'wb') as fout:
    fout.write(fin.read())

# Decompress
with gzip.open('data.json.gz', 'rt', encoding='utf-8') as f:
    data = f.read()

# --- TAR ---
# Create .tar.gz
with tarfile.open('project.tar.gz', 'w:gz') as tar:
    tar.add('src/', arcname='src')

# Extract
with tarfile.open('project.tar.gz') as tar:
    tar.extractall('extracted/')
    tar.getmembers()               # list contents

# Quick helpers via shutil
shutil.make_archive('backup', 'gztar', 'project/')
shutil.unpack_archive('backup.tar.gz', 'restored/')
```

---

## 16. Testing

### `unittest` — Standard Testing Framework

```python
import unittest
from unittest.mock import MagicMock, patch, call

# --- Class under test ---
class Calculator:
    def add(self, a, b): return a + b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return a / b

# --- Tests ---
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        pass   # clean up

    def test_add_positive(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_divide_ok(self):
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333, places=2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_types(self):
        self.assertIsInstance(self.calc.add(1, 2), int)
        self.assertIsNone(None)
        self.assertTrue(True)
        self.assertIn(3, [1, 2, 3])

# --- Mocking ---
class TestWithMock(unittest.TestCase):
    @patch('requests.get')
    def test_api_call(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'id': 1}

        import requests
        resp = requests.get('https://api.example.com/users/1')
        self.assertEqual(resp.json()['id'], 1)
        mock_get.assert_called_once_with('https://api.example.com/users/1')

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

---

## 17. Environment & Subprocess

### `subprocess` — Run External Commands

**Use cases:** Shell commands, scripts, external processes.

```python
import subprocess

# Simple run — capture output
result = subprocess.run(
    ['ls', '-la'],
    capture_output=True,
    text=True,
    check=True          # raises CalledProcessError on non-zero exit
)
print(result.stdout)
print(result.returncode)   # 0

# Shell command (use cautiously, never with user input)
result = subprocess.run('echo $HOME', shell=True, capture_output=True, text=True)

# Streaming output (long-running processes)
with subprocess.Popen(
    ['ping', '-c', '4', 'google.com'],
    stdout=subprocess.PIPE,
    text=True
) as proc:
    for line in proc.stdout:
        print(line, end='')

# Pipe stdin
proc = subprocess.run(
    ['python3', '-c', 'import sys; print(sys.stdin.read().upper())'],
    input='hello world',
    capture_output=True,
    text=True
)
print(proc.stdout)   # HELLO WORLD

# Environment variables
import os
env = {**os.environ, 'MY_VAR': 'my_value'}
subprocess.run(['env'], env=env)
```

---

## Quick Reference Cheatsheet

| Module         | Category        | Key Use Case                              |
|---------------|-----------------|-------------------------------------------|
| `pathlib`     | File System     | Modern cross-platform path manipulation   |
| `os`          | File System     | OS operations, env vars, process info     |
| `shutil`      | File System     | Copy, move, archive entire trees          |
| `json`        | Serialization   | JSON encode/decode, APIs, configs         |
| `csv`         | Serialization   | Tabular data import/export                |
| `pickle`      | Serialization   | Python-native object persistence          |
| `datetime`    | Date/Time       | Dates, times, arithmetic, formatting      |
| `re`          | Text            | Pattern matching, validation, parsing     |
| `collections` | Data Structures | Counter, deque, defaultdict, namedtuple   |
| `itertools`   | Iteration       | Combinatorics, lazy iteration             |
| `functools`   | Functions       | Caching, partial application, decorators  |
| `threading`   | Concurrency     | I/O-bound parallel tasks                  |
| `asyncio`     | Concurrency     | Async/await, high-concurrency I/O         |
| `multiprocessing` | Concurrency | CPU-bound parallel tasks                 |
| `logging`     | Observability   | Structured application logging            |
| `typing`      | Types           | Type hints for static analysis            |
| `dataclasses` | Types           | Boilerplate-free data containers          |
| `enum`        | Types           | Named constants and flags                 |
| `contextlib`  | Resources       | Context managers, exception suppression   |
| `argparse`    | CLI             | Command-line argument parsing             |
| `sqlite3`     | Database        | Embedded SQL database                     |
| `unittest`    | Testing         | Unit tests and mocking                    |
| `subprocess`  | OS Integration  | Run external commands/scripts             |
| `zipfile`     | Compression     | ZIP archive creation and extraction       |

---

> **Python Docs:** https://docs.python.org/3/library/  
> **Real Python Tutorials:** https://realpython.com  
> **Type Checking:** Use `mypy` or `pyright` for static analysis.  
> **Code Quality:** Use `ruff` for linting, `black` for formatting.
