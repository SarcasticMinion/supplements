def read_log_or_out(fileObj, thermo_output_list):

    flag = False
    for line in fileObj:
        data = line.split()
        try:
            if data[0] == 'Loop':
                flag = False
            if flag:
                yield (int(data[0]), float(data[1]))
            if data == thermo_output_list:
                flag = True
        except (IndexError, ValueError):
            pass
