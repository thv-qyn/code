def firstDegree(a,b):
    """
    Đây là phương trình bậc 1: ax+b=0
    :param a: hệ số a
    :param b: hệ số b
    :return: trả về 3 trường hợp kết quả
    """
    if a==0 and b==0:
        print(" phương trình vô số nghiệm")
    elif a==0 and b!=0:
        print(" phương trình vô nghiệm")
    else:
        x=-b/a
        print("no của phương trình = ",x)
print ("phương trình bậc 1")
a=float(input("nhập hệ số a:"))
b=float(input("nhập hệ số b:"))
firstDegree(a,b)


