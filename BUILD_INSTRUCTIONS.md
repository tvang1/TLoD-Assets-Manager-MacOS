# TLoD Assets Manager - macOS Build Instructions

## Overview
This document outlines the steps required to package and create a macOS executable (.app) for TLoD Assets Manager.

## Prerequisites
- Python 3.11+ (installed via Homebrew or python.org)
- PyInstaller
- PIL (Pillow)

## Installation of Build Tools

### 1. Install PyInstaller
```bash
pip install pyinstaller
```

## Build Process

### Step 1: Update Code for PyInstaller Compatibility

**File: `main_gui.py`**

Modify the entry point to detect PyInstaller bundle mode and use the correct path for bundled resources:

```python
if __name__ == '__main__':
    # Get the correct base path for both development and PyInstaller bundle
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        absolute_path_current = sys._MEIPASS
    else:
        # Running in normal Python environment
        absolute_path_current = os.path.abspath(os.getcwd())
    
    absolute_path_config = f'{absolute_path_current}/Resources/Manager.config'
    absolute_path_databases = f'{absolute_path_current}/Databases'
    background_image = f'{absolute_path_current}/Resources/main.png'.replace('/', '/')
    icon_app = f'{absolute_path_current}/Resources/Dragoon_Eyes.ico'
```

**Why:** When the app is packaged, PyInstaller extracts resources to a temporary directory (`sys._MEIPASS`). Without this change, the app cannot find the Databases, Resources, and Help folders.

### Step 2: Fix Database Path Handling

**File: `database_handler.py`**

In the `process_file_from_folder()` method, change the path handling to:

1. Keep absolute paths for file operations
2. Extract relative paths for structure parsing
3. Adjust path split lengths (from 3/4 to 2/3)

```python
cleaned_file_path: list = []

for file_path in file_path_list:
    # Keep the full absolute path for file operations
    cleaned_file_path.append(file_path)

# First gather all the file list and split them based in the nesting inside the folders
simple_nest_path: list[tuple] = []
double_nest_path: list[tuple] = []
for database_file_path in cleaned_file_path:
    # Extract relative path from Databases/ onwards for structure parsing
    if '/Databases/' in database_file_path:
        relative_path = database_file_path.split('/Databases/')[1]
    else:
        relative_path = database_file_path
    
    split_file_path = relative_path.split('/')
    get_parent_name: str = ''
    get_child_name: str = ''

    # if length_this_path equal to 2 == Simple Nesting ; if length_this_path equal to 3 == Double Nesting
    length_this_path = len(split_file_path)
    if length_this_path == 2:
        get_parent_name = split_file_path[1].replace('.csv', '')
        this_path_data_simple = get_parent_name, database_file_path
        simple_nest_path.append(this_path_data_simple)

    elif length_this_path == 3: # This are Characters and CutScenes Databases
        get_parent_name = split_file_path[1]
        get_child_name = split_file_path[2].replace('.csv', '').replace('_', ' ')
        this_path_data_double = get_parent_name, get_child_name, database_file_path
        double_nest_path.append(this_path_data_double)
```

**Why:** PyInstaller packages data files with absolute paths. The database handler needs to work with these absolute paths while maintaining the relative structure for internal logic.

### Step 3: Build the macOS App Bundle

Run PyInstaller with the following command:

```bash
cd /Users/thomasvang/Desktop/TLoD-Assets-Manager-MacOS

pyinstaller --windowed --onedir --name "TLoD-Assets-Manager" \
  --add-data "Databases:Databases" \
  --add-data "Help:Help" \
  --add-data "Resources:Resources" \
  --noconfirm \
  main_gui.py
```

**Parameters explained:**
- `--windowed` - Creates a GUI application (no console window)
- `--onedir` - Bundles everything in one directory (more reliable than `--onefile`)
- `--name "TLoD-Assets-Manager"` - Sets the executable name
- `--add-data "source:destination"` - Includes data files/folders in the bundle
- `--noconfirm` - Skips confirmation prompts
- `main_gui.py` - Entry point script

**What this creates:**
- `build/` - Temporary build files (can be deleted)
- `dist/TLoD-Assets-Manager.app` - The final macOS application bundle
- `TLoD-Assets-Manager.spec` - PyInstaller configuration file (keep for future rebuilds)

### Step 4: Copy App to Main Directory

**Important:** Use `ditto` to copy the app bundle, NOT `cp -r`. The `cp` command breaks the macOS bundle structure.

```bash
ditto dist/TLoD-Assets-Manager.app TLoD-Assets-Manager.app
```

**Why:** macOS app bundles are special directory structures with internal symlinks and resource forks. `ditto` is the proper macOS tool for preserving bundle integrity. Using `cp -r` causes segmentation faults when launching.

### Step 5: Test the App

```bash
# Test from command line
./TLoD-Assets-Manager.app/Contents/MacOS/TLoD-Assets-Manager

# Or open normally
open TLoD-Assets-Manager.app
```

## File Structure

After building, your directory structure should look like:

```
TLoD-Assets-Manager-MacOS/
├── build/                              # (generated, can delete after build)
├── dist/
│   ├── TLoD-Assets-Manager/           # Executable and dependencies
│   └── TLoD-Assets-Manager.app/       # Main app bundle
├── TLoD-Assets-Manager.app            # Copy for distribution
├── TLoD-Assets-Manager.spec           # PyInstaller config
├── Databases/                          # Source data
├── Resources/                          # Source resources
├── Help/                               # Help files
├── main_gui.py                         # Entry point
├── database_handler.py                 # Database handling
└── ... (other source files)
```

## Bundled Dependencies

The build automatically includes all these packages:
- PyQt6
- numpy
- scipy
- Pillow
- pygltflib

Plus all custom modules:
- file_handlers/
- deff_handlers/
- gltf_handlers/
- texture_handlers/

## Cleanup

After a successful build, you can clean up build artifacts:

```bash
rm -rf build/
rm -rf dist/TLoD-Assets-Manager/  # Keep dist/TLoD-Assets-Manager.app
```

## Distribution

The final executable for distribution is:
```
TLoD-Assets-Manager.app
```

Users can:
1. Copy it to their Applications folder
2. Double-click to run (no Python installation needed)
3. Move it anywhere on their Mac - it's completely portable

## Troubleshooting

### App crashes immediately
- Check that `main_gui.py` has the PyInstaller path detection code
- Check that `database_handler.py` uses absolute paths correctly
- Run from terminal to see error messages: `./TLoD-Assets-Manager.app/Contents/MacOS/TLoD-Assets-Manager 2>&1`

### "Databases not found" error
- Ensure `database_handler.py` is using absolute paths
- Verify the `--add-data` flags include all required folders
- Check that paths are extracted correctly: `relative_path = database_file_path.split('/Databases/')[1]`

### Segmentation fault on launch
- Do NOT use `cp -r` to copy the app bundle - use `ditto` instead
- Verify the icon file (if using one) is valid and not oversized
- Remove the `--icon` parameter if experiencing crashes with custom icons

### App runs from dist/ but not from main directory
- Use `ditto` to copy, not `cp -r`
- Check file permissions: `chmod -R +rx TLoD-Assets-Manager.app`

## Quick Build Script

For future builds, save this as `build.sh`:

```bash
#!/bin/bash
cd /Users/thomasvang/Desktop/TLoD-Assets-Manager-MacOS

# Clean old builds
rm -rf build dist TLoD-Assets-Manager.app

# Build new app
pyinstaller --windowed --onedir --name "TLoD-Assets-Manager" \
  --add-data "Databases:Databases" \
  --add-data "Help:Help" \
  --add-data "Resources:Resources" \
  --noconfirm \
  main_gui.py

# Copy to main directory
ditto dist/TLoD-Assets-Manager.app TLoD-Assets-Manager.app

# Test
echo "Build complete! Testing..."
./TLoD-Assets-Manager.app/Contents/MacOS/TLoD-Assets-Manager 2>&1 | head -5

echo "Success! App ready at: TLoD-Assets-Manager.app"
```

Make it executable:
```bash
chmod +x build.sh
```

Then build any time with:
```bash
./build.sh
```

## Notes

- **PyInstaller version used:** 6.17.0
- **Python version:** 3.11.14
- **Platform:** macOS (arm64 - Apple Silicon)
- **Last updated:** December 5, 2025
