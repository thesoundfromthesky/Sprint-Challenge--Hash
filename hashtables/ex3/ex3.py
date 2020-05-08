def intersection(arrays):

    """
    YOUR CODE HERE
    """
    
    d = {}
    l = len(arrays)
    for i in arrays:
        for i,v in enumerate(i):
            if v in d:
                d[v].append(v)
            else:
                d[v] = [v]

    result=[]

    for i,v in d.items():
       if len(v) == l:
           result.append(i)


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
