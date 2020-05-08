def finder(files, queries):

    """
    YOUR CODE HERE
    """
    """
    Query files then return all the matching path
    """
    #Convert files to dict and assign to query_file
    query_file={}
    #iterate files
    for i in files:
        #find file name
        k = i.split("/")[-1]
        #if file name is already  query_file
        if k in query_file:
            #append path to query_file
            query_file[k].append(i)
        else:
            #initialize query_file with key k and value [i]
            query_file[k]=[i]

    #assign path to result
    result=[]
    #iterate queires
    for i in queries:
        #if query exists in query_file
        if i in query_file:
            #extend to result
            result.extend(query_file[i])

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
