#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    """
    Make list of destination and return
    """
    route=[]
    
    #Convert tickets to dict
    trip ={t.source:t.destination for t in tickets}
    
    #find departure point
    cur = trip["NONE"]
    #append to route
    route.append(cur)
    #loop until cur find "NONE"
    while cur != "NONE":
        #find next trip
        cur = trip[cur]
        #append to route 
        route.append(cur)
    
    #return route
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result)