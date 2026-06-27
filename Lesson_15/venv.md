# Python Virtual Environment Guide

## What Is a Virtual Environment?

A virtual environment is an isolated Python workspace that contains its own:

* Python packages
* Dependencies
* Package versions

This allows each project to use different package versions without affecting other projects on your computer.

---

## Why Use Virtual Environments?

### 1. Avoid Dependency Conflicts

Different projects may require different versions of the same package.

Example:

Project A requires:

```bash
Django==4.2
```

Project B requires:

```bash
Django==5.1
```

Without virtual environments, installing one version could break the other project.

---

### 2. Keep the Global Python Installation Clean

Installing packages globally can quickly clutter your system.

Instead of:

```bash
pip install requests
```

for every project, install packages only inside the project's environment.

---

### 3. Improve Reproducibility

You can save all project dependencies into a file and allow others to recreate the exact same environment.

---

### 4. Follow Industry Best Practices

Virtual environments are standard practice in professional Python development.

---

# Recommended Method: venv

Python includes a built-in tool called `venv`.

Benefits:

* Included with Python
* No extra installation required
* Lightweight
* Works on Windows, macOS, and Linux
* Recommended for most projects

---

# Creating a Virtual Environment

## 1. Navigate to Your Project

```bash
cd my_project
```

---

## 2. Create the Environment

```bash
python3 -m venv .venv
```

This creates a directory named `.venv`.

Project structure:

```text
my_project/
│
├── .venv/
├── app.py
└── requirements.txt
```

Using `.venv` is a common convention because many editors automatically recognize it.

---

# Activating the Environment

## macOS / Linux

```bash
source .venv/bin/activate
```

You should see:

```text
(.venv) $
```

---

## Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

---

## Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

---

# Installing Packages

Example:

```bash
pip install requests
```

Verify installation:

```bash
pip list
```

---

# Saving Installed Packages

To save all installed packages:

```bash
pip freeze > requirements.txt
```

Example output:

```text
requests==2.32.4
urllib3==2.5.0
charset-normalizer==3.4.3
```

This file allows anyone to recreate the environment.

---

# Installing Packages From requirements.txt

After cloning the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

This installs all required dependencies automatically.

---

# Deactivating the Environment

When finished:

```bash
deactivate
```

You will return to your normal system Python.

---

# Best Practices

### Use `.venv` as the Environment Name

```bash
python3 -m venv .venv
```

---

### Never Commit the Virtual Environment

Add this to `.gitignore`:

```gitignore
.venv/
```

The environment can always be recreated from `requirements.txt`.

---

### Save Dependencies Regularly

Whenever you install or update packages:

```bash
pip freeze > requirements.txt
```

---

# Quick Start

```bash
# Create project folder
mkdir my_project
cd my_project

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install packages
pip install requests

# Save dependencies
pip freeze > requirements.txt

# Leave environment
deactivate
```

---

# Summary

```bash
# Create
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Install package
pip install package_name

# Save dependencies
pip freeze > requirements.txt

# Install dependencies later
pip install -r requirements.txt

# Deactivate
deactivate
```

For most Python projects, `venv` + `requirements.txt` is the simplest and most widely accepted solution.
# Additional Section: Working with `requirements.txt`

## What Is `requirements.txt`?

A `requirements.txt` file contains a list of all Python packages required by a project.

Example:

```text
requests==2.32.4
pandas==2.3.1
numpy==2.3.2
```

This allows anyone working on the project to install the exact dependencies needed.

---

## Creating a `requirements.txt` File

### Option 1: Save All Installed Packages (Recommended)

After installing packages in your virtual environment:

```bash
pip freeze > requirements.txt
```

Example:

```bash
pip install requests pandas
pip freeze > requirements.txt
```

Generated file:

```text
pandas==2.3.1
requests==2.32.4
numpy==2.3.2
python-dateutil==2.9.0
pytz==2025.2
```

---

### Option 2: Create It Manually

You can create the file yourself:

```text
requests==2.32.4
pandas==2.3.1
```

Save it as:

```text
requirements.txt
```

This approach is useful for small projects where you want full control over the dependencies.

---

## Installing Dependencies from an Existing `requirements.txt`

When you clone or download a Python project, the repository often contains a `requirements.txt` file.

### Step 1: Navigate to the Project

```bash
cd my_project
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv .venv
```

### Step 3: Activate the Virtual Environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 4: Install the Dependencies

```bash
pip install -r requirements.txt
```

The `-r` flag means "read package names from this file."

---

## Complete Example

Project structure:

```text
my_project/
│
├── .venv/
├── app.py
└── requirements.txt
```

Contents of `requirements.txt`:

```text
requests==2.32.4
pandas==2.3.1
```

Install everything:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

## Updating `requirements.txt`

After installing new packages:

```bash
pip install flask
```

Update the file:

```bash
pip freeze > requirements.txt
```

Commit the updated file to version control so other developers can install the new dependency.

---

## Typical Workflow

### Creating a New Project

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install requests pandas

pip freeze > requirements.txt
```

### Working on an Existing Project

```bash
git clone <repository>

cd project

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Most Important Commands

```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Save installed packages
pip freeze > requirements.txt

# Install packages from requirements file
pip install -r requirements.txt

# Show installed packages
pip list

# Deactivate environment
deactivate
```
