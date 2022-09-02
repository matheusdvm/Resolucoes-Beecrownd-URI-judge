# -*- coding: utf-8 -*-
a, b, c = (int(x) for x in input().split())
if 1<=a<=100 and 1<=b<=100 and 1<=c<=100:
    if c<a<b or b<a<c:
        print(a)
    elif c<b<a or a<b<c:
        print(b)
    elif a<c<b or b<c<a:
        print(c)
