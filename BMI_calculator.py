# BMI calculator
kilo = input("請輸入你的體重(kg)：")
height = input("請輸入你的身高(cm)：")

kilo = float(kilo)
height = float(height)

bmi = kilo/((height/100)**2)

print("你的BMI值是： %5.2f " % bmi)

if bmi < 18:
	print("屬於過輕體質！")
elif bmi >= 18 and bmi < 23:
	print("體重值正常！")
else:
	print("體重過重，請減肥！")