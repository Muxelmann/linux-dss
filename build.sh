#!/bin/bash

# Update and install prerequisites
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential lazarus subversion

# Make necessary symlinks for compilation
sudo ln -sv /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /usr/lib/x86_64-linux-gnu/libstdc++.so
sudo ln -sv /lib/x86_64-linux-gnu/libgcc_s.so.1 /lib/x86_64-linux-gnu/libgcc_s.so

OPENDSS_DIR="electricdss" # FIXME: Change this to where you want OpenDSS downloaded
OPENDSS_DIR=`realpath ${OPENDSS_DIR}`

# Acquire OpenDSS repo
mkdir ${OPENDSS_DIR}
cd ${OPENDSS_DIR}
svn checkout https://svn.code.sf.net/p/electricdss/code/trunk .

# Compile...
/usr/bin/fpc \
-Px86_64 -MDelphi -Scghi -Cg -Ct -O2  -k-lc -k-lm -k-lgcc_s -k-lstdc++ -l -vewnhibq \
-Fi${OPENDSS_DIR}/Source/LazDSS/Forms \
-Fi${OPENDSS_DIR}/Source/LazDSS/Shared \
-Fi${OPENDSS_DIR}/Source/LazDSS/Common \
-Fi${OPENDSS_DIR}/Source/LazDSS/PDElements \
-Fi${OPENDSS_DIR}/Source/LazDSS/Controls \
-Fi${OPENDSS_DIR}/Source/LazDSS/General \
-Fi${OPENDSS_DIR}/Source/LazDSS/Plot \
-Fi${OPENDSS_DIR}/Source/LazDSS/Meters \
-Fi${OPENDSS_DIR}/Source/LazDSS/PCElements \
-Fi${OPENDSS_DIR}/Source/LazDSS/Executive \
-Fi${OPENDSS_DIR}/Source/LazDSS/Parser \
-Fi${OPENDSS_DIR}/Source/LazDSS/units/x86_64-linux \
-Fl${OPENDSS_DIR}/Source/LazDSS/lib \
-Fu${OPENDSS_DIR}/Source/LazDSS/Shared \
-Fu${OPENDSS_DIR}/Source/LazDSS/Common \
-Fu${OPENDSS_DIR}/Source/LazDSS/PDElements \
-Fu${OPENDSS_DIR}/Source/LazDSS/Controls \
-Fu${OPENDSS_DIR}/Source/LazDSS/General \
-Fu${OPENDSS_DIR}/Source/LazDSS/Meters \
-Fu${OPENDSS_DIR}/Source/LazDSS/PCElements \
-Fu${OPENDSS_DIR}/Source/LazDSS/Executive \
-Fu${OPENDSS_DIR}/Source/LazDSS/Parser \
-Fu${OPENDSS_DIR}/Source/LazDSS/DirectDLL/ \
-FU${OPENDSS_DIR}/Source/LazDSS/units/x86_64-linux/ \
-FE${OPENDSS_DIR}/Source/LazDSS/units/x86_64-linux/ \
-olibopendssdirect.so -dBorland -dVer150 -dDelphi7 -dCompiler6_Up -dPUREPASCAL \
${OPENDSS_DIR}/Source/LazDSS/DirectDLL/OpenDSSDirect.lpr

