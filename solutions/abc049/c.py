# -*- coding: utf-8 -*-
S = str(input())
S = S.replace('eraser','').replace('erase','').replace('dreamer','').replace("dream","")
if S:
    print("NO")
else:
    print("YES")
