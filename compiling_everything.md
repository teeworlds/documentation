# Compiling Teeworlds

****IMPORTANT NOTE:** SDL and Freetype libs are not shipped with Teeworlds 0.7.x. You must download them separately and placed them in the other/ folder.

**Also:** Teeworlds 0.5.2 and earlier requires python 2.x to compile. Python 3.x will not work. Python 3.x support is introduced with Teeworlds 0.6.0.

**Also:** If you are using bam 0.2.0 (needed for Teeworlds 0.5.2 and earlier) the bam binary will not be in the bam directory, but in bam/src. You will need to change the paths accordingly to that or copy/move the bam executable to the bam directory.

### FAQ

**Q: How do I get rid of these errors?**

```
undefined reference to `__stack_chk_guard'
```

Remove `-fstack-protector -fstack-protector-all` from bam.lua (in 0.5.2 and earlier default.bam) in Teeworlds root directory and then run

```
../bam/bam -c all
```

**Q: What is BAM?**

Bam is the [build system made by matricks](http://matricks.github.io/bam/) used in Teeworlds.


# Windows

1. Download and unzip bam
    - [v0.2.0](http://github.com/downloads/matricks/bam/bam-0.2.0.zip) for Teeworlds 0.5.2 and earlier
    - [v0.4.0](http://github.com/downloads/matricks/bam/bam-0.4.0.zip) for Teeworlds 0.6.x
    - [v0.5.0](https://github.com/matricks/bam/archive/v0.5.0.zip) for Teeworlds 0.7.0 and later
2. Download and install [Python](https://www.python.org/download/) (for Teeworlds 0.5.2 and earlier the 2.x version, not 3.x).
4. Download and unzip [Teeworlds](https://www.teeworlds.com/?page=downloads).

### Setup (Using GNU Tools)

1. Download and install [MinGW](http://sourceforge.net/projects/mingw/files/latest/download?source=files). Select 'mingw32-gcc-g++' package inside MinGW installer.
2. Download and install [ZLib](http://gnuwin32.sourceforge.net/downlinks/zlib.php).

#### Compiling BAM

1. Update 'PATH' windows environment variable including MinGW and zlib bin folders.
    - Run in cmd (start>run>cmd):

    ```
    setx PATH "%PATH%;C:\MinGW\bin;C:\Program Files (x86)\GnuWin32\bin;"
    ```
2. Launch `make_win32_mingw.bat` script to compile bam.
    - Run in cmd (start>run>cmd):

    ```
    cd <folder_where_unzipped_bam_package>
    make_win32_mingw.bat
    ```

#### Compiling Teeworlds

Run in cmd (start->run->cmd):

```
cd teeworlds-version-src
..\bam\bam
```

This will build the client and server.

Bam parameters are described in a later section.

### Setup (Using Microsoft Tools)

1. Download and install [Visual C/C++ Express](https://www.visualstudio.com/post-download-vs/?sku=xdesk&clcid=0x409&telem=ga).

#### Compiling bam

1. Launch `make_win32_msvc.bat` script to compile bam.
    - Run in cmd (start>run>cmd):
    ```
    cd <folder_where_unzipped_bam_package>
    make_win32_msvc.bat
    ```

#### Compiling Teeworlds

Run the `x86 Native Tools Command Prompt` (32Bit) or the `x64 Native Tools Command Prompt` (64Bit) from the start menu.

Or

Run in cmd (start->run->cmd):

```
%comspec% /k ""C:\Program Files\Microsoft Visual Studio 14.0\VC\vcvarsall.bat"" x86

cd teeworlds-version-src
..\bam\bam
```

For 64-bit, use `amd64` instead:

```
%comspec% /k ""C:\Program Files\Microsoft Visual Studio 14.0\VC\vcvarsall.bat"" amd64
```

This will build the client and server. 

Bam parameters are described in a later section.


# Linux / Mac

## Setup

#### On Linux

Use your package manager (apt-get, emerge or whatever is used on your distribution) to install the following (you will need the header files):

- python
- alsa (asound)
- gl
- glu
- x11
- libsdl
- freetype

(python is the only one which is required to build server)

#### On Mac OS X

Install the XCode tools from apple. Download libsdl from the http://libsdl.org and put SDL.framework in /Library/Frameworks

#### Getting the source

Run the following commands to download and unzip bam and teeworlds:
**Replace VERSION in teeworlds-VERSION-src.zip with the version you want (probably the latest, 0.7.0)**

Using `wget`:

```
$ wget -qO- https://github.com/matricks/bam/archive/v0.5.0.tar.gz | tar xj
$ wget -qO- https://downloads.teeworlds.com/teeworlds/teeworlds-VERSION-src.zip | tar xj
```

Alternatively, using `fetch`:

```
$ fetch https://github.com/matricks/bam/archive/v0.5.0.tar.gz
$ unzip bam.zip
$ rm bam.zip
$ fetch https://downloads.teeworlds.com/teeworlds/teeworlds-VERSION-src.zip
$ unzip teeworlds-VERSION-src.zip
$ rm teeworlds-VERSION-src.zip
```

#### Compiling bam

```
$ cd bam
$ ./make_unix.sh
$ cd ..
```

#### Compiling teeworlds

This will build the client and server.

```
$ cd teeworlds-VERSION-src
$ ../bam/bam
```

For 0.7.0 and later, you will find the binaries in the `build` folder.

# Bam parameters

For more advanced options check the [bam documentation](http://matricks.github.io/bam/bam.html#5).



#### For Teeworlds v0.7.0 and later

By default, Teeworlds compiles in debug mode. To compile in release mode, add `conf=release` to the bam arguments. E.g.:

`$ ../bam/bam conf=release`

By default, Teeworlds compiles the `game` target, i.e. the client and server. Available targets are:

+ game (client and server)
+ client
+ server
+ tools
+ masterserver

E.g. to build the tools and master server in release mode use the following arguments:

`$ ../bam/bam conf=release tools masterserver`


You may specify the architecture using `arch`, e.g. `arch=X86` or `arch=x64`.

#### For Teeworlds v0.6.x and earlier

Available targets are:

+ release (for all in release mode)
+ debug (for all in debug mode)
+ server_release
+ server_debug
+ client_release
+ client_debug

E.g. to build server debug use the following arguments:

`$ ../bam/bam server_debug`
