import cv2  #access image file
import string #opening file access text
import os #read and write

d={}   #dictionary unordered collection key-value pair character to asci
c={}   #cannot access by index xor operations to convert to stegobject asci to character

for i in range(255): #iterate 255 times
    d[chr(i)]=i
    c[i]=chr(i)
    

x=cv2.imread(r"C:\Users\sahana p k\OneDrive\Pictures\gan.jpg")

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("enter key to edit(security key):")  #key
text=input("enter text to hide:") #secret msg

k1=0
t1n=len(text) #rgb length text
z=0#decides plane
n=0 #num of row
m=0 #num column

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[k1]]
    n=n+1
    m=m+1
    m=(m+1)%3

    k1=(k1+1)%len(key)

cv2.imwrite("encrypted-img.jpg",x)
os.startfile("encrypted-img.jpg")
print("data hiding completed successfully.")

k1=0
t1n=len(text) #rgb length text
z=0#decides plane
n=0 #num of row
m=0 #num column

ch=int(input("\nenter 1 to extract data from image:"))

if ch==1:
    key1=input("\nRe enter key to extract text:")
    decrypt=""
    
    if key == key1:
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[k1]]]
            n=n+1
            m=m+1
            m=(m+1)%3
            k1=(k1+1)%len(key)
        print("encrypted text was:",decrypt)
    else:
           print("key not found")
else:
     print("Thank you. exiting.")
