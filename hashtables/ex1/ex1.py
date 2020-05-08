def get_indices_of_item_weights(weights, length, limit):

    indices = {}
    for x in range(len(weights)):
        if weights[x] not in indices:
            indices[weights[x]] = [x]
        else:
            indices[weights[x]] += [x]


    for w in weights:
        if limit - w in indices:
            if w == limit - w:
                return [indices[w][1], indices[w][0]]
            if w > indices[limit-w][0]:
                return [indices[limit-w][0], indices[w][0]]
            else:
                return [indices[w][0], indices[limit-w][0]]
                

    """
    YOUR CODE HERE
    """

    return None
