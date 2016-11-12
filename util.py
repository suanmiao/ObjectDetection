
def write_to_file(file_name, content, flag='w'):
    f_param = open(file_name, flag)
    f_param.write(str(content))
    f_param.close()

