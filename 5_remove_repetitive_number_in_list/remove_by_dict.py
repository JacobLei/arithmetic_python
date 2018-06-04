
def remove_by_dict(l):
    return list({}.fromkeys(l).keys())

if __name__ == '__main__':
    l = [1, 2, 2, 3, 2, 3, 4]
    print(remove_by_dict(l))
