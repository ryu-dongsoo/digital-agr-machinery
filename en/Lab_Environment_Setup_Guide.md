# 🛠️ Lab Environment Setup Guide

> **Course:** Introduction to Digital Agricultural Machinery  
> **Instructor:** Dongsoo Ryu (Jeonbuk National University, Dept. of Biosystems Machinery Engineering)  
> **Last Updated:** 2026-05-17

---

## 📋 Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Python Installation](#2-python-installation)
3. [VS Code Installation & Configuration](#3-vs-code-installation--configuration)
4. [Git Installation & GitHub Account](#4-git-installation--github-account)
5. [Download Lab Materials](#5-download-lab-materials)
6. [Python Package Installation](#6-python-package-installation)
7. [Running Lab Code](#7-running-lab-code)
8. [Lab Report Submission (GitHub Issue)](#8-lab-report-submission-github-issue)
9. [FAQ & Troubleshooting](#9-faq--troubleshooting)

---

## 1. Prerequisites

### Required Software

| Software | Purpose | Download |
|----------|---------|----------|
| **Python 3.11+** | Run lab scripts | [python.org](https://www.python.org/downloads/) |
| **VS Code** | Code editor | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Git** | Version control & material download | [git-scm.com](https://git-scm.com/) |

### Recommended Environment

- **OS**: Windows 10 or Windows 11
- **Internet**: Stable Wi-Fi or wired connection required
- **Storage**: Minimum 2GB free space recommended

---

## 2. Python Installation

### 2.1 Download

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the **"Download Python 3.x.x"** button at the top

> 📸 *Click the yellow download button as shown below*
> ```
> ┌─────────────────────────────────────────┐
> │  Download Python 3.13.x                 │
> │  [████ Download Python 3.13.x ████]     │
> └─────────────────────────────────────────┘
> ```

### 2.2 Install

1. Run the downloaded installer (`python-3.x.x-amd64.exe`)
2. ⚠️ **MUST check "Add python.exe to PATH"** (Most important step!)
3. Click **"Install Now"**

> 📸 *Checkbox location at the bottom of the install screen*
> ```
> ┌─────────────────────────────────────────┐
> │  Install Python 3.13.x                  │
> │                                         │
> │  [Install Now]                          │
> │  [Customize installation]               │
> │                                         │
> │  ☑ Use admin privileges                 │
> │  ☑ Add python.exe to PATH  ← ⚠️ MUST!  │
> └─────────────────────────────────────────┘
> ```

### 2.3 Verify Installation

- Open **Command Prompt** (search "cmd" in Windows)
- Type the following command; if a version number appears, installation is successful:

```bash
python --version
```

- Expected output:
```
Python 3.13.3
```

> ❌ If you see `'python' is not recognized as an internal or external command...`
> → See [FAQ 9.1](#91-python-command-not-recognized)

---

## 3. VS Code Installation & Configuration

### 3.1 Download & Install

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click **"Download for Windows"** → Run the installer
3. Recommended installation options:
   - ☑ `Add "Open with Code" action to Windows Explorer file context menu`
   - ☑ `Add to PATH`

### 3.2 Install Required Extensions

- Open VS Code → Click **Extensions** icon in the left sidebar (or press `Ctrl+Shift+X`)
- Search and install the following extensions:

| Extension | Description | Required |
|-----------|-------------|----------|
| **Python** (Microsoft) | Python code execution & debugging | ✅ Required |
| **Jupyter** | Notebook execution (optional) | Optional |
| **Markdown Preview Enhanced** | Report preview | Recommended |

> 📸 *Extensions panel — Search "Python" and click Install*
> ```
> ┌──────────────────────────────────────────┐
> │  🔍 Python                               │
> │  ┌────────────────────────────────────┐  │
> │  │  ★ Python (Microsoft)             │  │
> │  │  IntelliSense, Linting, Debugging │  │
> │  │  [Install]                         │  │
> │  └────────────────────────────────────┘  │
> └──────────────────────────────────────────┘
> ```

### 3.3 Select Python Interpreter

1. Open any `.py` file in VS Code
2. Click the **Python version** in the bottom status bar
3. Select the installed Python 3.x version

> 📸 *Python interpreter selection in the bottom status bar*
> ```
> ┌──────────────────────────────────────────┐
> │  Status Bar (bottom)                      │
> │  ... Python 3.13.3 64-bit ← Click here   │
> └──────────────────────────────────────────┘
> ```

### 3.4 Gemini AI Coding Assistant (Google Account Required)

- Get AI-powered code assistance in VS Code (free)
- **Installation**:
  1. Extensions panel (`Ctrl+Shift+X`) → Search **"Gemini Code Assist"** → **Install**
  2. After installation, a **✦ Gemini icon** appears in the left sidebar
  3. Click the icon → **"Sign in with Google"** → Sign in with your Google account
  4. Once signed in, ask code questions in the chat panel

> 📸 *Gemini extension installation*
> ```
> ┌──────────────────────────────────────────┐
> │  🔍 Gemini Code Assist                   │
> │  ┌────────────────────────────────────┐  │
> │  │  ✦ Gemini Code Assist (Google)    │  │
> │  │  AI-powered coding assistant      │  │
> │  │  [Install]                         │  │
> │  └────────────────────────────────────┘  │
> └──────────────────────────────────────────┘
> ```

- **Usage Examples**:
  - Ask about errors: "Why is this error occurring?"
  - Explain code: Select code → Right-click → **"Gemini: Explain this"**
  - Generate code: Describe desired functionality in the chat

### 3.5 VS Code Panel Toggle (Keyboard Shortcuts)

| Function | Shortcut | Description |
|----------|----------|-------------|
| **Explorer** (File Tree) | `Ctrl+B` | Toggle left sidebar |
| **Terminal** | `` Ctrl+` `` | Toggle bottom terminal panel |
| **Gemini AI Chat** | `Ctrl+Shift+I` | Toggle Gemini chat panel |
| **Problems/Output** | `Ctrl+Shift+M` | Toggle problems panel |
| **Extensions** | `Ctrl+Shift+X` | Open extensions panel |
| **Command Palette** | `Ctrl+Shift+P` | Search all commands (most important!) |

> 📸 *VS Code layout overview*
> ```
> ┌────────────┬──────────────────────┬──────────┐
> │            │                      │          │
> │  Explorer  │    Editor Area       │  Gemini  │
> │  (Ctrl+B)  │    (Code Editing)    │  AI Chat │
> │            │                      │          │
> │            │                      │          │
> ├────────────┴──────────────────────┴──────────┤
> │        Terminal / Problems (Ctrl+`)           │
> └──────────────────────────────────────────────┘
> ```

### 3.6 Markdown Preview / Edit Mode Toggle

- Lab manuals (`.md` files) appear as raw code when opened
- **Preview (rendered document view)**:
  - Click the **📖 Preview icon** at the top-right of the editor
  - Or press `Ctrl+Shift+V` (full-screen preview)
  - Or press `Ctrl+K V` (side-by-side preview)

| Mode | Shortcut | Description |
|------|----------|-------------|
| **Preview** (read) | `Ctrl+Shift+V` | View rendered document |
| **Side-by-Side** | `Ctrl+K V` | Left: edit, Right: preview |
| **Edit** (write) | Double-click file | Edit markdown source |

> 💡 **Tip**: Use `Ctrl+K V` side-by-side mode when writing reports to see real-time rendering

### 3.7 Other Useful Shortcuts

| Function | Shortcut |
|----------|----------|
| **Quick File Open** | `Ctrl+P` |
| **Save** | `Ctrl+S` |
| **Undo / Redo** | `Ctrl+Z` / `Ctrl+Y` |
| **Toggle Comment** | `Ctrl+/` |
| **Duplicate Line** | `Shift+Alt+↓` |
| **Multi-cursor Edit** | `Alt+Click` (desired positions) |
| **Global Search** | `Ctrl+Shift+F` |
| **Open Settings** | `Ctrl+,` |

---

## 4. Git Installation & GitHub Account

### 4.1 Install Git

1. Go to [https://git-scm.com/](https://git-scm.com/) → Click **"Download for Windows"**
2. Run the installer → Keep all options as **default (Next)**
3. Verify installation:

```bash
git --version
```

- Expected output:
```
git version 2.47.1.windows.1
```

### 4.2 Create a GitHub Account

1. Go to [https://github.com/](https://github.com/)
2. Click **"Sign up"**
3. Enter the following information:

| Field | Example |
|-------|---------|
| **Email** | Your school or personal email |
| **Password** | 8+ characters, alphanumeric |
| **Username** | `hong-gildong-2024` (English, easy to remember) |

4. Complete email verification to activate your account

### 4.3 Configure Git User Info

- Open the VS Code terminal (`Ctrl+`` ` or Menu → Terminal → New Terminal) and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

> ⚠️ **Use the same name and email as your GitHub account**

### 4.4 Sign in to GitHub from VS Code

1. Click the **person icon** at the bottom-left of VS Code
2. Select **"Sign in to Sync Settings"** or **"Sign in with GitHub"**
3. Complete GitHub authentication in the browser

---

## 5. Download Lab Materials

### Method A: Git Clone (Recommended ⭐)

- Run the following command in the VS Code terminal:

```bash
git clone https://github.com/ryu-dongsoo/digital-agr-machinery.git
```

- A folder named `digital-agr-machinery` will be created
- VS Code → **File → Open Folder** → Select the folder

### Method B: ZIP Download (If unfamiliar with Git)

1. Go to [https://github.com/ryu-dongsoo/digital-agr-machinery](https://github.com/ryu-dongsoo/digital-agr-machinery)
2. Click the green **"<> Code"** button
3. Select **"Download ZIP"**

> 📸 *ZIP download location on GitHub*
> ```
> ┌──────────────────────────────┐
> │  <> Code ▼                   │
> │  ┌────────────────────────┐  │
> │  │ Clone: HTTPS / SSH     │  │
> │  │ Open with GitHub Desk  │  │
> │  │ Download ZIP ← Click   │  │
> │  └────────────────────────┘  │
> └──────────────────────────────┘
> ```

4. Extract the ZIP file → Open folder in VS Code

### Update Materials (Before Each Week's Class)

- If already cloned, get the latest materials:

```bash
git pull origin main
```

- If downloaded as ZIP → Re-download each week

### Folder Structure

```
digital-agr-machinery/
├── ko/                    ← Korean lab materials
│   ├── week2/             ← Week 2
│   ├── week3/             ← Week 3
│   ├── ...
│   ├── week14/            ← Week 14
│   ├── QUIZ_BANK.md       ← Quiz Bank
│   └── README.md          ← Lab Index
└── en/                    ← English version
```

---

## 6. Python Package Installation

### 6.1 Required Packages (Common for All Weeks)

- Most weekly labs use `numpy` and `matplotlib`
- Run in VS Code terminal:

```bash
pip install numpy matplotlib
```

### 6.2 Week-Specific Additional Packages

| Week | Packages Used | Install Command | Notes |
|:---:|-----------|----------|------|
| **02** | `numpy`, `matplotlib` | *(Common packages only)* | TCO economic analysis |
| **03** | *(No additional packages)* | — | Standard library only (CAN decoding) |
| **04** | `numpy`, `matplotlib` | *(Common packages only)* | GNSS trilateration, RTK, path planning |
| **05** | `rasterio` | `pip install rasterio` | GeoTIFF image processing (NDVI) |
| **06** | `numpy`, `matplotlib` | *(Common packages only)* | 3D Point Cloud (mpl_toolkits built-in) |
| **07** | — | — | Arduino `.ino` files (no Python) |
| **09** | `geopandas`, `shapely` | `pip install geopandas shapely` | GeoJSON prescription map generation |
| **10** | `numpy`, `matplotlib` | *(Common packages only)* | UAV flight animation |
| **11** | `numpy`, `matplotlib` | *(Common packages only)* | Pure Pursuit path tracking |
| **12** | `numpy`, `matplotlib` | *(Common packages only)* | Kinematics, soft gripper |
| **13** | `opencv-python`, `tensorflow` | `pip install opencv-python tensorflow` | AI model loading & inference |
| **13** | `ultralytics` | `pip install ultralytics` | YOLO object detection (optional) |
| **14** | — | — | Theory/analysis only (no code) |

### 6.3 Bulk Installation (All packages at once)

```bash
pip install numpy matplotlib rasterio geopandas shapely opencv-python tensorflow ultralytics
```

### 6.4 Verify Installation

```bash
python -c "import numpy; import matplotlib; print('Installation successful!')"
```

- If `Installation successful!` is printed, setup is complete

> ❌ If you encounter errors → See [FAQ 9.2](#92-pip-install-errors)

---

## 7. Running Lab Code

### 7.1 Basic Execution

1. Open the relevant week's folder in VS Code (e.g., `ko/week12/`)
2. Open the `.py` file to run (e.g., `step0_kinematics_sim.py`)
3. Choose one of the following methods:

| Method | Action |
|--------|--------|
| **Button** | Click `▶` (Run) button at the top-right |
| **Shortcut** | `Ctrl+F5` (Run without debugging) |
| **Terminal** | Type `python step0_kinematics_sim.py` |

> 📸 *Run button location in VS Code*
> ```
> ┌─────────────────────────────────────────────┐
> │  step0_kinematics_sim.py        ▶ ← Click  │
> │  ─────────────────────────────────────────  │
> │  import numpy as np                         │
> │  import matplotlib.pyplot as plt            │
> │  ...                                        │
> └─────────────────────────────────────────────┘
> ```

### 7.2 Lab Workflow

1. Read the **lab manual (`*.md` file)** for the relevant week first
2. Run scripts in order: `step0_xxx.py` → `step1_xxx.py` → ...
3. Modify parameters as instructed and observe results
4. Capture screenshots (`Win+Shift+S`) → Attach to report

---

## 8. Lab Report Submission (GitHub Issue)

### 8.1 Submission Overview

- Lab reports are submitted via **GitHub Issues**
- Write the report using the weekly template (`.md`), then paste into an Issue

### 8.2 Submission Procedure

#### Step 1: Write the Report

- Refer to the report template in the relevant week's folder (e.g., `12주차_실습_결과_보고서_양식.md`)
- Copy the template in VS Code and fill in your content

#### Step 2: Go to GitHub Issues Page

1. Go to [https://github.com/ryu-dongsoo/digital-agr-machinery/issues](https://github.com/ryu-dongsoo/digital-agr-machinery/issues)
2. Click **"New issue"**

> 📸 *New issue button location on the Issues tab*
> ```
> ┌────────────────────────────────────────────┐
> │  Issues    Pull requests    Actions         │
> │  ──────────────────────────────────────────│
> │  🔍 Filters ▼                              │
> │                     [New issue] ← Click     │
> └────────────────────────────────────────────┘
> ```

3. If an Issue Template appears, select **"📝 Lab Report Submission"**

#### Step 3: Write Title & Content

- **Title format**:

```
[Week12] 202412345_Hong-Gildong_LabReport
```

| Field | Format | Example |
|-------|--------|---------|
| **Week** | `[WeekXX]` | `[Week12]` |
| **Student ID** | 9-digit number | `202412345` |
| **Name** | Full name | `Hong-Gildong` |
| **Type** | `LabReport` (fixed) | `LabReport` |

- **Body**: Paste your report content in Markdown format

#### Step 4: Attach Screenshots

- To attach simulation result screenshots:
  1. Capture the screen with `Win+Shift+S`
  2. **Drag & drop** or **Ctrl+V** paste into the Issue body
  3. The image URL will be automatically inserted

> 📸 *Image drag & drop area*
> ```
> ┌────────────────────────────────────────────┐
> │  Leave a comment                            │
> │  ┌──────────────────────────────────────┐  │
> │  │  Write report content here...        │  │
> │  │                                      │  │
> │  │  ┌──────────────────────────────┐    │  │
> │  │  │ 📎 Drag images here          │    │  │
> │  │  │    or paste with Ctrl+V      │    │  │
> │  │  └──────────────────────────────┘    │  │
> │  └──────────────────────────────────────┘  │
> │                           [Submit new issue]│
> └────────────────────────────────────────────┘
> ```

#### Step 5: Select Labels & Submit

- In the right-side **Labels** area, select the relevant week label (e.g., `week12`, `report`)
- Click **"Submit new issue"** to complete submission

### 8.3 Submission Checklist

- [ ] Title format: `[WeekXX] StudentID_Name_LabReport`
- [ ] All sections of the report template completed
- [ ] Simulation result screenshots attached (at least 2)
- [ ] Labels selected
- [ ] Submitted within the deadline (7 days after class)

### 8.4 Confirm Submission

- If your Issue appears in the Issues list, submission is complete
- Professor feedback will be provided via **comments** on the Issue

---

## 9. FAQ & Troubleshooting

### 9.1 Python Command Not Recognized

- **Symptom**: `'python' is not recognized as an internal or external command...`
- **Cause**: "Add python.exe to PATH" was not checked during installation
- **Solution**:
  1. Re-run the Python installer
  2. Select **"Modify"** → Check `Add Python to environment variables`
  3. Or completely uninstall and reinstall Python (ensure PATH is checked)

### 9.2 pip install Errors

- **Symptom**: `pip: command not found` or permission error
- **Solution**:
  - Use `python -m pip install package_name` instead
  - Or run VS Code terminal as **Administrator**

### 9.3 Korean Character Display Issues

- **Symptom**: Korean text in matplotlib graphs shows as □□□
- **Solution** — Add these 2 lines at the top of your code:

```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
```

### 9.4 Matplotlib Graph Window Not Opening

- **Symptom**: No graph window appears after running code
- **Solution**:
  - Check if `plt.show()` exists at the end of the code
  - Verify the correct Python interpreter is selected in VS Code

### 9.5 Git Clone Authentication Error

- **Symptom**: `Authentication failed` or `Permission denied`
- **Solution**:
  - Verify GitHub login status
  - Ensure HTTPS URL is used for `git clone`
  - Try re-signing into GitHub from VS Code

### 9.6 Cannot Create GitHub Issue

- **Symptom**: "New issue" button is disabled
- **Cause**: GitHub login required
- **Solution**: Sign in to GitHub and try again

---

## 📞 Technical Support

| Item | Contact |
|------|---------|
| **Professor** | Dongsoo Ryu (ryudongsoo@jbnu.ac.kr) |
| **Lab** | Agricultural Smart Robot Lab (ASRL), Building 4 Room 311, JBNU |
| **Repository** | [github.com/ryu-dongsoo/digital-agr-machinery](https://github.com/ryu-dongsoo/digital-agr-machinery) |

---

[← Back to Lab Index](./README.md)
