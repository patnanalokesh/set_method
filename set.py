# a={}
# print(a,type(a))  #  {} <class 'dict'>

# b={3,5.7,"lokesh",(11,"hi")}
# print(b,type(b))  #  <class 'set'>

# d={10,45,37}
# print(d[2])  #  TypeError: 'set' object is not subscriptable.

# a={1,2,5,4}
# b='hello',1,2,5,4
# a.add(b)
# print(a)  #  {1, 2, 4, 5, ('hello', 1, 2, 5, 4)}

# f={4,5,8}
# f.clear()
# print(f)   #  set()

# a={1,2,3,4} ; b={1,2,4,5,6}; c={4,3,5,6,7,8}; d={1,3,5,6,8,9}
# print(a.intersection(b))
# print(a.intersection(c))
# print(a.intersection(d))
# print(b.intersection(d))  #  The intersection of two sets as a new set.{bcoz   all elements that are in both sets.}

# g={1,2,3,'hi'}
# h={3,4,5,'hello'}
# print(g.union(h))  #   The union of sets as a new set.(bcoz all elements that are in either set.)
# print(h.union(g))

# a={1,2,3}
# b={3,4,5}
# c={3,4,7}
# a.update(b)  # {1, 2, 3, 4, 5}
# a.update(c)  # {1, 2, 3, 4, 5, 7}
# print(a)    #  Update a set with the union of itself and others.

# a={5,10,20,30,40,50}
# b={10,25,30}
# print(a.difference(b))
# print(b.difference(a))
# print(a-b)
# print(b-a)

# g={55,56,45,21,87}
# g.discard(44)
# print(g)
# g.discard(56)
# print(g)

# f={54,84,31,4,57}
# f.pop()
# print(f)

# A={1,3,4,5,6,7}
# B={3,4,5}
# C={6,7,8}
# print(A.isdisjoint(B))
# print(A.isdisjoint(C))
# print(C.isdisjoint(B))

# f={1,2,3}
# g={1,2,3,4,5,6}
# h={1,2,4,5}
# print(f.issubset(g))
# print(f.issubset(h))
# print(g.issubset(f))
# print(h.issubset(g))

# a={8,9,10,12,14}
# # a.remove(140)
# print(10)
# print(a)   #KeyError: 140

# a={8,9,10,12,14}
# # b={10,14,15,1}
# b={8,9,10}
# print(a.issuperset(b))
# print(b.issuperset(a)) 
# print(dir(set()))
# print(len('add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'))