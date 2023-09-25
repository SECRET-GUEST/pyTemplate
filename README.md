```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ████████╗███████╗███╗   ███╗██████╗ ██╗      █████╗ ████████╗███████╗███████╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██║     ██╔══██╗╚══██╔══╝██╔════╝██╔════╝
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║       ██║   █████╗  ██╔████╔██║██████╔╝██║     ███████║   ██║   █████╗  ███████╗
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║       ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══██║   ██║   ██╔══╝  ╚════██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║       ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗██║  ██║   ██║   ███████╗███████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝
```
![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Batch Script](https://img.shields.io/badge/Batch-Script-blue)

# Python Templates 🐍

Python Templates is a versatile repository designed to automate the process of creating and compiling Python applications across different operating systems. This tool ensures the smooth integration of different scripts to offer an optimal user experience, featuring real-time internationalization through a dynamic translation file.

This repository contains different branches for various operating systems:
- `windows` for Windows-specific templates.
- `nautilus` for Linux (Nautilus file manager) specific templates.

The `main` branch serves as a general example. For a more streamlined and customized experience, it is recommended to clone the specific branches.


## 🌟 Features
- Real-time internationalization through an integrated translation file.
- Seamless integration of different scripts for streamlined operation.
- Pre-packaged Python application templates.

## 🔍 Prerequisites
Before you begin, ensure you have met the following requirements:
- [Python 3.10](https://www.python.org/downloads/) or higher installed.

Windows users 
- [Inno Setup](http://www.jrsoftware.org/isdl.php) installed for building setup files on Windows.
- [PyInstaller](https://pyinstaller.readthedocs.io/) for packaging the Python applications.


## 💎 Recommendations

- For Linux users, check out this [repository](https://github.com/SECRET-GUEST/actions-for-nautilus) to effortlessly create actions in Nautilus, enabling repository creation and cloning with a single click, given that git is installed on your system.


## 📌 Quick Start

### Linux users

Leveraging the [Actions for Nautilus](https://github.com/SECRET-GUEST/actions-for-nautilus) repository allows for the creation of customized actions, including easy cloning of this repository with just one click, provided Git is installed on your system.

### Windows users

You can just clone the `windows` branch:

```shell
git clone https://github.com/SECRET-GUEST/pyTemplate.git --branch windows
```

you can also use a batch script to make a **one-click installer** for anytime you need to clone :

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



## ❓ Support & Questions

For any queries or support needs, please feel free to open an issue or start a discussion. 

## 📜 License

This project is licensed under the [MIT License](LICENSE).

