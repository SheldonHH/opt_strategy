rm -rf /data/Feb_2_2023/error_categorize/speccpu_*
sleep 3
echo "sleep 3s"
python batch_run.py /data/0202_patch/ida/speccpu/clang/O0 /data/SSSSSS/SPECCPU2006/int speccpu_clang_O0
python batch_run.py /data/0202_patch/ida/speccpu/clang/O1 /data/SSSSSS/SPECCPU2006/int speccpu_clang_O1
python batch_run.py /data/0202_patch/ida/speccpu/clang/O2 /data/SSSSSS/SPECCPU2006/int speccpu_clang_O2
python batch_run.py /data/0202_patch/ida/speccpu/clang/O3 /data/SSSSSS/SPECCPU2006/int speccpu_clang_O3
python batch_run.py /data/0202_patch/ida/speccpu/gcc/O0 /data/SSSSSS/SPECCPU2006/int speccpu_gcc_O0
python batch_run.py /data/0202_patch/ida/speccpu/gcc/O1 /data/SSSSSS/SPECCPU2006/int speccpu_gcc_O1
python batch_run.py /data/0202_patch/ida/speccpu/gcc/O2 /data/SSSSSS/SPECCPU2006/int speccpu_gcc_O2
python batch_run.py /data/0202_patch/ida/speccpu/gcc/O3 /data/SSSSSS/SPECCPU2006/int speccpu_gcc_O3