class GHIDRA():
	GHIDRA_TYPES=['undefined', 'unsigned_short','byte','dwfenc','dword','qword','ulong','undefined1','undefined2','undefined4',
			'undefined8', 'word','ll','ull','uint','uchar','ushort','ulong','int8','sint8','uint8','int16','sint16','uint16',
			'int32','sint32','uint32','int64','sint64','uint64','bool','__int64','__int32','__int16','__int8','_BYTE','_WORD',
			'_DWORD','_QWORD','_LONGLONG','true','false','ulonglong','longlong']


	GHIDRA_INTERNAL_FUNCS=['SEXT','ZEXT','SUB','SBORROW','CARRY','SCARRY','CONCAT']


# get from ida.h
# ida.h //
class IDA():
	def __init__(self):
		pass
#: error: use of undeclared identifier
	IDA_TYPES=['_BYTE','_WORD','_DWORD','_QWORD','_OWORD','_UNKNOWN','__int8','unsigned __int8','__int16','__int64','__m128','__m256','__va_list_tag','__int32', '_cpp_buff_0','__pid_t', '__ino64_t', '__mode_t', '__ino_t', '__nlink_t', '__m64', '__dev_t', '__off_t', '__m128', '__m128d', '__uid_t', '__gnuc_va_list', '__m128i','__time_t','_IO_FILE', '__stream','__off64_t']

# : error: unknown type name
IDA_INTERNAL_FUNCS=['_BOOL4','_BOOL8','_getopt_initialized','_cpp_buff_0','__sighandler_t','__blksize_t','__syscall_slong_t', '_mask', '_obstack_chunk', '_ascii_bytes', '__c', '__b','__ino_t', '_force', '_remote']
