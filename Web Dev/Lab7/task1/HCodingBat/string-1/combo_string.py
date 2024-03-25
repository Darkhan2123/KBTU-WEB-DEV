def combo_string(a, b):
    min_len = min(len(a), len(b))
    max_len = max(len(a), len(b))

    if (min_len == len(a)):
        return a + b + a
    else:
        return b + a + b
