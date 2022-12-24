def main(S, d):
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): numnber
        
    Returns:
        float: result
    '''
    S = 78
    d = 8
    a = (S - d ** 2)/ (2 * d)
    b = a + d
    x = b - (a ** 2)/(2 * b)
    return x
