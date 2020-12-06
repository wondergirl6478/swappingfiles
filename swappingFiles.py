def SwappingFiles():
    fileA = input("Enter the path of the first file you want to swap :")
    fileB = input("Enter the second file name:")
    with open(fileA,'r') as a:
        data_a = a.read()
    with open(fileB, 'r') as b:
        data_b = b.read()
    with open(fileA, 'w') as a:
        a.write(data_b)
    with open(fileB, 'w') as b:
        b.write(data_a)
SwappingFiles()