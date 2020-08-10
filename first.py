n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

def binary(mid):
        if((mid + 1)<n and (arr[mid]!=arr[mid+1]) ):
            return  1
        elif((mid + 1)<n and arr[mid]!=arr[mid-1]):
            return 2
        elif(arr[mid]==0 and arr[n-1]==0 and arr[0]==0):
            return 3
        elif(arr[mid]==arr[n-1]):
            return -2
        else:
            return -1

lower=0
upper=n-1
while(lower<=upper):
    mid=lower + (upper-lower)//2
    a=binary(mid)
    if(a==-1):
        lower=mid+1
    elif(a==-2):
        upper=mid-1
    elif(a==1):
        print(f"Number of zeros is {n-mid-1}")
        break
    elif(a==2):
        print(f"Number of zeros is {n-mid}")
        break
    elif(a==3):
        print(f"Number of zeros is {n}")
        break
if(a<0):
 print("Not possible")



