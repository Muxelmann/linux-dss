#!/bin/python3
import ctypes
from PyDSS import dsslib

# Define argument types and result types
dsslib.DSSI.argtypes = [ctypes.c_int32, ctypes.c_int32]
dsslib.DSSI.restype = ctypes.c_int32
dsslib.DSSS.argtypes = [ctypes.c_int32, ctypes.c_char_p]
dsslib.DSSS.restype = ctypes.c_char_p


def num_circuits():
	"""This parameter gets the number of circuits currently defined."""
	return dsslib.DSSI(ctypes.c_int32(0), ctypes.c_int32(0))


def clear_all():
	"""This parameter clears all circuit definitions."""
	return dsslib.DSSI(ctypes.c_int32(1), ctypes.c_int32(0))


def start():
	"""This parameter validate the user and start the DSS. Returns TRUE (1) if successful."""
	return dsslib.DSSI(ctypes.c_int32(3), ctypes.c_int32(0))


def reset():
	"""This parameter resets DSS initialization for restarts, etc. from applets."""
	return dsslib.DSSI(ctypes.c_int32(6), ctypes.c_int32(0))


def new_circuit(circuit_name='UNNAMED'):
	"""This parameter makes a new circuit, the name of the circuit is 'UNNAMED' by default."""
	return dsslib.DSSS(ctypes.c_int32(0), circuit_name.encode('ascii')).decode('ascii')


def version():
	"""This parameter gets the version string for the DSS."""
	return dsslib.DSSS(ctypes.c_int32(1), ''.encode('ascii')).decode('ascii')

