def intersection(arrays):

    """
    YOUR CODE HERE
    """
    shortest = None
    idx = None
    convert=[]
    for i,v in enumerate(arrays):
        if shortest is None:
            shortest = len(v)
            idx = i
        else:
            if len(v) < shortest:
                shortest = len(v)
                idx = i
        convert.append({v:k for k,v in enumerate(v)})

   
    print(convert)
    





    return result

intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ])
# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000,2000000)) + [1,2,3])
#     arrays.append(list(range(2000000,3000000)) + [1,2,3])
#     arrays.append(list(range(3000000,4000000)) + [1,2,3])

#     print(intersection(arrays))
