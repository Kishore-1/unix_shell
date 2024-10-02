#System Date and Time
def dte():
    a=datetime.datetime.now()
    dt=a.strftime('%d-%b-%Y'),a.strftime('%X')   #in single line
    # tt=a.strftime('%X')                        #in two line
    print("Today Date :",dt,)
    # print("Current Time :",tt)
dte()
