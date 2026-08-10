#گرفتن اسم و چاپ

# print("nam ra vared konid:")
# name=input()
# print(f'slm {name} aziz')


#محاسبه سال تولد

# sen=int(input("sen ra vared konid:"))
# sal=1405-sen
# print(f'sal tavalod: {sal} ')


#تبدیل دما

# far=int(input("dama Fahrenheit: "))
# tem=(far-32)/1.8
# print(f'tabdil dama az Fahrenheit be Celsius : {tem} ')


# محاسبه مساحت و محیط مستطیل
# tol=int(input("tol mostatil ra vared konid:"))
# arz=int(input("arz mostatil ra vared konid:"))
# mas=tol*arz
# moh=(tol+arz)*2
# print(f'masahat {mas} va mohit {moh}')

#محاسبه bmi

# vazn=float(input("vazn ra be kg vard konid:"))
# gad=int(input("gad ra be cm vard konid:"))
# gad=gad/100
# bmi=vazn/(gad**2)

# match bmi:
#     case _ if bmi < 18.5:
#         print("kam vazn")
#     case _ if 18.5 <= bmi < 25:
#         print("normal")
#     case _ if 25 <= bmi < 30:
#         print("ezafe vazn")
#     case _:
#         print("chagh")
        
# print(f'bmi shma {bmi} hast')


#میانگین سه عدد را چاپ کن

# add1=int(input("add avl ra vared konid:"))
# add2=int(input("add dovom ra vared konid:"))
# add3=int(input("add sevom ra vared konid:"))

# min=(add1+add2+add3)/3
# print(f'min {min} hast')

#حقوق پایه رو بگیر، ۱۰٪ مالیات کم کن و خالص رو چاپ کن

# hogh=int(input("enter hoghogh:"))
# hog_khales=hogh*0.9

# print(f'hoghogh khales shoma {hog_khales} hast')


#قیمت کالا و درصد تخفیف رو بگیر و قیمت نهایی رو چاپ کن

# gh_kala=int(input("enter gh kala:"))
# takhfif=int(input("enter dar sad takhfif:"))
# gh_payani=(100/takhfif-1)*gh_kala

# # print(f'gh payani shoma {gh_payani} hast')

#تعداد ثانیه رو بگیر و به ساعت دقیقه ثانیه تبدیل کن.

# sanie=int(input("enter sanie:"))
# saat=sanie/3600
# dagige=sanie/60

# print(f'saat:{saat},dagige:{dagige},sanie:{sanie} hast')


#اطلاعات کاربر (اسم، سن، رشته، دانشگاه، شهر) رو بگیر و یه خلاصه مرتب چاپ کن.

name=(input("enter name:"))
sen=(input("enter sen:"))
reshte=(input("enter reshte:"))
daneshghah=(input("enter daneshghah:"))
shahr=(input("enter shahr:"))

print(f'asm shoma {name} , sen {sen}, reshte {reshte}, daneshghah {daneshghah},shahr {shahr}')