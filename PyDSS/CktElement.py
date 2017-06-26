#!/bin/python3
import ctypes
from PyDSS import dsslib

dsslib.CktElementI.argtypes = [ctypes.c_int32, ctypes.c_int32]
dsslib.CktElementI.restype = ctypes.c_int32
dsslib.CktElementF.argtypes = [ctypes.c_int32, ctypes.c_double]
dsslib.CktElementF.restype = ctypes.c_double
dsslib.CktElementS.argtypes = [ctypes.c_int32, ctypes.c_char_p]
dsslib.CktElementS.restype = ctypes.c_char_p


def num_terminals():
	"""This parameter will deliver the number of terminals of the active DSS object."""
	return dsslib.CktElementI(ctypes.c_int32(0), ctypes.c_int32(0))


def num_conductors():
	"""This parameter will deliver the number of conductors of the active DSS object."""
	return dsslib.CktElementI(ctypes.c_int32(1), ctypes.c_int32(0))


def num_phases():
	""""""
	return dsslib.CktElementI(ctypes.c_int32(2), ctypes.c_int32(0))


def open(terminal):
	"""This parameter will open the specified terminal (Argument) of the active DSS object."""
	return dsslib.CktElementI(ctypes.c_int32(3), ctypes.c_int32(terminal))


def close(terminal):
	"""This parameter will close the specified terminal (Argument) of the active DSS object."""
	return dsslib.CktElementI(ctypes.c_int32(4), ctypes.c_int32(terminal))


def is_open():
	"""This parameter will return a 1 if any terminal of the active DSS object is open, otherwise, it will return a 0."""
	return dsslib.CktElementI(ctypes.c_int32(5), ctypes.c_int32(0))


def get_normal_amps():
	"""This parameter will deliver the normal ampere rating for the active PDElement."""
	return dsslib.CktElementF(ctypes.c_int32(0), ctypes.c_double(0))


def set_normal_amps(amps=0.0):
	"""This parameter allows to fix the normal ampere rating for the active PDElement. The new value must be defined in the variable “Argument”."""
	return dsslib.CktElementF(ctypes.c_int32(1), ctypes.c_double(amps))


def get_emerg_amps():
	"""This parameter will deliver the Emergency ampere rating for the active PDElement."""
	return dsslib.CktElementF(ctypes.c_int32(2), ctypes.c_double(0))


def set_emerg_amps(amps=0.0):
	"""This parameter allows to fix the Emergency ampere rating for the active PDElement. The new value must be defined in the variable “Argument”."""
	return dsslib.CktElementF(ctypes.c_int32(3), ctypes.c_double(amps))


def name():
	"""This parameter delivers the full name of the active circuit element."""
	return dsslib.CktElementS(ctypes.c_int32(0), ''.encode('ascii')).decode('ascii')


def guid():
	"""This parameter delivers the unique name for the active circuit element."""
	return dsslib.CktElementS(ctypes.c_int32(3), ''.encode('ascii')).decode('ascii')


def energy_meter():
	"""This parameter delivers the name of the EnergyMeter linked to the active circuit element."""
	return dsslib.CktElementS(ctypes.c_int32(4), ''.encode('ascii')).decode('ascii')


def controller(index='1'):
	"""This parameter delivers the Full name of the i-th controller attached to the active circuit element. The i-th controller index must be specified in the argument arg. Ex: Str = Controller(2). See NumControls to determine valid index range."""
	return dsslib.CktElementS(ctypes.c_int32(5), index.encode('ascii')).decode('ascii')
