def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    list1 = [int(i) for i in str(num1)]
    list2 = [int(i) for i in str(num2)]

    set1 = set()
    set2 = set()

    for num in list1:
        set1.add(num)
    for num in list2:
        set2.add(num)

    if set1 == set2:
        count1 = { num : list1.count(num) for num in set1 }
        count2 = { num : list2.count(num) for num in set2 }
        if count1 == count2:
            return True
        else:
            return False
    else:
        return False