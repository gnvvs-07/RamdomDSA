n = 3
def generator(open,close,ds=None,ans=None,count=0):
    # print(open,close)
    # print("answer:",end='')
    # print(ds)
    
    # count+=1
    # print(close)
    # if count == 5:
    #     return
    if ds is None:
        ds = ""
    if ans is None:
        ans =[]
    if open>close:
        return
    if open ==0 :
        if close ==0:
            ans.append(ds)
            return 
        else:
            close_1 = close
            while close>0:
                ds+=")"
                close-=1
            # generator(open,close-1,ds,ans,count)
            ans.append(ds)
            while close_1>0:
                ds = ds[:-1]   
                close_1-=1
            return  
    
    ds+="("
    generator(open-1,close,ds,ans,count)
    ds = ds[:-1]
    
    ds+=")"
    generator(open,close-1,ds,ans,count)
    ds = ds[:-1]

    return ans
        
# print(generator(n,n))
for rows in generator(n,n):
    print(*rows)