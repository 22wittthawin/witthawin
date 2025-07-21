i = 0
while i <= 100:
    print(i)
    i += 1

i = 1000
while i >= 0:
    print(i)
    i -= 1

min_num = None 
while True:
    try:
        num = float(input("กรอกจำนวนจริงบวก: "))
        if num <= 0:
            break
        if min_num is None or num < min_num:
            min_num = num
    except:
        break

if min_num is not None:
    print("จำนวนจริงบวกที่น้อยที่สุดคือ:", min_num)
else:
    print("ไม่มีข้อมูลจำนวนจริงบวก")
