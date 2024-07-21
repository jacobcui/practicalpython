# How to Install Python on Windows, Linux, and macOS

## Windows

1. **Download the Installer:**
   - Go to the official Python website: [python.org](https://www.python.org/).
   - Navigate to the "Downloads" tab and click on "Python 3.x.x" (where "x.x" is the latest version number).

2. **Run the Installer:**
   - Once the installer is downloaded, run it.
   - Make sure to check the box that says "Add Python 3.x to PATH" before clicking "Install Now".

3. **Verify Installation:**
   - Open Command Prompt by pressing `Win + R`, typing `cmd`, and pressing `Enter`.
   - Type `python --version` and press `Enter` to verify the installation.

## Linux (Ubuntu/Debian)

1. **Update Package List:**
   - Open a terminal and run:
     ```bash
     sudo apt update
     ```

2. **Install Python:**
   - Run the following command to install Python 3:
     ```bash
     sudo apt install python3
     ```

3. **Verify Installation:**
   - Type `python3 --version` in the terminal to verify the installation.

## macOS

1. **Install Homebrew (if not already installed):**
   - Open a terminal and run:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. **Install Python:**
   - Once Homebrew is installed, run:
     ```bash
     brew install python
     ```

3. **Verify Installation:**
   - Type `python3 --version` in the terminal to verify the installation.