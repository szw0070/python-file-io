#!/usr/bin/env python3

# script should use regular expressions to...
# find all words related to heritability:
#   heritable
#   inherit
#   inheritance
#   other forms of these words
# and write the line number that the word is found on with a tab ('\t') then the word

def find_words():
    print('opening origin.txt')
    with open('origin.txt', 'r') as in_stream:
        print('opening output.txt')
        with open('origin_output.txt','w') as out_stream:
            for line in in_stream:
                line = line.strip()
                word_list = line.split()
                word_list.sort()
                for word in word_list:
                    out_stream.write('{0}\n'.format(word))
    print('Done')
    print('dummy.txt is closed?', in_stream.closed)
    print('origin_output is closed?', out_stream.closed)

find_words()
