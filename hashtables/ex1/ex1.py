def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    """
    Return indices of sum of two weights to meet limit
    """

    #convert weights to dict to assign to w_d
    w_d = {}
    #i is index of weight v is value of weight
    for i,v in enumerate(weights):
        #if value is in w_d
        if v in w_d:
            #append index of weight to w_d with key value of weight
            w_d[v].append(i)
        else:
            #initialize w_d at key value of weight with value index of weight
            w_d[v]=[i]
    
    #iterate weights
    for i in weights:
        #l is limit - i which is weight left reach limit
        l = limit - i
        # continue if l is not positive
        if l < 0:
            continue
        #if l exists in w_d process
        if l in w_d:
            a,b = None, None       
            #if l is itself     
            if l == i:
                a = w_d[i].pop()
                b = w_d[i].pop() 
            else:
                a = w_d[l].pop()
                b = w_d[i].pop()
            #greater index comes first
            if a > b:
                return (a, b)
            else:
                return (b, a)    

    return None

weights = [4, 4]

print(get_indices_of_item_weights(weights, 2, 8))