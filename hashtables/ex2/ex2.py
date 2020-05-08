#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    dic = {}
    trip = [None] * (len(tickets))
    for t in tickets:
        if t.source == "NONE":
            trip[0] = t.destination
        dic[t.source] = t.destination

    for y in range(1, len(tickets)):
        trip[y] = dic[trip[y-1]]
        

    """
    YOUR CODE HERE
    """

    return trip
