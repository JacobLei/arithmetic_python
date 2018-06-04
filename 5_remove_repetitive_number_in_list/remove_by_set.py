
# use set()

def remove_by_set(l):
    return list(set(l))

if __name__ == '__main__':
    l = [1, 2, 2, 1, 4, 3]
    print(remove_by_set(l))
