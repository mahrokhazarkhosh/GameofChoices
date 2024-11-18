import random

#-----دریافت ورودی از کاربر-----
while True:
    entekhab = int(input("1_ sang \n2_ kaghaz \n3_ gheychi \n"))
    if entekhab == 0:
        break

    if (entekhab != 1) and (entekhab != 2) and (entekhab != 3):
        print("voroodi na motabar ast")
        break

#--------اضافه کردن انتخاب تصادفی سیستم------

entekhabesystem = random.randint(1, 3)
entekhabesystemstring = ""
if entekhabesystem == 1:
    entekhabesystemstring = "sang"
elif entekhabesystem == 2:
    entekhabesystemstring = "kaghaz"
elif entekhabesystem == 3:
    entekhabesystemstring = "gheychi"
print("entekhabe system : "+entekhabesystemstring)

#-------تعیین منطق برنده------

if (entekhabesystem == 1 and entekhab == 2)\
or (entekhabesystem == 2 and entekhab == 3)\
or (entekhabesystem == 3 and entekhab == 1):
    print("shoma barande shodid")
elif entekhabesystem == entekhab:
    print("mosavi shodid")
else:
    print("shoma bakhtid")

print("\n\n")