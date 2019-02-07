# Compiling Teeworlds on Windows

**IMPORTANT NOTE:** SDL and Freetype libs are not shipped with Teeworlds 0.7.x. You must download them separately and place them in the other\ folder.

**Q: What is bam?**

Bam is the [build system made by matricks](http://matricks.github.io/bam/) used in Teeworlds.

### Setup (Using Microsoft Tools)
1. Download and install [Visual Studio 2017 Community](https://visualstudio.microsoft.com/de/downloads/).


## Windows x64 
#### Setup
1. Download and unzip [Teeworlds source](https://github.com/teeworlds/teeworlds/releases) or [Teeworlds latest source](https://github.com/teeworlds/teeworlds/archive/master.zip)
2. Download and install [Python 3.x](https://www.python.org/download/)
3. Download and unzip [bam](https://github.com/matricks/bam/archive/v0.5.1.zip) to `teeworlds-version\bam`
    - Run `make_win64_msvc.bat` to compile bam
    - **Note:** Bam does not recognise Visual Studio 2017. As a workaround, to compile bam, copy `line 45 to end` from `make_win64_msvc.bat` and paste it in the `x64 Native Tools Command Prompt`

#### Compiling
1. Run the `x64 Native Tools Command Prompt` (64Bit) from the start menu.
2. `cd teeworlds-version`
    - Changes to the teeworlds source directory
3. `.\bam\bam config`
    - Runs bam configuration
4. `.\bam\bam conf=release`
    - Compiles teeworlds (Client and Server)
    - `conf=debug` will build the debug version instead
    - You can also provide a target:
        - `game`(default)
        - `server`
        - `client`
        - `content`
        - `masterserver`
        - `tools`
    - For example, to build the tools and master server in release mode use the following arguments:
        - `.\bam\bam conf=release tools masterserver`
    - Flag `-f` will force a recompile
5. The compiled game is located at `teeworlds-version\build\x86_64\`


## Windows x86 
#### Setup
1. Download and unzip [Teeworlds source](https://github.com/teeworlds/teeworlds/releases) or [Teeworlds latest source](https://github.com/teeworlds/teeworlds/archive/master.zip)
2. Download and install [Python 3.x](https://www.python.org/download/)
3. Download and unzip [bam](https://github.com/matricks/bam/archive/v0.5.1.zip) to `teeworlds-version\bam`
    - Run `make_win32_msvc.bat` to compile bam
    - **Note:** Bam does not recognise Visual Studio 2017. As a workaround, to compile bam, copy `line 45 to end` from `make_win32_msvc.bat` and paste it in the `x86 Native Tools Command Prompt`


#### Compiling
1. Run the `x86 Native Tools Command Prompt` (32Bit) from the start menu.
2. `cd teeworlds-version`
    - Changes to the teeworlds source directory
3. `.\bam\bam config`
    - Runs bam configuration
4. `.\bam\bam conf=release`
    - Compiles teeworlds (Client and Server)
    - `conf=debug` will build the debug version instead
    - You can also provide a target:
        - `game`(default)
        - `server`
        - `client`
        - `content`
        - `masterserver`
        - `tools`
    - For example, to build the tools and master server in release mode use the following arguments:
        - `.\bam\bam conf=release tools masterserver`
    - Flag `-f` will force a recompile
5. The compiled game is located at `teeworlds-version\build\x86\`

    
# For Teeworlds v0.6.x and earlier

1. `cd teeworlds-version`
    - Changes to the teeworlds source directory
2. `.\bam\bam release`
    - Compiles teeworlds (Client and Server)
    - Available targets for release and debug:
        - `release` (for all in release mode)
        - `debug` (for all in debug mode)
        - `server_release`
        - `server_debug`
        - `client_release`
        - `client_debug`
3. The compiled game is located in `teeworlds-version`

**Note:** Teeworlds 0.5.2 and earlier requires python 2.x to compile. Python 3.x will not work. Python 3.x support is introduced with Teeworlds 0.6.0.

**Note:** Teeworlds 0.5.2 and earlier requires bam 0.2.0. The bam binary will not be in the bam directory, but in `bam\src`. You will need to change the paths accordingly to that or copy/move the bam executable to the bam directory.
