N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for i in range(M)]
#print(N,M)
#print(A)
#print(BC)
#print("---")
A = sorted(A)
BC = sorted(BC, key = lambda x: -x[1])
D = []
for bc in BC :
    for i in range(bc[0]) :
        if len(D) < N :
            D.append(bc[1])
        else :
            break
    else :
        continue
    break
    
if N > len(D) :
    S = len(D)
else :
    S = N
for i in range(S) :
    if A[i] < D[i] :
        A[i] = D[i]
    else :
        break
print(sum(A))

#times = [bc[0] for bc in BC]
#values = [bc[1] for bc in BC]
#values, times = zip(*sorted(zip(values, times),reverse=True))
#print(values)
#print(times)
#values.sort(reverse=True)

# for i, v in enumerate(values) :
#     tmp = [n for n,i in enumerate(A) if i > v]
#     if len(tmp) == N :
#         break
#     elif len(tmp) == 0 :
#         ind = N + 1
#     else :
#         ind = tmp[0]
#
#     if times[i] < ind :
#         A[0:times[i]] = [v] * times[i]
#     else :
#         A[0:ind] = [v] * ind
#     #print(A)
#     A = sorted(A)
# print(sum(A))

#for i, v in enumerate(values) :
#    for t in range(times[i]) :
#        min_A = min(A)
#        if v > min_A :
#            A[A.index(min(A))] = v
#            print(A)
#        else :
#            break
#    else:
#        continue
#    break
#print(sum(A))

