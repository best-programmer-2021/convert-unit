print("""welcome 

    1- kilometer to mile 
    2- mile to kilometer
    3- centimeter to meter
    4- meter to centimeter
    5- inch to centimeter
    6- centimeter to inch 
    7- meter to inch 
    8- inch to meter 

    """)
go = input("please choose operation : ")
go = int(go)
went = go
if went==1 :
    kilometer = input("how many kilometer : ")
    kilometer = int(kilometer)
    ki = 0.6213712
    ki *= kilometer
    print(ki)
elif went==2 :
    mile = input("how many mile : ")
    mile = int(mile)
    mi = 1.6093439799
    mi *= mile 
    print(mi)       
elif went==3 :
    centimeter = input("how many centimeter : ")
    centimeter = int(centimeter)
    cen = 0.01
    cen *= centimeter
    print(cen)
elif went==4 :
    meter = input("how many meter : ")
    meter = int(meter)
    met = 100
    met *= meter
    print(met)
elif went==5 :
    inch = input("how many inch : ")
    inch = int(inch)
    inc = 2.54
    inc *= inch
    print(inc)
elif went==6 :
    ce = input("how many centimeter : ")
    ce = int(ce)
    c = 0.3937007874
    c *= ce
    print(c)
elif went==7 :
    me = input("how many meter : ")
    me = int(me)
    m = 39.37007874
    m *= me
    print(m)
elif went==8 :
    ic = input("how many inch : ")
    ic = int(ic)
    i = 0.0254
    i *= ic
    print(i)
else :
    print("your choose is incorrect") 
    print("please try again")
    print("good luck")
e = input("choose one key to exit : ")                               