# python batch_run.py /data/maliha/decompilation/data/error/ida/speccpu/clang/O0 /data/maliha/decompilation/data/source/speccpu/int speccpu_clang_O0
import os
import sys

def find_util_name(text):
	text = text.split('-')

	utilname = text[0]

	return utilname


if __name__ == '__main__':
	decompiled_err_dir = sys.argv[1]
	source_dir = sys.argv[2]
	err_distribution_dir = sys.argv[3]
	decompiler = 'ida'

	print("****** Maliha *******")
	print("err_distribution_dir:",err_distribution_dir)
	print("decompiled_err_dir:",decompiled_err_dir)

	cmd = "mkdir -p "+ err_distribution_dir
	print("*** create err_distribution_file: ****",cmd)
	os.system(cmd)
	
	subdir =  next(os.walk(decompiled_err_dir))[1]

	for dirname in subdir:
		decompiledErr = os.path.join(decompiled_err_dir, dirname)

		print("*** inside ***")
		print("decompiledErr:",decompiledErr)

		utilname = find_util_name(dirname)
		print("utilname:",utilname)		

		#if 'KPRCA_00010-clang-O0' not in subdir:
			#continue

		if utilname == 'bzip2':
			utilname = '401.bzip2'
		if utilname == 'gcc':
			utilname = '403.gcc'

		if utilname == 'gobmk':
			utilname = '445.gobmk'
		if utilname == 'sjeng':
			utilname = '458.sjeng'

		if utilname == 'mcf':
			utilname = '429.mcf'
		if utilname == 'libquantum':
			utilname = '462.libquantum'

		if utilname == 'lbm':
			utilname = '470.lbm'


		sourcePath = os.path.join(source_dir,utilname+'/src')
		err_distribution = os.path.join(err_distribution_dir, dirname)
		err_csv1 = os.path.join(err_distribution_dir,dirname+'_a.csv')
		err_csv2 = os.path.join(err_distribution_dir,dirname+'_b.csv')

		cmd = "python main.py -e "+ decompiledErr  +' -d '+decompiler+' > '+err_distribution
		print("********* final command ******", cmd)		
		os.system(cmd)

# python batch_run.py /data/maliha/decompilation/data/error/ida/speccpu/clang/O0 /data/maliha/decompilation/data/source/speccpu/int speccpu_clang_O0
		