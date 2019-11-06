import pandas as pd
import numpy as np
df=pd.read_csv("homework4.txt", sep=";", header=0)
a=df.groupby(["Company","Payment","Order"])["Quantity"].sum()

b=a.xs('Cash',level="Payment")
c=a.xs('Credit',level="Payment")


coffeearray = np.asarray(df.Company)
for x in b:
    print("From", coffeearray[0] , (x), " people have bought", "order" , "on discount.") #ı could not change order.
for x in c:
    print(coffeearray[0]  ,(x), "assistant have bought" , "order" , "credit")
    
coffeearray = np.asarray(df.Company)
for x in b:
    print("From", coffeearray[1] , (x), " people have bought", "order" , "on discount.") #ı could not change order.
for x in c:
    print(coffeearray[1]  ,(x), "assistant have bought" , "order" , "credit")
    
coffeearray = np.asarray(df.Company)
for x in b:
    print("From", coffeearray[2] , (x), " people have bought", "order" , "on discount.") #ı could not change order.
for x in c:
    print(coffeearray[2]  ,(x), "assistant have bought" , "order" , "credit")
    
coffeearray = np.asarray(df.Company)
for x in b:
    print("From", coffeearray[3] , (x), " people have bought", "order" , "on discount.") #ı could not change order.
for x in c:
    print(coffeearray[3]  ,(x), "assistant have bought" , "order" , "credit")
    

    

    
