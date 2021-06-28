def computepay(h, hrs_rate):
        if int(h) > 40:
                total_pay_forty=40 * hrs_rate
                extra_pay=(h-40)*1.5*hrs_rate
                total_pay=total_pay_forty + extra_pay
                return total_pay
        else:
                total_pay = h * hrs_rate
        return total_pay

hrs = input("Enter Hours:")
h = float(hrs)
hrs_rate = input("Enter Hourly Rate:")
hrs_rate = float(hrs_rate)
p = computepay(h, hrs_rate)
print("Pay", p)
