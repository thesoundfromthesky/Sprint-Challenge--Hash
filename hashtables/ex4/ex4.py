def has_negatives(a):

    """
    YOUR CODE HERE
    """
    """
    find if integer has negative pair then return a list
    """
    #convert
    convert = {i:-i for i in a}
    #keep answers in result
    result=[]

    #iterate input
    for i in a:
        #if i is positive we check
        if i > 0:
            #get value of i
            negative = convert[i]
            #if negative is in convert
            if negative in convert:
                #it has negative pair and append to result
                result.append(i)

    #return result
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
