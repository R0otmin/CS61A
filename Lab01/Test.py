def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.
    
    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    a,b = min(i,j,k),i+j+k-min(i,j,k)-max(i,j,k)
    return pow(a,2)+pow(b,2)
print(two_of_three(10,2,8))
