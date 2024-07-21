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

## Starting a Jupyter Notebook in VS Code

1. **Install Python Extension:**
   - Open VS Code.
   - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
   - Search for "Python" and install the extension by Microsoft.

2. **Install Jupyter Extension:**
   - In the Extensions view, search for "Jupyter" and install the extension by Microsoft.

3. **Create or Open a Python File:**
   - Open a folder where you want to work.
   - Create a new file with a `.py` extension (e.g., `notebook.py`).

4. **Start a Jupyter Notebook:**
   - Open the Command Palette by pressing `Ctrl+Shift+P`.
   - Type "Jupyter: Create New Blank Notebook" and select it.
   - A new Jupyter Notebook will open in VS Code.

5. **Run Cells:**
   - You can now write Python code in the cells and run them by pressing `Shift+Enter`.

That's it! You have successfully installed VS Code and started a Jupyter Notebook within it.