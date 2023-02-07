# extensions
import os
import csv
ext = ('.txt', 'jpg')
 
# scanning the directory to get required files
all_dict = {}
f_cont = 0
for files in os.scandir("/data/Feb_2_2023/gcc_res/"):
    if files.path.endswith(ext):

        f_cont+=1
        fp = open(files)
        fkey = fp
        subdict = {}
        for i, line in enumerate(fp):
            if i > 2:
                # print("line:",line)
                if ":" in line:
                    print(line)
                    err_key = line[0:line.index(":")]
                    value = line[line.index(":")+2:len(line)-1]
                    # print("value",value)
                    if value != "":
                        subdict[err_key] = value
                
                # break
        fp.close()
        all_dict[str(f_cont)] = subdict
        with open(str(f_cont)+'.csv', 'w') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in subdict.items():
                writer.writerow([key, value])
# print("all_dict",all_dict)
print(all_dict['1'])
