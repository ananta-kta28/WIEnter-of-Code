# Write a program to rotate elements of an array to the left by given number
def rotate(L, d, n):
	k = L.index(d)
	new_lis = []
	new_lis = L[k+1:]+L[0:k+1]
	return new_lis


if __name__ == '__main__':
    
    arr = []
    n = int(input("Enter number of elements : "))
    d=int(input("enter step: "))
    
    for i in range(0, n):
        ele = int(input("enter element"))
        arr.append(ele)

    N=len(arr)

    arr = rotate(arr, d, N)
    for i in arr:
        print(i, end=" ")
