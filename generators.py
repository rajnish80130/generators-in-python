# What is a Generator

# Python generators are a simple way of creating iterators.

# iterable
class mera_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_iterator(self)
    
# iterator
class mera_iterator:
    
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start+=1
        return current

# The Why

L = [x for x in range(100000)]

#for i in L:
    #print(i**2)
    
import sys
print(sys.getsizeof(L))

x = range(10000000)

#for i in x:
    #print(i**2)
print(sys.getsizeof(x))

# A Simple Example

def gen_demo():
    
    yield "first statement"
    yield "second statement"
    yield "third statement"

gen = gen_demo()

for i in gen:
    print(i)

# Python Tutor Demo (yield vs return)

# Example 2

def square(num):
    for i in range(1,num+1):
        yield i**2

gen = square(10)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)

# Range Function using Generator

def mera_range(start,end):
    for i in range(start,end):
        yield i

for i in mera_range(15,26):
    print(i)

# Generator Expression

# list comprehension
L = [i**2 for i in range(1,101)]
gen = (i**2 for i in range(1,101))

for i in gen:
    print(i)


# Benefits of using a Generator
# 1. Ease of Implementation

class mera_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_iterator(self)

# iterator
class mera_iterator:
    
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start+=1
        return current

def mera_range(start,end):
    
    for i in range(start,end):
        yield i

# 2. Memory Efficient

L = [x for x in range(100000)]
gen = (x for x in range(100000))

import sys

print('Size of L in memory',sys.getsizeof(L))
print('Size of gen in memory',sys.getsizeof(gen))

# 3. Representing Infinite Streams
def all_even():
    n = 0
    while True:
        yield n
        n += 2

even_num_gen = all_even()
print(next(even_num_gen))
print(next(even_num_gen))

# 4. Chaining Generators
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))