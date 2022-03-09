def top_n(items, n):
    """
    Return the top n items in an array in desc order.
    
    Args:
        items (array): list or array-like object
        n (int): num of items to return
    
    Return:
        array: top n items in desc order
    
    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    for i in range(n):  # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # if this item value is greater than the next..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two
    
    # get last n items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]

# print(top_n([-16, -3, 7, 2, 5, 0, 6, 12, 2, 8], 3))
