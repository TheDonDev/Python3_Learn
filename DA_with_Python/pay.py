try:
    inp=input('Enter Hours:')
    hours=int(inp)
except:
    print('Error,Enter Numeric Value')
try:
    inp=input('Enter Rates:')
    rate=int(inp)
except:
    print('Error,Enter Numeric Value')
def computepay(hours,rate):
    if hours>=45:
        pay=(hours + 2.5)*(rate)
        print('Pay:', pay)
    else:
        pay=hours*rate
        print('Pay:', pay)
computepay(hours,rate)
        