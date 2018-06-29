#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("hello lyt")
a = 100
if a >= 0:
    print(a)
else :
    print(-a)
print("啦啦啦啦")
print(ord("A"))
print(chr(67))
print("\u4e2d")
print("ABC".encode("ascii"))
print("李云彤".encode("utf-8"))
print(b'\xe6\x9d\x8e\xe4\xba\x91\xe5\xbd\xa4'.decode("utf-8"))
print(len("abc"))
print("hello %s" % "lyt")
s1=72
s2=85
r=(85-72)/72
print("???%s" % r)
lalala = ["aaaa","bbbb","ccccc"]
print(lalala[-1])
lalala.append("dddd")
lalala.insert(2,"duangduang")
print(lalala)
lalala.pop()
print(lalala)
lalala[0] = "yingying"
print(lalala)
dingding = ["1111",11111,True]
print(dingding)
tuple = (1,2,3,["x","y"])
print(tuple)
tuple[3][1] = "z"
print(tuple)

# s = input("birth:")
# birth = int(s)
# if birth < 2000:
#     print("1")
# else:
#     print("2")
print(list(range(5)))
sum = 0 ;
for x in list(range(101)):
    sum = sum + x
print(sum)
a = {"jiang":666,"yu":777,"hong":888}
print(a["jiang"])
print(a.get("yu"))
print(abs(-100))
print(hex(15))
from MyAbs import myAbs
print(myAbs(-100))
from MyAbs import power
print(power(5,5))

import math
print(math.sqrt(4))


