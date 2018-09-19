import os
number = 37    # Put lowest number file here
last_number = 95   # Put highest number of file here
first = "e:/"
title_first = "MD"
last = ".raw"
number_string = str(number)
title = title_first+number_string
path = first+title_first+number_string+last  # makes folder name
global copy_text

while number <= last_number:
    if os.path.exists(path):
        os.chdir("c:/users/user/desktop")
        with open("titles.txt","r+") as copy_file:
            for line_copy in copy_file:
                if title in line_copy:
                    idx = line_copy.find("\n")
                    idx_number = idx - 5
                    copy_text = line_copy[5:idx]
                    print(copy_text)
        os.chdir(path)   # brings me into folder
        number += 1
        number_string = str(number)
        title = title_first + number_string
        path = first + title_first + number_string + last  # makes folder name
        with open('_HEADER.txt','r+') as input_files:
            with open('HEADER.txt', 'a') as f:
                for line in input_files:
                    if 'Sample' in line:
                        f.write(line[:23] + copy_text + line[23:])
                        print(line)
                    else:
                        f.write(line)
                        print(line)
        os.remove('_HEADER.txt')
        os.rename('HEADER.txt', '_HEADER.txt')
    else:
        number += 1
        number_string = str(number)
        title = title_first + number_string
        path = first + title_first + number_string + last  # makes folder name
