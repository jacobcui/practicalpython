# How to Install Visual Studio Code (VS Code) and Start a Jupyter Notebook

## Installing Visual Studio Code (VS Code)

### Windows

1. **Download the Installer:**
   - Go to the official VS Code website: [code.visualstudio.com](https://code.visualstudio.com/).
   - Click on the "Download for Windows" button.

2. **Run the Installer:**
   - Once the installer is downloaded, run it.
   - Follow the on-screen instructions to complete the installation.

### Linux (Ubuntu/Debian)

1. **Download the Installer:**
   - Open a terminal and run:
     ```bash
     sudo apt update
     sudo apt install software-properties-common apt-transport-https wget
     wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
     sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
     sudo apt update
     sudo apt install code
     ```

### macOS

1. **Download the Installer:**
   - Go to the official VS Code website: [code.visualstudio.com](https://code.visualstudio.com/).
   - Click on the "Download for Mac" button.

2. **Run the Installer:**
   - Once the installer is downloaded, open the downloaded file and drag the Visual Studio Code app to the Applications folder.
