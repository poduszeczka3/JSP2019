for i in range(1,5):
    for j in range(10):
        for k in range(10):
            if i%2==0 and j%2==0 and k%2==0 and 100*i+10*j+k<=400:
                x=100*i+10*j+k
                print(str(x)+",")