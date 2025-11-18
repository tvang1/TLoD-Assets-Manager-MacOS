# TLoD Assets Manager MacOS/Linux Version
TLoD Tool for manage game Assets (Textures, Models, Animations).
Version: **BETA 0.2**

*Changelog from TheRamenRider*
11-18-2025

There are some bash scripts for convienience.

namefix.sh and installDepend.sh

namefix.sh is just for convienience to fix text for the versioning.

installDepend.sh is a usefull script to install dependencies for Python for TLod Assets Manager. If one pulls from my fork, please alter the script to include your version of Python and adjust your env accordingly.

*Changelog from TheRamenRider*
10-18-2025

These are changes made from the TLoD Assets Manager Beta 0.2 to fit the MacOS/Linux Environment. 

1) Fixed notable f-strings mismatches. It's a logical issue mostly pertaining to nested f-strings. This was more notable for config_handlers.py and folder_handler.py

--- From ---
firstrun_flag = f'FIRST_RUN = {configuration_dict.get(f'First_Run')}\n'
res_x = f'DEFAULT_RES_X = {configuration_dict.get(f'SizeX')}\n'
res_y = f'DEFAULT_RES_Y = {configuration_dict.get(f'SizeY')}\n'
sc_folder = f'SC_FOLDER = {configuration_dict.get(f'SC_Folder')}\n'
deploy_folder = f'DEPLOY_FOLDER = {configuration_dict.get(f'Deploy_Folder')}'

--- To --
firstrun_flag = f"FIRST_RUN = {configuration_dict.get(f'First_Run')}\n"
res_x = f"DEFAULT_RES_X = {configuration_dict.get(f'SizeX')}\n"
res_y = f"DEFAULT_RES_Y = {configuration_dict.get(f'SizeY')}\n"
sc_folder = f"SC_FOLDER = {configuration_dict.get(f'SC_Folder')}\n"
deploy_folder = f"DEPLOY_FOLDER = {configuration_dict.get(f'Deploy_Folder')}"

There are plans to fix this into literal strings. For now, this should help.

2) Fixed file pathing for MacOS/Linux. MacOS/Linux utilizes ‘/‘ instead of ‘\’. Most of the .py escaped and utlized '\\'. I replaced the '\\' with '/' throughout .py files.

--- From ---
absolute_path_config = f'{absolute_path_current}\\Resources\\Manager.config'
absolute_path_databases = f'{absolute_path_current}\\Databases'
background_image = f'{absolute_path_current}\\Resources\\main.png'.replace('\\', '/')
icon_app = f'{absolute_path_current}\\Resources\\Dragoon_Eyes.ico'

--- To ---
absolute_path_config = f'{absolute_path_current}/Resources/Manager.config'
absolute_path_databases = f'{absolute_path_current}/Databases'
background_image = f'{absolute_path_current}/Resources/main.png'.replace('/', '/')
icon_app = f'{absolute_path_current}/Resources/Dragoon_Eyes.ico'


3) Ran into a bug and logical issues with submap texture exporting. When using submap converstions, the textures seemed to not want to be exported. DooMMetal identified the bug. Values in submap_conversion_window.py needed to be set to True. Such as { self.texture_convert = True } and { self.check_texture.setChecked(True) }

I'd like to thank DooMMEtal and Monoxide for assisting with this version.


-----
*About the tool:*

Surely you are familiar to TLoD TMD Converter (tool for converting Models from TLoD) and TLoD Texture Converter (tool for converting Textures), now i merged the best of the two worlds in a single tool. TLoD Assets Manager. 

A tool designed to efficiently work with TLoD Models, Textures and in a future Sounds/Audio files.

At this very moment BETA Version 0.1, the idea about this tool is not only converting models/animations/textures, but also in a future help to modding community to easily grouping and sorting their installed Visual and Audio mods!. For BETA 0.2, Preview of Models/Animations and Textures in real time.

Since this tool realies heavily in [Severed Chains](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains), i strongly recommend install it and run it (at least once) to get files properly deployed.

Also this tool came with a lot of news!.
- Changed support for 3D converted files into glTF 2.0, file format. Since Blender 4.0+ it's moving Collada DAE Files support into Legacy. This change also help us to store easily in the same file all the Animations from a converted model.
- Navigation for Conversion now it's more easy.
- Advanced features, deprecated, since Severed Chains convert almost all files into their "PSX Standard Version" file format.

Updates to be pull:
- Model/Animation and Texture Previewing.
- DEFF Converter.
- Sound/Music Converter.
- Visual/Sound Mods Managment.

---

## Severed Chains

You can check Severed Chains and it's Development in here:

Link: [Severed Chains](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains)

Some parts of my code uses a "translated" version of Severed Chains code, Java -> Python.

This project made by: Monoxide.
Maintaned: Severed Chains Dev Team. (Lead Monoxide).
License: GPL Affero.

## PyQt6

As GUI i use PyQt6 a nice way to work on modern GUIs and hopefully get this tool working multiplatform without loosing my mind:

Link: [PyQt6](https://pypi.org/project/PyQt6/)

Project by: Riverbank Computing Limited.

Maintaned by: Phil Thimpson.

License: GPL v3.

### Other code snippets / Thanks

Monoxide, thanks a lot for making Severed Chains, also to helping me out understanding the Animations file formats and other stuff around the code.

TheFlyingZamboni, thanks a lot mate for giving the Texture code snippets and also for helping me understand how it works!.

StackOverflow Community in general. Since i look some solutions for stuff that i need to do in this code.

All rights reserved to their respective owners, you can check in the code the refereces for them!.

---

#### How to Install

If you are familiar with Python, you can pull the code and executing `main_gui.py`.

If you want to use a direct "compiled-Windows-EXE-version", download the lastest from here:
[Latest Build](https://github.com/Legend-of-Dragoon-Modding/TLoD-Assets-Manager/releases).

#### Setup

First start the tool will ask where it's located the `files` folder of Severed Chains, in here is where the TLoD Assets are deployed after Severed Chains first startup.

Later will ask a folder to deploy the converted files.

In the `CONFIG` Button you can change some options related to Window size and folders setup (if you want to change the deploy folder or the Severed Chains folder).

#### How to use it

In the main window will find several buttons to do specific tasks.
- Convert Battle Models. Pretty self-explanatory.
- Convert SubMap Models. Convert models used in the Pre-rendered Backgrounds, not only the characters but the 3D and Textures from the Pre-rendered Background.
- Convert WorldMap Models. Convert models used while world navigation. 
- Textures Only. In here you'll find the Textures which have no model related to it, for example the game GUI, some text, fonts, etc.
- Future Options: DEFF Conversion (convert Special Visual effects used during Magic casts, Dragoon attacks/magics, some other stuff), Sound Conversion, Mod Manager.