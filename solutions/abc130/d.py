# Ref https://owlog.org/abc130/#toc6
import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    acc = list(accumulate(A))

    cnt = 0
    left, right = 0, 0
    while right < N:
        while acc[right] - acc[left] < K and right < N:
            right += 1

        while acc[right] - acc[left] >= K:
            cnt += N + 1 - right
            left += 1

    print(cnt)

# def main():
#     from itertools import accumulate
#     import sys
#     input = sys.stdin.readline
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
#     ans = 0
#     tmp = A[0]
#     n = 1
#     l = 1
#     for j in range(len(A)) :
#         for i in range(n, len(A)):
#             if tmp >= K :
#                 ans += len(A) - i
#             else :
#                 if l < len(A) - 1 :
#                     tmp += A[l]
#                     l += 1
#                 else :
#                     print(ans)
#                     sys.exit()
#         tmp = tmp - A[j]
#         n = i
#     print(ans)

if __name__ == '__main__':
    main()

