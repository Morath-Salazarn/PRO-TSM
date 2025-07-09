def vieleParameter(eins, *derRest):
    print("1 ter Parameter",eins)
    i=2
    for param in derRest:
        print(i,"ter Parameter",param)
        i=i+1
vieleParameter("Test","zwei",3,4,5,6)
vieleParameter("Test","zwei",3,4,5,"sechs","sieben")