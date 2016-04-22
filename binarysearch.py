import xml.etree.ElementTree as X 

def part(arr,low,high):
    p, i = arr[high], low
    for j in range(low,high):
        if arr[j]<=p:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def qsort(arr,low,high):
    if low<high:
        p=part(arr,low,high)
	qsort(arr,low,p-1)
	qsort(arr,p+1,high)

def binary(arr, item):
    first = 0
    last = len(arr)-1
    flag=0
	
    while first<=last and flag==0:
         midpoint = (first + last)//2
 	 
         if arr[midpoint] == item:
            print 'element found at index',midpoint
	    flag=1
         else:
            if item < arr[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    
    if flag==0:
      print 'not found'


while True:
	ch = int(raw_input("Enter 1. integer 2.Character 3.Exit :"))
	if ch==2:
	    r = X.parse('samplechar.xml').getroot()
	    arr = r.text.split()
	    qsort(arr,0,len(arr)-1)
	
	    for i in arr:
	       print i

	    item=raw_input("Enter the item to be searched :")

	    binary(arr,item)
    
	elif ch==1:    
    
	    r = X.parse('sampleint.xml').getroot()
	    arr =map(int, r.text.split())
	    qsort(arr,0,len(arr)-1)

	    for i in arr:
	       print i

	    item=int(raw_input("Enter the item to be searched :"))

	    binary(arr,item)
	elif ch==3:
	    break
	else:
            print "Invalid Choice"
	



