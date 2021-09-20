# Compiling Teeworlds on Windows

**Q: What is bam?**

Bam is the [build system made by matricks](http://matricks.github.io/bam/) used in Teeworlds.

## Setup (Using Microsoft Tools)

1. Download and install [Visual Studio 2017 Community](https://visualstudio.microsoft.com/de/downloads/).
2. Download and unzip [Teeworlds source](https://github.com/teeworlds/teeworlds/releases) or [Teeworlds latest source](https://github.com/teeworlds/teeworlds/archive/master.zip)
3. Download and install [Python 3.x](https://www.python.org/download/)
4. Download and unzip [bam](https://github.com/teeworlds/bam/archive/master.zip) to `teeworlds-version\bam`
    - Run `make_win64_msvc.bat` (or `make_win32_msvc.bat` for x86) to compile bam
    - **Note:** Bam does not recognise Visual Studio 2017. As a workaround, to compile bam, run the aforementioned batch script from the `x64 Native Tools Command Prompt` (or `x86 Native Tools Command Prompt` for x86)

## Compiling Teeworlds v0.7.x

1. Run the `x64 Native Tools Command Prompt` (or `x86 Native Tools Command Prompt` for x86) from the start menu.
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
5. The compiled game is located at `teeworlds-version\build\x86_64\` (or `teeworlds-version\build\x86\` for x86)

## Compiling Teeworlds v0.6.x and earlier

1. Run the `x64 Native Tools Command Prompt` (or `x86 Native Tools Command Prompt` for x86) from the start menu.
2. `cd teeworlds-version`
    - Changes to the teeworlds source directory
3. `.\bam\bam release`
    - Compiles teeworlds (Client and Server)
    - Available targets for release and debug are:
        - `release` (for all in release mode)
        - `debug` (for all in debug mode)
        - `server_release`
        - `server_debug`
        - `client_release`
        - `client_debug`
4. The compiled game is located in `teeworlds-version`

**Note:** Teeworlds 0.5.2 and earlier requires Python 2.x to compile. Python 3.x will not work. Python 3.x support is introduced with Teeworlds 0.6.0.

**Note:** Teeworlds 0.5.2 and earlier requires bam 0.2.0. The bam binary will not be in the bam directory, but in `bam\src`. You will need to change the paths accordingly to that or copy/move the bam executable to the bam directory.
