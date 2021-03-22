def computepay(h,r):
    overRate = r * 1.5
    if h > 40:
        p = h * overRate
    elif h <= 40:
        p = h * r
    return p

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

pay = computepay(hours,rate)
pay = str(pay)

print('Pay: ' + pay)
