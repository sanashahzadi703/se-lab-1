try:
    a=float(input("Enter a:"))
    b=float(input("Enter b:"))
    c=float(input("Enter c:"))
    d=float(input("Enter d:"))

    det=a*d-b*c
    if det==0:
        print("The matrix is singular,its inverse does not exist")
    else:
        inverse=[[d/det,-b/det,a/det]]
        print("the inverse of the matrix is:")
        for row in inverse:
            print(row)
except:
    print("an ERROR OCCURED")



