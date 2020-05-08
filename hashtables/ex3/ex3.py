def intersection(arrays):

    arrays = sorted(arrays, key=lambda x: len(x))
    ans = []
    dic = {}
    for a in arrays[0]:
        dic[a] = 1
    for ar in arrays[1:]:
        for a in ar:
            if a in dic:
                dic[a] += 1
    ans = [n for n in dic if dic[n] == len(arrays)]


    """
    YOUR CODE HERE
    """
    
    return ans


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
