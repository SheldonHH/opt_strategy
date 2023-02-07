# extensions
import os
ext = ('.txt', 'jpg')
 
# scanning the directory to get required files
all_dict = {}
f_cont = 0
for files in os.scandir("/data/Feb_2_2023/gcc_res/"):
    f_cont+=1
    if files.path.endswith(ext):
        fp = open(files)
        fkey = fp
        subdict = {}
        for i, line in enumerate(fp):
            if i > 3:
                print("line:",line)
                if ":" in line:
                    err_key = line[0:line.index(":")]
                    value = [line.index(":"),len(line)]
                    
                    subdict[err_key] = value 
                    if err_key in all_dict:
                        old_v = all_dict[err_key]
                        old_v.update(subdict)
                        all_dict[err_key] = old_v

                    else:
                        all_dict[err_key] = subdict
                # break
        fp.close()
print("all_dict",all_dict)
    