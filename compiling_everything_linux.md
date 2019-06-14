# Compiling Teeworlds on Linux

**IMPORTANT NOTE:** SDL and Freetype libs are not shipped with Teeworlds 0.7.x. You must download them separately.

**Q: What is bam?**

Bam is the [build system made by matricks](http://matricks.github.io/bam/) used in Teeworlds.

#### Setup
1. Use your package manager (apt-get, emerge or whatever is used on your distribution) to install the following (you will need the header files):
    - gcc
    - g++
    - python
    - alsa (asound)
    - gl
    - glu
    - x11
    - libsdl2
    - freetype
2. Download and unzip [Teeworlds source](https://github.com/teeworlds/teeworlds/releases) or [Teeworlds latest source](https://github.com/teeworlds/teeworlds/archive/master.zip)
3. Download and unzip [bam](https://github.com/matricks/bam/archive/v0.5.1.tar.gz) to `teeworlds-version/bam`
4. Compiling bam  
    - `$ cd bam`
    - `$ ./make_unix.sh`
    - `$ cd ..`


#### Compiling
1. `cd teeworlds-version`
    - Changes to the teeworlds source directory
2. `./bam/bam config`
    - Runs bam configuration
3. `./bam/bam conf=release`
    - Compiles teeworlds (Client and Server)
    - `conf=debug` will build the debug version
    - Available targets for release and debug:
        - `game`(default)
        - `server`
        - `client`
        - `content`
        - `masterserver`
        - `tools`
    - To build the tools and master server in release mode use the following arguments:
        - `conf=release tools masterserver`
    - Flag `-f` will force a recompile
    - You may specify the architecture using `arch`, e.g. `arch=x86` or `arch=x86_64`.
4. The compiled game is located at `teeworlds-version/build/<arch>`


# For Teeworlds v0.6.x and earlier

1. `cd teeworlds-version`
    - Changes to the teeworlds source directory
2. `./bam/bam release`
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

**Note:** If you are using bam 0.2.0 (needed for Teeworlds 0.5.2 and earlier) the bam binary will not be in the bam directory, but in bam/src. You will need to change the paths accordingly to that or copy/move the bam executable to the bam directory.
