import random
def andGate():
    # Or gate Learning
    
    # in and gate you can increase decimal points as much as you want
    weight1=round(random.uniform(-0.5,0.5), 1)    # to round the out to 1 decimal point 
    weight2=round(random.uniform(-0.5,0.5), 1)  # to round the out to 1 decimal point
    print("Weighted intialization",weight1,weight2)
    weighto=round(random.uniform(-0.5,0.5), 1)    # to round the out to 1 decimal point 
    xo=-1
    alpha=0.1
    flage=True     # flage will be false when convergence reaches
    output=1
    andGate=((0,0,0),(0,1,0),(1,0,0),(1,1,1))
    while(flage==True):
        flage=False
        for examp in andGate:
            value=(examp[0]*weight1)+(examp[1]*weight2)
            thetha=weighto*xo
            if(value+thetha>=0):      #if perceptoron excited
                output=1    
            else:
                output=0
            if((output-examp[2])!=0):
                weight1=round(weight1+(alpha*(examp[2]-output)*examp[0]),1)   # to round the out to 1 decimal point
                weight2=round(weight2+(alpha*(examp[2]-output)*examp[1]),1)   # to round the out to 1 decimal point
                weighto=round(weighto+(alpha*(examp[2]-output)*xo),1)   # to round the out to 1 decimal point
                flage=True
    return (weight1,weight2,weighto)

weight1,weight2,weighto=andGate()
print(weight1,weight2,weighto)