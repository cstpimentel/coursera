def computepay(h,r):
	if h <= base :
		pay = h * r
	elif h > base :
		OT = h - base
		OTpay = OT * r * 1.5
		pay = OTpay + base * r
	return pay


hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Enter rate per hour:")
r = float(rph)
base = 40

p = computepay(h,r)
print p
