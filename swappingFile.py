def swappingFiles():
    f1= input('file 1 to swap')
    f2= input('file2 to swap')

    file1= open(f1, 'r')
    data_a= file1.read()
    file1.close()

    file2= open(f2, 'r')
    data_b= file2.read()
    file2.close()

    file1= open(f1,'w')
    file1.write(data_b)
    file1.close()

    file2= open(f1,'w')
    file2.write(data_a)
    file2.close()

    print('done!!')
swappingFiles()
    
    
