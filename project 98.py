def sawpfileData():
    filename1=input("Enter name")
    file1=open(filename1,"r")
    data_a=file1.read()
    filename2=input("enter second name")
    file2=open(filename2,"r")
    data_b=file2.read()
    with open(filename1,"w") as a:
        a.write(data_b)
    with open(filename2,"w")as b:
        b.write(data_a)
    




sawpfileData()