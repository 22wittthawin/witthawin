#4.1.พิมพ์จํานวนเต็มตั้งแต่0 ถึง 100
i = 0
while i <= 100:
    print(i)
    i += 1

#4.2.พิมพ์จํานวนเต็มตั้งแต่1000 ถึง 0
i = 1000
while i >= 0:
    print(i)
    i -= 1

#4.3.รับข้อมูลเข้าจํานวนจริงบวกบรรทัดละจํานวน หยุดรับเมื่อข้อมูลเข้าไม่ใช่จํานวนจริงบวก แล้วหา
#จํานวนจริงบวกที่มีค่าน้อยที่สุดจากจํานวนจริงบวกทั้งหมดที่รับเข้ามา
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
