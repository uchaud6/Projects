# Project Description located @ https://www.dumas.io/teaching/2021/fall/mcs260/nbview/projects/project3.html

# MCS 260 Fall 2021 Project 3
# Umar Chaudhry
# I completed this project completely with my own work and followed the project description to the best of my ability. 
" Create functions that help analyze orbits/cycles "

def orbit(f,x0,n):
    """
    Compute the first `n` terms of the orbit of `x0` under
    the function `f`.
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument
        `n` - the number of points to compute (a positive integer)
    Returns:
        A list of length `n` containing the values [ x0, f(x0), f(f(x0)), f(f(f(x0))), ... ]
    """
    values = [x0]
    for i in range(n-1):
        values.append(f(x0))
        # update 'x0' so the function can be applied repeatedly 'n' amount of times
        x0 = f(x0)
    return values

def orbit_data(f,x0):
    """
    Repeatedly apply function `f` to initial value `x0` until some
    value is seen twice.  Return dictionary of data about the observed
    behavior.

    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        Dictionary with the following keys (after each key is a description of
        the associated value):
           "initial": The part of the orbit up to, but not including, the first
                value that is ever repeated.
           "cycle": The part of the orbit between the first and second instances of
                the first value that appears twice, including the first but not the
                second.  In other words, the entire orbit consits of the "initial"
                part followed by the "cycle" repeating over and over again.

    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...

    Then the return value would be:
    {
        "initial":[11, 31, 12, 5, 6, 2],
        "cycle": [8,19,17]
    }
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """

    results = {}
    # 'sequence' will be used to track output of 'f(x0)' called repeatedly on itself and
    # determine the data under the "initial" and "cycle" keys of 'results'
    sequence = [x0]
    # 'seen' will be a boolean to test if a value in the output has been repeated
    seen = False
    # indice counter will be used to determine the indice in 'sequence' where
    # a value has been repeated and use that information to find the 'initial' and 'cycle' keys
    indice_counter = 0
    while True:
        # increment the indice at the start as 'sequence' already has one element
        indice_counter += 1
        # if a value has been repeated, the 'initial' and 'cycle' keys can be assigned to 'results'
        if seen == True:
            # assign all the values from the beginning of 'sequence' up until the indice where a cycle occurs
            results["initial"] = sequence[:-(len(sequence[sequence.index(seen_value):(indice_counter+1)]))]
            # assign all the values from where the first instance of the repeated value was mentioned up until when it was repeated 
            results["cycle"] = sequence[sequence.index(seen_value):indice_counter]
            break
        
        if f(x0) not in sequence:
            sequence.append(f(x0))
        else:
            # still add repeated element to the list but make note of its indice by decreasing 'indice_counter' 
            # in order to have the correct indice of the repeated value in the next iteration of the while loop
            sequence.append(f(x0))
            # assign the repeated value of 'f(x0)' to 'seen_value' to use sequence.index() method in the next iteration
            seen_value = f(x0)
            # boolean triggers the condition of a repeated value
            seen = True
            indice_counter -= 1
        # update 'x0' so the function can be applied repeatedly 'n' amount of times
        x0 = f(x0)
    return results

def eventual_period(f,x0):
    """
    Determine the length of the periodic cycle that `x0` ends up in.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        The length of the periodic cycle that the orbit of `x0` ends up in.

    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    
    Then the return value of eventual_period(f,11) would be 3, since the periodic
    cycle contains the 3 values 8,19,17.
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """
    data = orbit_data(f,x0)
    return len(data["cycle"])

def steps_to_enter_cycle(f,x0):
    """
    Determine the length of the intial part of the orbit of `x0` under `f` before
    it enters a periodic cycle.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        The number of elements of the orbit of `f` before the first value that 
        repeats.
        
    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    
    Then the return value of steps_to_enter_cycle(f,11) would be 6, because there are 6
    values in the intial segment of the orbit (i.e. 11, 31, 12, 5, 6, 2) which are followed by
    a periodic cycle.
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """
    data = orbit_data(f,x0)
    return len(data["initial"])

def eventual_cycle(f,x0):
    """
    Return the periodic cycle that the orbit of x0 ends up in as a list.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `x0` - a value of the type that `f` accepts as its argument

    Returns:
        The earliest segment from the orbit of `x0` under `f` that repeats
        indefinitely thereafter, as a list.
        
    Example: Suppose that applying f repeatedly to start value 11 gives this sequence:
    11, 31, 12, 5, 6, 2, 8, 19, 17, 8, 19, 17, 8, 19, 17, 8, ...
    
    Then eventual_cycle(f,x0) would return [8, 19, 17].
    
    (If the orbit of `x0` doesn't end up in a cycle, it's ok for this function to run forever
    trying to find one.)
    """
    data = orbit_data(f,x0)
    return data["cycle"]

def smallest_first(L):
    """
    Rotates a list so that its smallest element appears first.
    
    Arguments:
       `L`: A list of integers, no two of them equal
       
    Returns:
       A list that is the result of moving the first element of `L` to the end,
       repeatedly, until the first element of `L` is the smallest element of the list.
       
    Example: smallest_first([46,41,28]) returns [28,46,41]
    Example: smallest_first([4,2,1]) returns [1,4,2]
    Example: smallest_first([9,8,7,6,5,4,3,2,1]) returns [1,9,8,7,6,5,4,3,2]
    """
    while True:
        if L[0] != min(L):
            L.append(L[0])
            L.remove(L[0])
        elif L[0] == min(L):
            break
    return L

def find_cycles(f,start_vals):
    """
    Find all the periodic cycles of the function `f` that appear when you consider
    orbits of the elements of `start_vals`.
    
    Arguments:
        `f` - a function (should take one integer argument and return an integer)
        `start_vals` - a list of integers to use as starting values

    Returns:
        A list of lists, consisting of all the periodic cycles that are seen
        in the orbits of the start values from `start_vals`.  Each cycle is 
        given with its smallest entry appearing first, and any given cycle
        appears only once in the list.
       
    e.g. If `mwdp` is the mean with digit power function, then find_cycles(mwdp,[65,66,67])
    would return [ [28,46,41], [38,51] ] because both 65 and 67 end up in the [28,46,41]
    cycle and 66 ends up in the [38,51] cycle.
    """
    periodic_cycles = []
    for value in start_vals:
        data = orbit_data(f,value)
        # use smallest_first() so a repeated cycle is not confused to be new and added to 'periodic cycles'
        data = smallest_first(data["cycle"])
        if data not in periodic_cycles:
            periodic_cycles.append(data)
    return periodic_cycles


