# OpenDSS for Linux

OpenDSS is an electric power Distribution System Simulator (DSS) for supporting distributed resource integration and grid modernisation efforts.

As explained in the background section, the original OpenDSS package ships with a Dynamic Linked Library (DLL) that allowing the user to interface with the solver via COM Server. However, this was limited to Windows.

This repository provides a procedure to acquire and compile a Linux (here Ubuntu 16.04) compatible shared object library, which is used in a sample `PyDSS` module.

## TODO

- [x] Compile on *Ubuntu Linux* for *Ubuntu Linux*
- [x] Compiled library works on *Ubuntu Linux*
- [x] Compile on *Raspberry Pi* for *Raspberry Pi*
- [ ] Compiled library works on *Raspberry Pi*
- [ ] Cross-compile on *Ubuntu Linux* for *Raspberry Pi*
- [ ] Compiled library works on *Raspberry Pi*

## Usage on Ubuntu Linux - *simplest*

### Setup

Run the following or follow the steps below manually:

```
make setup_Ubuntu
```

<hr>

Start by installing all prerequisites, including the standard compiler and lazarus (with Free Pascal). Also two additional symbolic links need to be added for the compilation to function correctly.

```
sudo apt update
sudo apt upgrade
sudo apt install build-essential lazarus subversion
sudo ln -sfv /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /usr/lib/x86_64-linux-gnu/libstdc++.so
sudo ln -sfv /lib/x86_64-linux-gnu/libgcc_s.so.1 /lib/x86_64-linux-gnu/libgcc_s.so
```

### Compile

Fully compile the library using:

```
make
```

This will save the final `libopendssdirect.so` in the `lib` directory, and a full copy of the OpenDSS source is stored in `electricdss`. If you want the OpenDSS source saved somewhere else, you can build like so:

```
make OPENDSS_DIR=some_other_dir
```

Also, making the project will download and compile a standalone KLUSolve, to assure it is compiled for the correct CPU architecture.

## Usage on Raspberry Pi

### Setup

Run the following or follow the steps below manually:

```
make setup_RPi
```

<hr>

Start by installing all prerequisites, including the RPi compilers, and add two symbolic links needed for the compilation to function correctly.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential subversion
sudo ln -sfv /usr/lib/arm-linux-gnueabihf/libstdc++.so.6 /usr/lib/arm-linux-gnueabihf/libstdc++.so
sudo ln -sfv /lib/arm-linux-gnueabihf/libgcc_s.so.1 /lib/arm-linux-gnueabihf/libgcc_s.so
```

Install `fpc` (version 3.0.0) on Raspberry:

```
wget ftp://ftp.hu.freepascal.org/pub/fpc/dist/3.0.0/arm-linux/fpc-3.0.0.arm-linux-raspberry1wq.tar
tar -xvf fpc-3.0.0.arm-linux-raspberry1wq.tar
cd fpc-3.0.0.arm-linux
sudo ./install.sh
cd ..
```

Make sure you install it into `/usr` **not** `/usr/local`.

### Compiling

Next build `libopendssdirect.so` for ARM:

```
make arm
```

This compiler also downloads and compile KLUSolve since it is not provided for ARM.

### BUG

I currently get a Stack-Overflow error when importing the `libopendssdirect.so` using `ctypes` in Python (2/3).

Reasons may be:

- [x] Try different `fpc` compiler (v 3.0.0 instead of v 3.0.2)
- [ ] Try different `gcc` compiler (v 5.* instead of 4.5)

## Cross-Compile on Ubuntu Linux for Raspberry Pi

***THIS STAGE IS STILL INCOMPLETE***

### Setup

First install the correct cross-compiler:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential subversion
```

Acquire `fpc` (version 3.0.2):

```
wget https://sourceforge.net/projects/freepascal/files/Linux/3.0.2/fpc-3.0.2.x86_64-linux.tar
```