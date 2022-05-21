# Compute the future value of a given present value, annual rate, and number of years.

principle = raw_input("Enter the principle amount (in $): ")
p = float(principle)

rate = raw_input("Enter the annual interest rate (eg. for 5% enter 0.05): ")
r = float(rate)

years = raw_input("Enter the years: ")
y = float(years)

FV = p*(1+r)**y
print "The Future Value is" + " $" + str(FV)
