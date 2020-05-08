def finder(files, queries):

    dic = {}
    result = []
    for f in files:
        end = f.split("/")[-1]
        if end in dic:
            dic[end].append(f)
        else:
            dic[end] = [f]
    for q in queries:
        if q in dic:
            result += [fi for fi in dic[q]]


    """
    YOUR CODE HERE
    """

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
