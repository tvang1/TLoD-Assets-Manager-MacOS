## TLoD Tool for manage game Assets (Textures, Models, Animations).
Version: **BETA 0.2**

**MAC OS Fork**
Yeah you read well!... right now TheRamenRider it's doing a very good job forking and adapting TLoD Assets Converter code for MacOS and their Users!.
Since I do not have a proper hardware to test it, was impossible to me making something at least 'good'.
[https://github.com/tvang1/TLoD-Assets-Manager-MacOS]
You can check it in there!

**Instructions for MacOS users by TheRamenRider/tvang1**

I'm assuming one can download this repo and can extract the contents in an organized place.
Or hopefully, one knows how to clone from a repo.
If you have trouble doing that, please look at [ https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository ]

So we have some requirements. TLoD Assets Converter relies on Python and some dependecies.
Python can be installed a couple of ways on MacOS.
1) Python's main page [ https://www.python.org/downloads/ ]
2) 'Brew' [ https://brew.sh ]

I personally use 'brew' as it's similar to Linux distro packages.

Once you get Python installed. You'll have to use MacOS terminal and navigate to the TLoD Assets Converter folder.

> cd [ path to folder ]

As far as running the program and getting dependecies, you're in luck!
Just run the command in terminal (assuming you're in the TLoD Assets Converter folder):

> bash Start-TLoD.sh

This sets up a python virtual environment for TLoD Assets Converter and installs the dependecies. Once that's done, you can continue to run Start-TLoD.sh or main_gui.py to use TLoD Assets Converter. As long as the .venv is present, you'll be able to run the tool.

---

## About the tool:

Surely you are familiar to TLoD TMD Converter (tool for converting Models from TLoD) and TLoD Texture Converter (tool for converting Textures), now i merged the best of the two worlds in a single tool. TLoD Assets Manager. 

A tool designed to efficiently work with TLoD Models, Textures and in a future Sounds/Audio files.

At this very moment BETA Version 0.2, the idea about this tool is not only converting models/animations/textures, but also in a future help to modding community to easily grouping and sorting their installed Visual and Audio mods!. For BETA 0.5 (yeah I re-formulate this, sorry but I was very positive in reaching this goal way before), Preview of Models/Animations and Textures in real time.

Since this tool relies heavily in [Severed Chains](https://github.com/Legend-of-Dragoon-Modding/Severed-Chains), strongly recommend install it and run it (at least once) to get files properly deployed.

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

As GUI TLoD Assets Converter uses PyQt6 a nice way to work on modern GUIs and hopefully get this tool working multiplatform without loosing my mind:

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

First start the tool will ask where it's located the `files` folder of Severed Chains, in here is where the TLoD Assets are deployed after Severed Chains first startup.

Later will ask a folder to deploy the converted files.

In the `CONFIG` Button you can change some options related to Window size and folders setup (if you want to change the deploy folder or the Severed Chains folder).

#### How to use it

In the main window will find several buttons to do specific tasks.
- Convert Battle Models. Pretty self-explanatory.
- Convert SubMap Models. Convert models used in the Pre-rendered Backgrounds, not only the characters also the 3D and Textures from the Pre-rendered Background.
- Convert WorldMap Models. Convert models used while world navigation. 
- Textures Only. In here you'll find the Textures which are not attached to a model, for example the game GUI, some text, fonts, etc.
- Future Options: DEFF Conversion (convert Special Visual effects used during Magic casts, Dragoon attacks/magics, some other stuff), Sound Conversion, Mod Manager.
