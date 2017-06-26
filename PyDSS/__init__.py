#!/bin/python3
import os, ctypes

dsslib_path = os.path.abspath('/'.join(__file__.split('/')[:-2])) + '/lib/libopendssdirect.so'
dsslib = ctypes.CDLL(dsslib_path)
