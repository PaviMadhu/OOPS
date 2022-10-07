class Solution:
    def findMedianSortedArrays(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.num3=self.num1+self.num2
        self.num4=list(set(sorted(self.num3)))
        if len(self.num4)%2==0:
            self.temp=len(self.num4)
            self.temp1=self.temp//2
            self.temp2=(self.num4[self.temp1-1]+self.num4[self.temp1])/2
        else:
            self.temp=len(self.num4)
            self.temp1=(self.temp-1)//2
            self.temp2=self.num4[self.temp1]
        return self.temp2
x=input()
y=x[1:-1]
x1=input()
y1=x1[1:-1]
num_1=y.split(",")
num_2=y1.split(",")

num1=[]
num2=[]
for i in num_1:
    a=int(i)
    num1.append(a)
for j in num_2:
    b=int(j)
    num2.append(b)

obj=Solution()
res=obj.findMedianSortedArrays(num1,num2)
print(res)