import random

#-----دریافت ورودی از کاربر-----
while True:
    entekhab = int(input("1_ sang \n2_ kaghaz \n3_ gheychi \n"))
    if entekhab == 0:
        break

    if (entekhab != 1) and (entekhab != 2) and (entekhab != 3):
        print("voroodi na motabar ast")
        break

#---