def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
	product = 1
	count = 0
	while k != 0 and count < k:
        product *= n
        n -= 1
        count += 1
    return product


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    a = 0
    collect = []

    while y > 0:

        a = y % 10
        
        y = y//10

        collect.append(a)
    
    return sum(collect)


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"


# method 1: string

    return "88" in str(n)

# method 2: number

    flag = 0
    d = 0

    while n > 0:

        n, d = n // 10, n % 10

        if d == 8 and flag == 1:
            return True

        elif d == 8:
            flag = 1

        else:
            flag = 0

    return False
