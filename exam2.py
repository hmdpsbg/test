T = int(input())
for _ in range(T):
    # 读取数据
    tmp = [int(i) for i in input().split()]
    n = int(tmp[0])
    m = int(tmp[1])
    a = []
    tmp = [int(i) for i in input().split()]
    for i in range(n):
        a.append(int(tmp[i]))
    
    # a排序，也可以不用排
    a.sort()
    _sum = sum(a)
    _max = _sum // m    # 计算可能的最大值
    if n < m:
        _max = a[-1] // 2


    # 可能的最大结果，降序遍历，直到满足条件为止
    while _max > 0:
        # cnt记录满足最大的用户数
        cnt = 0
        for num in a:
            if num >= _max:
                cnt += num // _max
        if cnt >= m:
            break
        else:
            _max -= 1
    print(_max)