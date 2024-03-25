def string_match(a, b):
    min_length = min(len(a), len(b))
    cnt = 0
    for i in range(min_length - 1):
        if a[i:i+2] == b[i:i+2]:
            cnt += 1
    return cnt
