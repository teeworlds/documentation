# Compiling Teeworlds

**IMPORTANT NOTE:** Teeworlds 0.5.2 and earlier requires python 2.x to compile. Python 3.x will not work. Python 3.x support is introduced with Teeworlds 0.6.0.

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

### Windows

##### Setup

1. Download and install Visual C/C++ Express (http://www.microsoft.com/express/download/default.aspx) 
2. Download and install Python (https://www.python.org/download/). (for Teeworlds 0.5.2 and earlier the 2.x version, not 3.x)
3. Download and unzip bam (0.2.0 for Teeworlds 0.5.2 and earlier, 0.4.0 for Teeworlds 0.6.0 and later) 
4. Download and unzip teeworlds (https://www.teeworlds.com/?page=downloads) 

##### Compiling bam

Run in cmd (start>run>cmd):

```
cd bam
make_win32_msvc.bat
cd ..
```

##### Compiling teeworlds

Run in cmd (start->run->cmd):

```
%comspec% /k ""C:\Program Files\Microsoft Visual Studio 9.0\VC\vcvarsall.bat"" x86

cd teeworlds-version-src 

..\bam\bam
```

This will build the client and server.

Bam parameters are described in a later section.

### Linux / Mac

#### Setup

##### On Linux

Use your package manager (apt-get, emerge or whatever is used on your distribution) to install the following (you will need the header files):

- python
- alsa (asound)
- gl
- glu
- x11
- libsdl
- freetype

(python is the only one which is required to build server)

##### On Mac OS X

Install the XCode tools from apple. Download libsdl from the http://libsdl.org and put SDL.framework in /Library/Frameworks

#### Getting the source

Run the following commands to download and unzip bam and teeworlds:
**Replace VERSION in teeworlds-VERSION-src.zip with the version you want (probably the latest, 0.6.0)**

Using `wget`:

```
$ wget -qO- http://github.com/downloads/matricks/bam/bam-0.4.0.tar.bz2 | tar xj
$ wget -qO- https://downloads.teeworlds.com/files/teeworlds-VERSION-src.zip | tar xj
```

Alternatively, using `fetch`:

```
$ fetch http://github.com/downloads/matricks/bam/bam-0.4.0.zip
$ unzip bam.zip
$ rm bam.zip
$ fetch https://downloads.teeworlds.com/files/teeworlds-VERSION-src.zip
$ unzip teeworlds-VERSION-src.zip
$ rm teeworlds-VERSION-src.zip
```

##### Compiling bam
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

### Bam parameters

By default, Teeworlds compiles in debug mode. To compile in release mode, add `conf=release` to the bam arguments. E.g.:

`$ ../bam/bam conf=release`

By default, Teeworlds compiles the `game` target, i.e. the client and server. Available targets are:
- game (client and server)
- client
- server
- tools
- masterserver

E.g. to build the tools and master server in release mode use following arguments:

`$ ../bam/bam conf=release tools masterserver`
