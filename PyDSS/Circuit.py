#!/bin/python3
import ctypes
from PyDSS import dsslib

dsslib.CircuitI.argtypes = [ctypes.c_int32, ctypes.c_int32]
dsslib.CircuitI.restype = ctypes.c_int32
dsslib.CircuitF.argtypes = [ctypes.c_int32, ctypes.c_double, ctypes.c_double]
dsslib.CircuitF.restype = ctypes.c_double
dsslib.CircuitS.argtypes = [ctypes.c_int32, ctypes.c_char_p]
dsslib.CircuitS.restype = ctypes.c_char_p


def num_ckt_elements():
	"""This parameter will deliver the number of CktElements included in the active circuit."""
	return dsslib.CircuitI(ctypes.c_int32(0), ctypes.c_int32(0))


def num_buses():
	"""This parameter will deliver the number of buses included in the active circuit."""
	return dsslib.CircuitI(ctypes.c_int32(1), ctypes.c_int32(0))


def num_nodes():
	"""This parameter will deliver the number of nodes included in the active circuit."""
	return dsslib.CircuitI(ctypes.c_int32(2), ctypes.c_int32(0))


def first_pc_element():
	"""This parameter sets the first PCElement to be the active PCElement, as a result, this parameter will deliver the index of the active PCElement (ideally 1)."""
	return dsslib.CircuitI(ctypes.c_int32(3), ctypes.c_int32(0))


def next_pc_element():
	"""This parameter sets the next PCElement to be the active PCElement, as a result, this parameter will deliver the index of the active PCElement (if there is no more it will return a 0)."""
	return dsslib.CircuitI(ctypes.c_int32(4), ctypes.c_int32(0))


def first_pd_element():
	"""This parameter sets the first PDElement to be the active PDElement, as a result, this parameter will deliver the index of the active PDElement (ideally 1)."""
	return dsslib.CircuitI(ctypes.c_int32(5), ctypes.c_int32(0))


def next_pd_element():
	"""This parameter sets the next PDElement to be the active PDElement, as a result, this parameter will deliver the index of the active PDElement (if there is no more it will return a 0)."""
	return dsslib.CircuitI(ctypes.c_int32(6), ctypes.c_int32(0))


def sample():
	"""This parameter forces all meters and monitors to take a sample, returns 0."""
	return dsslib.CircuitI(ctypes.c_int32(7), ctypes.c_int32(0))


def save_sample():
	"""This parameter forces all meters and monitors to save their sample buffers, returns 0."""
	return dsslib.CircuitI(ctypes.c_int32(8), ctypes.c_int32(0))


def set_active_nbus(index):
	"""This parameter sets active the bus specified by index, which is compatible with the index delivered by AllBusNames, returns 0 it everything ok."""
	return dsslib.CircuitI(ctypes.c_int32(9), ctypes.c_int32(index))


def first_element():
	"""This parameter sets the first Element of the active class to be the active Element, as a result, this parameter will deliver the index of the active Element (0 if none)."""
	return dsslib.CircuitI(ctypes.c_int32(10), ctypes.c_int32(0))


def next_element():
	"""This parameter sets the next Element of the active class to be the active Element, as a result, this parameter will deliver the index of the active Element (0 if none)."""
	return dsslib.CircuitI(ctypes.c_int32(11), ctypes.c_int32(0))


def update_storage():
	"""This parameter forces all storage classes to update. Typically done after a solution."""
	return dsslib.CircuitI(ctypes.c_int32(12), ctypes.c_int32(0))


def parent_pd_element():
	"""This parameter sets parent PD Element, if any, to be the active circuit element and returns index > 0 if it fails or not applicable."""
	return dsslib.CircuitI(ctypes.c_int32(13), ctypes.c_int32(0))


def end_of_time_step_update():
	"""This parameter calls end of time step cleanup routine in solutionalgs.pas. Returns 0."""
	return dsslib.CircuitI(ctypes.c_int32(14), ctypes.c_int32(0))


def capacity(c_start=0.0, c_increment=0.0):
	"""This parameter returns the total capacity of the active circuit. Or this parameter it is necessary to specify the start and increment of the capacity in the arguments argument1 and argument2 respectively."""
	return dsslib.CircuitF(ctypes.c_int32(0), ctypes.c_double(c_start), ctypes.c_double(c_increment))


def name():
	"""This parameter returns the name of the active circuit."""
	return dsslib.CircuitS(ctypes.c_int32(0), ''.encode('ascii')).decode('ascii')


def disable(element):
	"""This parameter allows to disable an element of the active circuit, the element must be specified by name. As a result, this parameter will deliver the string “Ok”."""
	return dsslib.CircuitS(ctypes.c_int32(1), element.encode('ascii')).decode('ascii')


def enable(element):
	"""This parameter allows to enable an element of the active circuit, the element must be specified by name. As a result, this parameter will deliver the string “Ok”."""
	return dsslib.CircuitS(ctypes.c_int32(2), element.encode('ascii')).decode('ascii')


def set_active_element(element):
	"""This parameter allows to activate an element of the active circuit, the element must be specified by name. As a result, this parameter will deliver a string with the index of the active element."""
	return dsslib.CircuitS(ctypes.c_int32(3), element.encode('ascii')).decode('ascii')


def set_active_bus(bus):
	"""This parameter allows to activate a bus of the active circuit, the bus must be specified by name. As a result, this parameter will deliver a string with the index of the active Bus."""
	return dsslib.CircuitS(ctypes.c_int32(4), bus.encode('ascii')).decode('ascii')


def set_active_class(class_name):
	"""This parameter allows to activate a Class of the active circuit, the Class must be specified by name. As a result, this parameter will deliver a string with the index of the active Class."""
	return dsslib.CircuitS(ctypes.c_int32(5), class_name.encode('ascii')).decode('ascii')
