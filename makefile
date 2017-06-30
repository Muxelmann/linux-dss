OPENDSS_DIR		?= electricdss

CC		= /usr/bin/fpc
MACROS	= -MDelphi -Scghi -Ct -O2  -k-lc -k-lm -k-lgcc_s -k-lstdc++ -l -vewnhibq
CFLAGS	= -dBorland -dVer150 -dDelphi7 -dCompiler6_Up -dPUREPASCAL -dCPU64
OUT		= libopendssdirect.so
TMP		= ./tmp
LIB		= ./lib

KLUSOLVE = KLUSolve
KLUSOLVE_LIB = ${KLUSOLVE}/Lib
KLUSOLVE_TEST = ${KLUSOLVE}/Test

all: ${TMP} ${LIB} update_dss klusolve
	$(CC) \
	-Px86_64 -Cg $(MACROS) \
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
	-Fl${KLUSOLVE_LIB} \
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
	-FU${TMP} \
	-FE${LIB} \
	-o${OUT} \
	${CFLAGS} \
	${OPENDSS_DIR}/Source/LazDSS/DirectDLL/OpenDSSDirect.lpr

arm: ${TMP} ${LIB} update_dss klusolve
	$(CC) \
	-Parm  $(MACROS) \
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
	-Fi${OPENDSS_DIR}/Source/LazDSS/units/arm-linux \
	-Fl${KLUSOLVE_LIB} \
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
	-Fu${TMP} \
	-FE${LIB} \
	-o${OUT} \
	${CFLAGS} \
	${OPENDSS_DIR}/Source/LazDSS/DirectDLL/OpenDSSDirect.lpr

klusolve:
	mkdir ${KLUSOLVE}
	svn checkout https://svn.code.sf.net/p/klusolve/code/ ${KLUSOLVE}
	mkdir -p ${KLUSOLVE_LIB}
	mkdir -p ${KLUSOLVE_TEST}
	make -C ${KLUSOLVE}

light: update_dss all
	rm -fr ${TMP}

${TMP}:
	mkdir -p ${TMP}

${LIB}:
	mkdir -p ${LIB}

clean:
	rm -rf ${TMP}
	rm -rf ${LIB}

update_dss: ${OPENDSS_DIR}
	svn update ${OPENDSS_DIR}

${OPENDSS_DIR}:

	mkdir ${OPENDSS_DIR}
	svn checkout https://svn.code.sf.net/p/electricdss/code/trunk ${OPENDSS_DIR}
