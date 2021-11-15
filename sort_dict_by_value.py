x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

by_key = {k: v for k, v in sorted(x.items(), key=lambda item: item[0], reverse=True)}
by_value = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}

print("dict sorted key", by_key)
print("dict sorted by value", by_value)

# for k in x:
#     print(k, ': ', x[k])

# for item in x.items():
#     print(item)