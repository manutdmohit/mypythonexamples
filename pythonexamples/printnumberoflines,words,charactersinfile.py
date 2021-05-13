import os
fname=input('Enter File Name:')
if os.path.isfile(fname):
    print('File Exists:',fname)
    lcount=wcount=ccount=0
    f=open(fname,'r')
    for line in f:
        lcount=lcount+1
        no_of_words_in_current_line=len(line.split())
        wcount=wcount+no_of_words_in_current_line
        no_of_characters_in_current_line=len(line)
        ccount=ccount+no_of_characters_in_current_line

    print('The Number of lines:',lcount) 
    print('The Number of words:',wcount)
    print('The Number of character:',ccount) 

else:
    print('The file does not exist:',fname)