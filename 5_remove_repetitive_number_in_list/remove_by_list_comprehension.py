
def remove_by_list_comprehension(l):
    x = []
    [x.append(i) for i in sorted(l) if not i in x] 
    return x

if __name__ == '__main__':
    l = [1, 1, 2, 2, 3, 4]
    print(remove_by_list_comprehension(l))
