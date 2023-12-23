"""
Describing MRO, its importance, how to find the MRO, and how to fix MRO issues
"""

"""
What is Method Resolution Order? 
The order in which Python looks for a method in a hierarchy of classes

Why is it important?
Generally don't have to worry about it with linear inheritance. Method order is a straight line
from child class up to base class 

class A:
    pass

class B(A):
    pass

class C(B):
    pass
    
c = C()

C -> B -> A

[C,B,A] #method resolution order. Meaning a method will be called in the order C,B,A when looking at class C

But multiple inheritance can cause issues where the inheritance order won't allow for a 
proper order to be created. 
If a proper order isn't created, Python can't call methods properly in the inheritance hierarchy

Ok...so why do I need to worry about it?
Because you may run into multiple inheritance issues where the order in which you write your
inheritance structure matters, and by knowing MRO, you can fix inheritance ordering issues

For Method Resolution Order to succeed, we must have both monotonicity and local precendence. 
Error, can't create consistent method resolution order if either 
Monotonicity - Inheritance order of parents must be maintained
Local precendence - Local inheritance order must be maintained
"""

class A:
    pass

class B:
    pass

class C(A,B):
    pass

# class D(B,A): #causes class E(C,D) to fail MRO
class D(A,B):
    pass

class E(C,D):
    pass

print(E.mro())

"""
General form of the algorithm
L(current_class) = [current_class] + merge(L(parents),[parents])

Expand L(parents) to full linearization
The algorithm is as follows: 
1. Pick the head of the list, beginning with the first list
2. If this head DOES NOT exist in the tail of any other list, add it to the linearization [current_class] and remove it from all the other lists
    - repeat step 1
3. If this head DOES exist in the tail of any other list, pick the head of the next list and repeat the previous check
4. If we go through all the lists and can’t find a head that doesn’t exist in a tail, MRO fails


class A:
L(A) = [A] + merge(L(no_parents),[no_parents])
L(A) = [A]

class B:
L(B) = [B] + merge(L(no_parents),[no_parents])
L(B) = [B]

class C(A,B):
L(C) = [C] + merge([A], [B], [A,B])
L(C) = [C,A] + merge([B], [B])
L(C) = [C,A,B]

class D(B,A):
L(D) = [D] + merge(L(B), L(A), [B,A])
L(D) = [D] + merge([B], [A], [B,A])
L(D) = [D,B] + merge([A], [A])
L(D) = [D,B,A] #This will cause L(E) to fail later

#Let's try Linearization of class E, using the failure L(D) = [D,B,A]
class E(C,D):
L(E) = [E] + merge(L(C), L(D), [C,D])
L(E) = [E] + merge([C,A,B], [D,B,A], [C,D])
L(E) = [E,C] + merge([A,B], [D,B,A], [D])
L(E) = [E,C,D] + merge([A,B], [B,A])
L(E) = [E,C,D] + #FAIL

#Now let's retry with the correct linearization of D
class D(A,B):
L(D) = [D,A,B] #Correct Linearalization of D

class E(C,D):
L(E) = [E] + merge(L(C), L(D), [C,D])
L(E) = [E] + merge([C,A,B], [D,A,B], [C,D])
L(E) = [E,C] + merge([A,B], [D,A,B], [D])
L(E) = [E,C,D] + merge([A,B], [A,B])
L(E) = [E,C,D,A] + merge([B], [B])
L(E) = [E,C,D,A,B]
"""