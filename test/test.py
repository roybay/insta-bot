def file_read(fname):
    content_array = []
    with open(fname) as f:
        #Content_list is the list that contains the read lines.     
        for line in f:
            content_array.append(line.rstrip())
        print(content_array)

file_read('../firstname.txt')