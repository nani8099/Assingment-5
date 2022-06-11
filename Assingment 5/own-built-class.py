# Write a Python class to implement pow(x, n)

# Explanation:

# Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)

# You must implement it using Class

# Sample Input:

# x: 10

# n: 2

# Sample Output:

# 100


class py_pow:
   def powr(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.powr(x,-n)
        val = self.powr(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

x=int(input("Enter x value :"))
n=int(input("Enter n value :"))
print("pow(x,n) value is :",py_pow().powr(x,n));



# OUTPUT:

# Enter x value : 10
# Enter n value : 2
# pow(x,n) value is : 100










