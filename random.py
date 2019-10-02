global n    #n -> Q+
global n_m  #=n, but but modifiable
loop = "true"

while loop=="true":
    n = random.randint(10**149, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    tmp_a = n%2
    if tmp_a==1:
        loop = "false"

n_m = n

return n
return n_m    
