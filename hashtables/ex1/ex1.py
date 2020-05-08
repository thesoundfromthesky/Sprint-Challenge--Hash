def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    """
    UPER
    Find sum of two weights that meets limit.
    Convert list of weights to dict, the key to be value of list, the value to be index of list.
    Iterate dict and start from the heaviest weight.
    Check if key of the heaviest weight - limit exists in dict.
    Return when condition is met.
    Return format should be (index of the higher, index of the smaller).
    """
    weights_dict = {f"{v}-{i}":i for i,v in enumerate(weights)}

    for cur_weight in weights:
        print(cur_weight)
        if limit - cur_weight < 0:
            continue   
        limit_left = limit - cur_weight     
        if limit_left in weights_dict:            
            limit_left_index = weights_dict[limit_left]
            if limit_left_index == weights_dict[cur_weight]:
                continue
            if weights_dict[cur_weight] > limit_left_index: 
                return [weights_dict[cur_weight], limit_left_index]
            else:
                return [limit_left_index, weights_dict[cur_weight]]

    return None

weights = [4, 4]

get_indices_of_item_weights(weights, 2, 8)