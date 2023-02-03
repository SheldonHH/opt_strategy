#python main.py -e ../data/error/ida/speccpu/clang/O0/lbm-clang-O0-compilation-errors/ -s ../data/source/speccpu/int/ -opt O0 -c clang -o err_cat_lbm_clang_O0_ida -d ida > ida_speccpu_clang_O0_lbm-clang-O0-compilation-errors

import subprocess
import sys
import os
import re
import collections
# import pandas as pd
from re import search
from collections import defaultdict
import argparse
from typedef import *
from patterns import *


def get_config():
	"""
	get config information from command line
	"""
	parser = argparse.ArgumentParser()

	parser.add_argument('-e', '--error_folder', dest='error_folder',
						help='The folder of error recompiled file to be processed.', type=str, required=True)
	parser.add_argument('-s', '--source_folder', dest='source_folder',
						help='The directory of the original source code for the app.', type=str, required=False)
	parser.add_argument('-opt', '--opt', dest='opt_level',
						help='The optimization level when compiling the source code.', type=str, required=False)
	parser.add_argument('-c', '--compiler', dest='compiler',
						help='The compiler that  used to compile the source code.', type=str, required=False)
	
	parser.add_argument('-o', '--output_folder', dest='output_folder',
						help='The folder that saves the output.', type=str,
						required=False)

	parser.add_argument('-d', '--decompiler', dest='decompiler',
						help='The flag to indicate the decompiler.', type=str,
						required=False)
	

	args = parser.parse_args()

	config_info = {
		'source_folder': args.source_folder,
		'output_folder': args.output_folder,
		'opt_level': args.opt_level,
		'compiler': args.compiler,
		'error_folder': args.error_folder,
		'decompiler': args.decompiler
	}

	return config_info

def find_quote(text):
	quote_list = list()
	for i in range(len(text)):
		ch = text[i]
		if ch == "'":
			quote_list.append(i)

	return quote_list

def check_undeclared_identifier_ghidra(error_info):
	temp = error_info.split(';')
	error = temp[0]
	print("*yanlin error", error)
	quote_list = find_quote(error)
	first_index = quote_list[0]
	last_index = quote_list[1]

	var = error[first_index+1:last_index]
	cat = 'undeclared_variable'
	print("yanlin cat23",var)
	if var in GHIDRA.GHIDRA_TYPES:
		cat = 'undeclared_types_defined_by_GHIDRA'
	elif 'DAT_' in var or 'UNK_' in var or 'byte_' in var or 'PTR_' in var:
		cat = 'global_static_varible_value'
	elif var == '__va_list_tag':
		cat = 'variadic_function_va_list_tag'
	elif 'register0x' in var:
		cat = 'undeclared register0x?'
	elif 'stack0x' in var:
		cat = 'undeclared stack0x'
	else:
		for func in GHIDRA.GHIDRA_INTERNAL_FUNCS:
			if func in var:
				cat = 'undeclared_GHIDRA_internal_decompiler_func'
				break

	print("yanlin cat32 cat",cat)
	return cat

def check_unknown_type_ghidra(error_info):
	temp = error_info.split(';')
	error = temp[0]
	print("*yanlin unknown type error", error)
	quote_list = find_quote(error)
	first_index = quote_list[0]
	last_index = quote_list[1]

	var = error[first_index+1:last_index]
	cat = 'unknown type ?'
	print("yanlin cat23",var)
	if var in GHIDRA.GHIDRA_TYPES:
		cat = 'unknown_types_defined_by_GHIDRA'

	print("yanlin cat32 cat",cat)
	return cat

def check_undefined_func_ghidra(error_info):
	temp = error_info.split(';')
	error = temp[0]
	print("**yanlin error", error)
	quote_list = find_quote(error)
	first_index = quote_list[0]
	last_index = quote_list[1]

	var = error[first_index+1:last_index]
	cat = 'undefined_func'
	print("yanlin cat27",var)
	find = 0
	for func in GHIDRA_INTERNAL_FUNCS:
		if func in var:
			cat = 'undefined_GHIDRA_internal_decompiler_func'
			find = 1
			break

	print("yanlin cat27 cat",cat)
	return cat

def identify_error_pattern_ghidra(error):
	#print(pattern.patterns)
	print("error:",error)
	find_error_pattern = False
	for(reg_expression, type_name) in pattern.patterns:
		out = re.findall(reg_expression, error)
		# print("out:",out)
		if out:
			#print("find")
			find_error_pattern = True 
			return type_name

	return "unknown error"

def main():
	cat_error_counts = {}
	total_errors = 0
	error_distribution = defaultdict(set)
	unknown_errors = defaultdict(list)
	config_info = get_config()

	orig_proj_src_codes_folder = config_info['source_folder']
	error_dir = config_info['error_folder']
	opt = config_info['opt_level']
	compiler = config_info['compiler']
	#acsv = config_info['acsv']
	#bcsv = config_info['bcsv']

	output_dir = config_info['output_folder']
	decompiler = config_info['decompiler']

	print("maliha print")
	# print(output_dir)
	# print(decompiler)
	#os.system('mkidr -p '+output_dir)

	func_count = 1
	err_funcs =  [os.path.join(error_dir,f) for f in os.listdir(error_dir) if os.path.isfile(os.path.join(error_dir,f)) if ".cache" not in f]

	for err_func in err_funcs:
		err_funcfile = err_func.strip('\n')
		# print("err_funcfile:",err_funcfile)
		func_name = os.path.basename(err_funcfile)
		print("***************** Next Function ******************")
		print("func_count:",func_count)
		print("func_name '",func_name,"'")

		err_content = ''
		err_file_path = ''
		print("err_func:",err_funcfile)
		print("err_funcfile:",err_funcfile)
		with open(err_funcfile, 'r') as file:
			for line in file:
				line = line.rstrip()
				#print(line)
				if 'error: ' in line:
					total_errors += 1
					error_type_name = identify_error_pattern_ghidra(line)
					if "fatal error: too many errors emitted" not in line and "error: linker command failed with exit code 1" not in line:
						cat = error_type_name
						if error_type_name == "use of undeclared identifier":
							temp = line.split('error:')
							temp[1] = temp[1].replace('\xe2\x80\x98',"'")
							temp[1] = temp[1].replace('\xe2\x80\x99',"'")
							if decompiler == 'ghidra':
								cat = check_undeclared_identifier_ghidra(temp[1])
								cat = "use of undeclared identifier: "+cat 

						if error_type_name == "unknown type name":
							temp = line.split('error:')
							temp[1] = temp[1].replace('\xe2\x80\x98',"'")
							temp[1] = temp[1].replace('\xe2\x80\x99',"'")
							if decompiler == 'ghidra':
								cat = check_unknown_type_ghidra(temp[1])
								cat = "unknown type name: "+cat 

						if error_type_name == "undefined reference to a function":

							temp = line.split('error:')
							temp[1] = temp[1].replace('\xe2\x80\x98',"'")
							temp[1] = temp[1].replace('\xe2\x80\x99',"'")
							if decompiler == 'ghidra':
								cat = check_undefined_func_ghidra(temp[1])
								cat = "undefined reference to a function: "+cat 

						if cat not in cat_error_counts:
							cat_error_counts[cat] = 1 
						else:
							cat_error_counts[cat] += 1 

						error_distribution[cat].add(func_name)

						if cat == "unknown error":
							
							unknown_errors[func_name].append(line)

		func_count += 1
	print("******************** ================== ******************** ==================")
	print('Total # fns with errors: {}. Total errors: {}'.format(len(err_funcs), total_errors))
	print("******************** ================== error type: occurrences ******************** ==================")
	cat_error_counts = collections.OrderedDict(sorted(cat_error_counts.items()))
	for key, value in cat_error_counts.items():
		print('{}: {}'.format(key, value))


	error_func_count = dict()
	for cat in error_distribution:
		funcs = error_distribution[cat]

		error_func_count[cat] = len(funcs)

	print("******************** ================== error distribution ******************** ==================")
	print("******************** ================== error type: func count ******************** ==================")
	error_func_count = collections.OrderedDict(sorted(error_func_count.items()))
	for key,value in error_func_count.items():
		print('{}: {}'.format(key, value))

	print("******************** ================== unknown errors ******************** ==================")
	#print(unknown_errors)
	for func in unknown_errors:
		print(func, unknown_errors[func])


if __name__ == '__main__':
	main()
