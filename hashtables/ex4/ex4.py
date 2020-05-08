def has_negatives(a):

    ans = []
    dic = {}
    for num in a:
        dic[num] = None
    for num in a:
        if num > 0:
            if num * -1 in dic:
                ans.append(num)


    """
    YOUR CODE HERE
    """
    
    return ans


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
