#!/usr/bin/python
from nltk.tokenize import word_tokenize


def word_list(path):
    list_of_words = []
    with open(path) as f:
        for line in f:
            y = word_tokenize(line)
            list_of_words.append(y)
    return list_of_words


def vendor_list_word_count(x, n):
    vendor_list = []
    for i in x:
        temp = ''
        for j in i:
            temp += j.upper() + ' '
        vendor_list.append(temp.strip())

    vendor_common_list_temp = []
    vendor_common_list = []

    for i in x:
        if len(i) >= n:
            vendor = ''
            for j in range(0, n):
                # print '####'
                vendor += i[j].upper() + ' '
            vendor = vendor.strip()
            for k in vendor_list:
                if vendor in k:
                    # print 'k: ',k
                    vendor_common_list_temp.append(k.upper())
                    # vendor_list.remove(k)
    # print vendor_common_list_temp

    for i in vendor_common_list_temp:
        if vendor_common_list_temp.count(i) > 1:
            vendor_common_list.append(i)

    return sorted(set(vendor_common_list))


def output_text(path, common_vendor, user_input_line, index):
    output_file_path = 'text/new_vendor_list.txt'
    output_file = open(output_file_path, 'w')
    vendor = []
    with open(path) as f:
        for line in f:
            temp = line.strip()

            if temp.upper() not in common_vendor[int(index)-1]:
                output_file.write(line)
    output_file.write(user_input_line.upper() + '\n')
    return output_file_path


path = 'text/vendor_list.txt'
x = word_list(path)
flag = 0
final_vendor_list_temp=[]
while flag == 0:
    n = raw_input('Number of words you want to match: ')
    vendor_list = vendor_list_word_count(x, int(n))
    final_vendor_list = []

    for i in range(0, len(vendor_list) - 1):
        if vendor_list[i] in vendor_list[i + 1]:
            final_vendor_list.append(vendor_list[i])
            final_vendor_list.append(vendor_list[i + 1])
            # added this line
        else:
            if len(final_vendor_list) > 0:
                final_vendor_list_temp.append(set(final_vendor_list))
                final_vendor_list=[]

    final_vendor_list = sorted(set(final_vendor_list))

    if len(final_vendor_list) > 0:
        final_vendor_list_temp.append(final_vendor_list)

    # print 'temp: ', final_vendor_list_temp

    if len(final_vendor_list_temp) > 0:
        # print 'Vendor List: ', final_vendor_list_temp
        final_vendor_list_temp = list(final_vendor_list_temp)
        final_vendor_list_temp_1=[]
        for i in final_vendor_list_temp:
            final_vendor_list_temp_1.append(list(i))
            # print i
        # print ''final_vendor_list_temp_1
        for i in range(0, len(final_vendor_list_temp_1)):
            print str(i+1)+'. '+str(final_vendor_list_temp_1[i])
        index = raw_input('Give the folder number which you want to rename: ')
        rename = raw_input('Give the name you wish to change               : ')
        output = output_text(path, final_vendor_list_temp, str(rename).upper(), int(index))
        print 'New Vendor list save to: ', output
        flag = 1
    else:
        print 'No Vendor has ' + n + ' common words.'
