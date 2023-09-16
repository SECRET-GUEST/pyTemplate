![Python](https://img.shields.io/badge/Python-3.10+-blue)

```
██████╗ ██╗   ██╗██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗  ██╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗███║
██████╔╝ ╚████╔╝ ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝╚██║
██╔═══╝   ╚██╔╝  ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗ ██║
██║        ██║   ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║ ██║
╚═╝        ╚═╝   ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═╝
                                                                         
```

![Batch Script](https://img.shields.io/badge/Batch-Script-blue)


# Builder1 🛠️

Builder1 is a robust tool that automates the process of creating and compiling Python applications, featuring real-time internationalization through a dynamic translation file. This tool integrates batch and Python scripts to deliver an optimal user experience.

Here : [some explanations on installers with pyinstaller](https://github.com/SECRET-GUEST/tiny-scripts/tree/ALL/python/INSTALLER)

---
---
---

## 📋 Table of Contents

1. [Features](#-features)
2. [Prerequisites](#-prerequisites)
3. [Usage](#-usage)
4. [License](#-license)
5. [Support & Questions](#-support--questions)
6. [Recommendations](#-recommendations)

## 🌟 Features

- Automatic setup file creation with Inno Setup
- Real-time console message translation through an integrated translation class
- Seamless integration with batch scripts for streamlined operation
- Pre-packaged Python application template in the `scripts` directory

## 🔍 Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python 3.10](https://www.python.org/downloads/) or higher installed
- [Inno Setup](http://www.jrsoftware.org/isdl.php) installed for building setup files
- [PyInstaller](https://pyinstaller.readthedocs.io/) for packaging the Python applications


## 📜 License

This repository is released under the [MIT License](LICENSE). Please see the `LICENSE` file for more information.


## ❓ Support & Questions

If you have any questions or need support, please feel free to open an issue, a new discussion, or join my twitter.


## 💎 Recommendations  

In your quest for more tools to enhance your desktop productivity, these additional repositories are worth a look:


- [Font Lister](https://github.com/SECRET-GUEST/font_lister) : This tool can list your fonts in a PDF, complete with images.
- [Silence](https://github.com/SECRET-GUEST/silence) : A Python tool that rapidly eliminates all comments from a page.
- [Themes](https://github.com/SECRET-GUEST/themes) : A collection of themes you can use in Python and other contexts.
- [LogInfo](https://github.com/SECRET-GUEST/logInfo) : Facilitate Python programming with effective error handling.

Looking for more? Discover user-friendly, GUI-free script here: 
- [Tiny Scripts](https://github.com/SECRET-GUEST/tiny-scripts)



---


## Git Repository Cloning Batch Script 📦

The batch script below assists in cloning a specific git repository. Before running the script, ensure that Git is installed on your system. You can get it from [Git's official site](https://git-scm.com/). 

Here is a brief explanation of the script:

1. It first checks whether Git is installed on your system.
2. If Git is installed, it proceeds to clone the 'main' branch of the specified repository (in this case, the pyTemplate repository).
3. If an error occurs at any point (like Git not being installed or the repository failing to clone), it displays an appropriate error message.

```batch
@echo off
:: Check if git is installed
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Git is not installed. Please install it from https://git-scm.com/ to proceed.
    exit /b 1
)

:: Clone the repository
git clone https://github.com/SECRET-GUEST/pyTemplate.git -b main

if %errorlevel% neq 0 (
    echo An error occurred while cloning the repository.
    exit /b 1
)

echo The repository was cloned successfully.
exit /b 0
```

Save this script as a `.bat` file and execute it to clone the repository. Once the repository is cloned successfully, a confirmation message will be displayed.




