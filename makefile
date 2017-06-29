OPENDSS_DIR		?= electricdss

CC		= /usr/bin/fpc
MACROS	= -MDelphi -Scghi -Ct -O2  -k-lc -k-lm -k-lgcc_s -k-lstdc++ -l -vewnhibq
CFLAGS	= -dBorland -dVer150 -dDelphi7 -dCompiler6_Up -dPUREPASCAL
OUT		= libopendssdirect.so
TMP		= ./tmp/
LIB		= ./lib/

all: ${TMP} ${LIB} update_dss
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
	-FU${TMP} \
	-FE${LIB} \
	-o${OUT} \
	${CFLAGS} \
	${OPENDSS_DIR}/Source/LazDSS/DirectDLL/OpenDSSDirect.lpr

arm: ${TMP} ${LIB} update_dss
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
	-Fu${OPENDSS_DIR}/Source/LazDSS/units/arm-linux/ \
	-FE${OPENDSS_DIR}/Source/LazDSS/units/arm-linux/ \
	-o${OUT} \
	${CFLAGS} \
	${OPENDSS_DIR}/Source/LazDSS/DirectDLL/OpenDSSDirect.lpr

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
