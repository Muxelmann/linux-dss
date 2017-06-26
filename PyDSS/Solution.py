#!/bin/python3
import ctypes
from PyDSS import dsslib

dsslib.SolutionI.argtypes = [ctypes.c_int32, ctypes.c_int32]
dsslib.SolutionI.restype = ctypes.c_int32
dsslib.SolutionF.argtypes = [ctypes.c_int32, ctypes.c_double]
dsslib.SolutionF.restype = ctypes.c_double
dsslib.SolutionS.argtypes = [ctypes.c_int32, ctypes.c_char_p]
dsslib.SolutionS.restype = ctypes.c_char_p


def solve():
	"""Executes the solution for the present solution mode. Returns 0."""
	return dsslib.SolutionI(ctypes.c_int32(0), ctypes.c_int32(0))


def get_mode():
	"""This parameter returns the present solution mode (See DSS help)."""
	return dsslib.SolutionI(ctypes.c_int32(1), ctypes.c_int32(0))


def set_mode(mode):
	"""This parameter modifies the present solution mode (See DSS help)."""
	return dsslib.SolutionI(ctypes.c_int32(2), ctypes.c_int32(mode))


def get_hour():
	"""This parameter returns the present hour (See DSS help)."""
	return dsslib.SolutionI(ctypes.c_int32(3), ctypes.c_int32(0))


def set_hour(hour):
	"""This parameter modifies the present hour (See DSS help)."""
	return dsslib.SolutionI(ctypes.c_int32(4), ctypes.c_int32(hour))


def get_year():
	"""This parameter returns the present Year (See DSS help)."""
	return dsslib.SolutionI(ctypes.c_int32(5), ctypes.c_int32(0))


def set_year(year):
	"""This parameter modifies the present Year (See DSS help)."""
	return dsslib.SolutionI(ctypes.c_int32(6), ctypes.c_int32(year))


def iterations():
	"""This parameter return the number of iterations taken for the last solution."""
	return dsslib.SolutionI(ctypes.c_int32(7), ctypes.c_int32(0))


def get_max_iterations():
	"""This parameter returns the Maximum number of iterations used to solve the circuit."""
	return dsslib.SolutionI(ctypes.c_int32(8), ctypes.c_int32(0))


def set_max_iterations(max_iterations):
	"""This parameter modifies the Maximum number of iterations used to solve the circuit."""
	return dsslib.SolutionI(ctypes.c_int32(9), ctypes.c_int32(max_iterations))


def get_number():
	"""This parameter returns the number of solutions to perform for MonteCarlo and time series simulations."""
	return dsslib.SolutionI(ctypes.c_int32(10), ctypes.c_int32(0))


def set_number(number):
	"""This parameter modifies the number of solutions to perform for MonteCarlo and time series simulations."""
	return dsslib.SolutionI(ctypes.c_int32(11), ctypes.c_int32(number))


def get_random():
	"""This parameter returns the randomization mode for random variables "Gaussian" o "Uniform"."""
	return dsslib.SolutionI(ctypes.c_int32(12), ctypes.c_int32(0))


def set_random(random):
	"""This parameter modifies the randomization mode for random variables "Gaussian" o "Uniform"."""
	return dsslib.SolutionI(ctypes.c_int32(13), ctypes.c_int32(random))


def get_load_model():
	"""This parameter returns the Load Model: {dssPowerFlow (default)|dssAdmittance}."""
	return dsslib.SolutionI(ctypes.c_int32(14), ctypes.c_int32(0))


def set_load_model(load_model):
	"""This parameter modifies the Load Model: {dssPowerFlow (default)|dssAdmittance}."""
	return dsslib.SolutionI(ctypes.c_int32(15), ctypes.c_int32(load_model))


def get_algorithm():
	"""This parameter returns the base solution algorithm: {dssNormalSolve | dssNewtonSolve}."""
	return dsslib.SolutionI(ctypes.c_int32(18), ctypes.c_int32(0))


def set_algorithm(algorithm):
	"""This parameter modifies the base solution algorithm: {dssNormalSolve | dssNewtonSolve}."""
	return dsslib.SolutionI(ctypes.c_int32(19), ctypes.c_int32(algorithm))


def get_control_mode():
	"""This parameter returns the mode for control devices: {dssStatic (default) | dssEvent | dssTime}."""
	return dsslib.SolutionI(ctypes.c_int32(20), ctypes.c_int32(0))


def set_control_mode(control_mode):
	"""This parameter modifies the mode for control devices: {dssStatic (default) | dssEvent | dssTime}."""
	return dsslib.SolutionI(ctypes.c_int32(21), ctypes.c_int32(control_mode))


def get_control_iterations():
	"""This parameter returns the current value of the control iteration counter."""
	return dsslib.SolutionI(ctypes.c_int32(22), ctypes.c_int32(0))


def set_control_iterations(control_iterations):
	"""This parameter modifies the current value of the control iteration counter."""
	return dsslib.SolutionI(ctypes.c_int32(23), ctypes.c_int32(control_iterations))


def get_max_control_iterations():
	"""This parameter returns the maximum allowable control iterations."""
	return dsslib.SolutionI(ctypes.c_int32(24), ctypes.c_int32(0))


def set_max_control_iterations(max_control_iterations):
	"""This parameter modifies the maximum allowable control iterations."""
	return dsslib.SolutionI(ctypes.c_int32(25), ctypes.c_int32(max_control_iterations))


def sample_do_control_actions():
	"""This parameter modifies the maximum allowable control iterations."""
	return dsslib.SolutionI(ctypes.c_int32(26), ctypes.c_int32(0))


def check_fault_status():
	"""This parameter executes status check on all fault objects defined in the circuit. Returns 0."""
	return dsslib.SolutionI(ctypes.c_int32(27), ctypes.c_int32(0))


def solve_direct():
	"""This parameter executes a direct solution from the system Y matrix, ignoring compensation currents of loads, generators (includes Yprim only)."""
	return dsslib.SolutionI(ctypes.c_int32(28), ctypes.c_int32(0))


def solve_pflow():
	"""This parameter solves using present power flow method. Iterative solution rather than direct solution."""
	return dsslib.SolutionI(ctypes.c_int32(29), ctypes.c_int32(0))


def solve_no_control():
	"""This parameter is similar to SolveSnap except no control actions are checked or executed."""
	return dsslib.SolutionI(ctypes.c_int32(30), ctypes.c_int32(0))


def solve_plus_control():
	"""This parameter executes a power flow solution (SolveNoControl) plus executes a CheckControlActions that executes any pending control actions."""
	return dsslib.SolutionI(ctypes.c_int32(31), ctypes.c_int32(0))


def init_snap():
	"""This parameter initializes some variables for snap shot power flow. SolveSnap does this automatically."""
	return dsslib.SolutionI(ctypes.c_int32(32), ctypes.c_int32(0))


def check_controls():
	"""This parameter performs the normal process for sampling and executing Control Actions and Fault Status and rebuilds Y if necessary."""
	return dsslib.SolutionI(ctypes.c_int32(33), ctypes.c_int32(0))


def sample_control_devices():
	"""This parameter executes a sampling of all intrinsic control devices, which push control actions into the control queue."""
	return dsslib.SolutionI(ctypes.c_int32(34), ctypes.c_int32(0))


def do_control_actions():
	"""This parameter pops control actions off the control queue and dispatches to the proper control element."""
	return dsslib.SolutionI(ctypes.c_int32(35), ctypes.c_int32(0))


def build_y_matrix(whole_matrix=True):
	"""This parameter forces building of the System Y matrix according to the argument: {1= series elements only | 2= Whole Y matrix}."""
	if whole_matrix:
		return dsslib.SolutionI(ctypes.c_int32(36), ctypes.c_int32(2))
	else:
		return dsslib.SolutionI(ctypes.c_int32(36), ctypes.c_int32(1))


def system_y_changed():
	"""This parameter indicates if elements of the System Y have been changed by recent activity. If changed returns 1; otherwise 0."""
	return dsslib.SolutionI(ctypes.c_int32(37), ctypes.c_int32(0))


def get_converged():
	"""This parameter indicates whether the circuit solution converged (1 converged | 0 not converged)."""
	return dsslib.SolutionI(ctypes.c_int32(38), ctypes.c_int32(0))


def set_converged(converged=1):
	"""This parameter modifies the converged flag (1 converged | 0 not converged)."""
	return dsslib.SolutionI(ctypes.c_int32(39), ctypes.c_int32(converged))


def total_iterations():
	"""This parameter returns the total iterations including control iterations for most recent solution."""
	return dsslib.SolutionI(ctypes.c_int32(40), ctypes.c_int32(0))


def most_iterations_done():
	"""This parameter returns the max number of iterations required to converge at any control iteration of the most recent solution."""
	return dsslib.SolutionI(ctypes.c_int32(41), ctypes.c_int32(0))


def get_control_actions_done():
	"""This parameter indicates that the control actions are done: {1 done, 0 not done}."""
	return dsslib.SolutionI(ctypes.c_int32(42), ctypes.c_int32(0))


def set_control_actions_done(control_actions_done=1):
	"""This parameter modifies the flag to indicate that the control actions are done: {1 done, 0 not done}."""
	return dsslib.SolutionI(ctypes.c_int32(43), ctypes.c_int32(control_actions_done))


def finish_time_step():
	"""This parameter call cleanup, sample monitors, and increment time at end of time step."""
	return dsslib.SolutionI(ctypes.c_int32(44), ctypes.c_int32(0))


def cleanup():
	"""This parameter update storage, invcontrol, etc., at end of time step."""
	return dsslib.SolutionI(ctypes.c_int32(45), ctypes.c_int32(0))


def get_frequency():
	"""This parameter returns the frequency for the next solution."""
	return dsslib.SolutionF(ctypes.c_int32(0), ctypes.c_double(0))


def set_frequency(frequency=50.0):
	"""This parameter sets the frequency for the next solution."""
	return dsslib.SolutionF(ctypes.c_int32(1), ctypes.c_double(frequency))


def get_seconds():
	"""This parameter returns the seconds from top of the hour."""
	return dsslib.SolutionF(ctypes.c_int32(2), ctypes.c_double(0))


def set_seconds(seconds):
	"""This parameter sets the seconds from top of the hour."""
	return dsslib.SolutionF(ctypes.c_int32(3), ctypes.c_double(seconds))


def get_step_site():
	"""This parameter returns the step size for the next solution."""
	return dsslib.SolutionF(ctypes.c_int32(4), ctypes.c_double(0))


def set_step_size(step_size):
	"""This parameter sets the step size for the next solution."""
	return dsslib.SolutionF(ctypes.c_int32(5), ctypes.c_double(step_size))


def get_load_mult():
	"""This parameter returns the default load multiplier applied to all non-fixed loads."""
	return dsslib.SolutionF(ctypes.c_int32(6), ctypes.c_double(0))


def set_load_mult(load_mult=1.0):
	"""This parameter sets the default load multiplier applied to all non-fixed loads."""
	return dsslib.SolutionF(ctypes.c_int32(7), ctypes.c_double(load_mult))


def get_tolerance():
	"""This parameter returns the solution convergence tolerance."""
	return dsslib.SolutionF(ctypes.c_int32(8), ctypes.c_double(0))


def set_tolerance(tolerance):
	"""This parameter sets the solution convergence tolerance."""
	return dsslib.SolutionF(ctypes.c_int32(9), ctypes.c_double(tolerance))


def get_pct_annual_growth():
	"""This parameter returns the percent default annual load growth rate."""
	return dsslib.SolutionF(ctypes.c_int32(10), ctypes.c_double(0))


def set_pct_annual_grotth(pct_annual_growth):
	"""This parameter sets the percent default annual load growth rate."""
	return dsslib.SolutionF(ctypes.c_int32(11), ctypes.c_double(pct_annual_growth))


def get_gen_kW():
	"""This parameter returns the generator kW for AutoAdd mode."""
	return dsslib.SolutionF(ctypes.c_int32(12), ctypes.c_double(0))


def set_gen_kW(gen_kW):
	"""This parameter sets the generator kW for AutoAdd mode."""
	return dsslib.SolutionF(ctypes.c_int32(13), ctypes.c_double(gen_kW))


def get_gen_pf():
	"""This parameter returns the pf for generators in AutoAdd mode."""
	return dsslib.SolutionF(ctypes.c_int32(14), ctypes.c_double(0))


def set_gen_pf(gen_pf):
	"""This parameter sets the pf for generators in AutoAdd mode."""
	return dsslib.SolutionF(ctypes.c_int32(15), ctypes.c_double(gen_pf))


def get_cap_var():
	"""This parameter returns the capacitor kvar for adding in AutoAdd mode."""
	return dsslib.SolutionF(ctypes.c_int32(16), ctypes.c_double(0))


def set_cap_var(cap_var):
	"""This parameter sets the capacitor kvar for adding in AutoAdd mode."""
	return dsslib.SolutionF(ctypes.c_int32(17), ctypes.c_double(cap_var))


def get_gen_mult():
	"""This parameter returns the default multiplier applied to generators (like LoadMult)."""
	return dsslib.SolutionF(ctypes.c_int32(18), ctypes.c_double(0))


def set_gen_mult(gen_mult=1.0):
	"""This parameter sets the default multiplier applied to generators (like LoadMult)."""
	return dsslib.SolutionF(ctypes.c_int32(19), ctypes.c_double(gen_mult))


def get_dbl_hour():
	"""This parameter returns the hour as a double, including fractional part."""
	return dsslib.SolutionF(ctypes.c_int32(20), ctypes.c_double(0))


def set_dbl_hour(dbl_hour):
	"""This parameter sets the hour as a double, including fractional part."""
	return dsslib.SolutionF(ctypes.c_int32(21), ctypes.c_double(dbl_hour))


def step_size_min(minutes):
	"""This parameter sets the step size in minutes."""
	return dsslib.SolutionF(ctypes.c_int32(22), ctypes.c_double(minutes))


def step_size_hr(hours):
	"""This parameter sets the step size in Hours."""
	return dsslib.SolutionF(ctypes.c_int32(23), ctypes.c_double(hours))


def process_time():
	"""This parameter retrieves the time required (microseconds) to perform the latest solution time step, this time does not includes the time required for sampling meters/monitors."""
	return dsslib.SolutionF(ctypes.c_int32(24), ctypes.c_double(0))


def total_read_time():
	"""This parameter retrieves the accumulated time required (microseconds) to perform the simulation."""
	return dsslib.SolutionF(ctypes.c_int32(25), ctypes.c_double(0))


def total_write_time():
	"""This parameter sets the accumulated time (microseconds) register. The new value for this register must be specified in the argument."""
	return dsslib.SolutionF(ctypes.c_int32(26), ctypes.c_double(0))


def time_time_step():
	"""This parameter retrieves the time required (microseconds) to perform the latest solution time step including the time required for sampling meters/monitors."""
	return dsslib.SolutionF(ctypes.c_int32(27), ctypes.c_double(0))


def model_id():
	"""This parameter returns the ID (text) of the present solution mode."""
	return dsslib.SolutionS(ctypes.c_int32(0), ''.encode('ascii')).decode('ascii')


def get_ld_curve():
	"""This parameter returns the Load-Duration Curve name for LD modes."""
	return dsslib.SolutionS(ctypes.c_int32(1), ''.encode('ascii')).decode('ascii')


def set_ld_curve(ld_curve):
	"""This parameter sets the Load-Duration Curve name for LD modes."""
	return dsslib.SolutionS(ctypes.c_int32(2), ld_curve.encode('ascii')).decode('ascii')


def get_default_daily():
	"""This parameter returns the default daily load shape (defaults to "Default")."""
	return dsslib.SolutionS(ctypes.c_int32(3), ''.encode('ascii')).decode('ascii')


def set_default_daily(default_daily):
	"""This parameter sets the default daily load shape (defaults to "Default")."""
	return dsslib.SolutionS(ctypes.c_int32(4), default_daily.encode('ascii')).decode('ascii')


def get_default_yearly():
	"""This parameter returns the default yearly load shape (defaults to "Default")."""
	return dsslib.SolutionS(ctypes.c_int32(5), ''.encode('ascii')).decode('ascii')


def set_default_yearly(default_yearly):
	"""This parameter sets the default yearly load shape (defaults to "Default")."""
	return dsslib.SolutionS(ctypes.c_int32(6), default_yearly.encode('ascii')).decode('ascii')

