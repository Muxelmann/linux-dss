#!/bin/python3
import ctypes
from PyDSS import dsslib

dsslib.BUSI.argtypes = [ctypes.c_int32, ctypes.c_int32]
dsslib.BUSI.restype = ctypes.c_int32
dsslib.BUSF.argtypes = [ctypes.c_int32, ctypes.c_double]
dsslib.BUSF.restype = ctypes.c_double
dsslib.BUSS.argtypes = [ctypes.c_int32, ctypes.c_char_p]
dsslib.BUSS.restype = ctypes.c_char_p


def num_nodes():
	"""This parameter returns the number of nodes of this bus."""
	return dsslib.BUSI(ctypes.c_int32(0), ctypes.c_int32(0))


def coord_defined():
	"""This parameter returns 1 if a coordinate has been defined for this bus; otherwise, it will return 0."""
	return dsslib.BUSI(ctypes.c_int32(2), ctypes.c_int32(0))


def get_unique_node_number():
	"""This parameter returns a unique node number at the active bus to avoid node collisions and adds it to the node list for the bus. The start number can be specified in the argument."""
	return dsslib.BUSI(ctypes.c_int32(3), ctypes.c_int32(0))


def n_customers():
	"""This parameter returns the total number of customers server down line from this bus."""
	return dsslib.BUSI(ctypes.c_int32(4), ctypes.c_int32(0))


def section_id():
	"""This parameter returns the integer ID of the feeder section in which this bus is located."""
	return dsslib.BUSI(ctypes.c_int32(5), ctypes.c_int32(0))


def kV_base():
	"""This parameter returns the base voltage at bus in kV."""
	return dsslib.BUSF(ctypes.c_int32(0), ctypes.c_double(0))


def get_x():
	"""This parameter returns the X coordinate for the bus."""
	return dsslib.BUSF(ctypes.c_int32(1), ctypes.c_double(0))


def set_x(x):
	"""This parameter allows to write the X coordinate for the bus. Returns 0."""
	return dsslib.BUSF(ctypes.c_int32(2), ctypes.c_double(x))


def get_y():
	"""This parameter returns the Y coordinate for the bus."""
	return dsslib.BUSF(ctypes.c_int32(3), ctypes.c_double(0))


def set_y(y):
	"""This parameter allows to write the Y coordinate for the bus. Returns 0."""
	return dsslib.BUSF(ctypes.c_int32(4), ctypes.c_double(y))


def distance():
	"""This parameter returns the distance from the energymeter (if non-zero)."""
	return dsslib.BUSF(ctypes.c_int32(5), ctypes.c_double(0))


def n_failures(): # defined as "lambda"
	"""This parameter returns the accumulated failure rate downstream from this bus; faults per year."""
	return dsslib.BUSF(ctypes.c_int32(6), ctypes.c_double(0))


def n_interrupts():
	"""This parameter returns the number of interruptions this bus per year."""
	return dsslib.BUSF(ctypes.c_int32(7), ctypes.c_double(0))


def int_diration():
	"""This parameter returns the average interruption duration in hours."""
	return dsslib.BUSF(ctypes.c_int32(8), ctypes.c_double(0))


def cust_interruptions():
	"""This parameter returns the annual number of customer interruptions from this bus."""
	return dsslib.BUSF(ctypes.c_int32(9), ctypes.c_double(0))


def cust_duration():
	"""This parameter returns the accumulated customer outage durations."""
	return dsslib.BUSF(ctypes.c_int32(10), ctypes.c_double(0))


def total_miles():
	"""This parameter returns the total length of line downline from this bus, in miles. For recloser siting algorithm."""
	return dsslib.BUSF(ctypes.c_int32(11), ctypes.c_double(0))


def name():
	"""This parameter returns the name of the active bus."""
	return dsslib.BUSS(ctypes.c_int32(0), ''.encode('ascii')).decode('ascii')
