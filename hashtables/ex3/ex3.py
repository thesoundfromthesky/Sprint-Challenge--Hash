def intersection(arrays):

    """
    YOUR CODE HERE
    """
    
    arrays.sort(key=lambda i:len(i))

    d = {}
    l = len(arrays)
    for idx, i in enumerate(arrays):
        for i in i:
            if i in d:
                d[i].append(i)
            elif idx == 0:
                d[i] = [i]

    result=[]

    for i,v in d.items():
       if len(v) == l:
           result.append(i)


    return result

# intersection([
#             [1,2,3],
#             [1,4,5],
#             [1,6,7]
#         ])
        # arrays = [
        #     list(range(1000000, 2000000)) + [1,2,3],
        #     list(range(2000000, 3000000)) + [1,2,3],
        #     list(range(3000000, 4000000)) + [1,2,3],
        #     list(range(4000000, 5000000)) + [1,2,3],
        #     list(range(5000000, 6000000)) + [1,2,3],
        #     list(range(6000000, 7000000)) + [1,2,3],
        #     list(range(7000000, 8000000)) + [1,2,3],
        #     list(range(8000000, 9000000)) + [1,2,3],
        #     list(range(9000000, 10000000)) + [1,2,3],
        #     list(range(10000000, 11000000)) + [1,2,3]
        # ]
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
