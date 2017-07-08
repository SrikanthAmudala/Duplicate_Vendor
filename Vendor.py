import sys


def output_text(path, common_vendor, user_input_line, index):
    output_file_path = 'text/new_vendor_list.txt'
    output_file = open(output_file_path, 'w')
    # print common_vendor
    with open(path) as f:
        for line in f:
            temp = line.strip()
            if temp.upper() not in common_vendor[int(index) - 1]:
                output_file.write(line)
    output_file.write(user_input_line.upper() + '\n')
    return output_file_path


def word_list(path):
    list_of_words = []
    with open(path) as f:
        for line in f:
            list_of_words.append(line.strip().upper())
    return list_of_words


def duplicate_words(x, n):
    x = sorted(x)
    y = []
    z = []

    if n == 1:
        for i in x:
            for j in x:
                if i == j:
                    pass
                elif (i.split(' ')[0]) == (j.split(' ')[0]):
                    y.append(j)
                else:
                    pass

            y = set(y)
            for k in y:
                x.remove(k)
            y = list(y)

            y.append(i)
            z.append(y)
            y = []

    elif n == 2:
        for i in x:
            if len(i.split(' ')) >= 2:
                for j in x:

                    if i == j:
                        pass
                    elif len(j.split(' ')) >= 2:
                        p = i.split(' ')
                        q = j.split(' ')
                        if (p[0] + p[1]) == (q[0] + q[1]):
                            y.append(j)
                    else:
                        pass

                y = set(y)
                for k in y:
                    x.remove(k)
                y = list(y)

                y.append(i)
                z.append(y)
                y = []

    elif n == 3:
        for i in x:
            if len(i.split(' ')) >= 3:
                for j in x:

                    if i == j:
                        pass
                    elif len(j.split(' ')) >= 3:
                        p = i.split(' ')
                        q = j.split(' ')
                        if (p[0] + p[1] + p[2]) == (q[0] + q[1] + q[2]):
                            y.append(j)
                    else:
                        pass

                y = set(y)
                for k in y:
                    x.remove(k)
                y = list(y)

                y.append(i)
                z.append(y)
                y = []

    elif n == 4:
        for i in x:
            if len(i.split(' ')) >= 4:
                for j in x:

                    if i == j:
                        pass
                    elif len(j.split(' ')) >= 4:
                        p = i.split(' ')
                        q = j.split(' ')
                        if (p[0] + p[1] + p[2] + p[3]) == (q[0] + q[1] + q[2] + q[3]):
                            y.append(j)
                    else:
                        pass

                y = set(y)
                for k in y:
                    x.remove(k)
                y = list(y)

                y.append(i)
                z.append(y)
                y = []

    else:
        print 'Max Words to match are 4'
    final_list = []
    for i in z:
        if len(i) > 1:
            final_list.append(i)
            # print i
    return final_list


path = 'text/vendor_list.txt'
x = word_list(path)
flag = 0
while flag == 0:
    n = raw_input('Give the No of words you want to compare (n<5): ')
    if n == '':
        print 'input can not be empty'
    elif int(n) > 4:
        print ('No of words must be less than 5, Try again!')
    else:
        n = int(n)
        flag = 1
        duplicate_vendors = duplicate_words(x, n)
        for i in range(0, len(duplicate_vendors)):
            print str(i + 1) + '. ' + str(duplicate_vendors[i])
        flag1 = 0
        while (flag1 == 0):
            index = raw_input('Give the folder number which you want to rename or give 0 to exit: ')
            if int(index) == 0:
                sys.exit()
            rename = raw_input('Give the name you wish to change: ')
            output = output_text(path, duplicate_vendors, str(rename).upper(), int(index))
            print 'New Vendor list save to: ', output
