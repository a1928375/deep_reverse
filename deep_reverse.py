def is_list(p):
    return isinstance(p, list)

def deep_reverse(p):
    if is_list(p):
        result = []
        for i in range(len(p) - 1, -1, -1):
            result.append(deep_reverse(p[i]))
        return result
    else:
        return p
        
p = [1, [2, 3]]
print deep_reverse(p)

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)

print p

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)

print q
