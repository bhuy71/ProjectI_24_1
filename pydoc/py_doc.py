def add_numbers(a, b):
    """
    This function adds two numbers together.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    
    Example:
        >>> add_numbers(3, 5)
        8
    """
    return a + b


def subtract_numbers(a, b):
    """
    This function subtracts b from a.

    Args:
        a (int or float): The number to be subtracted from.
        b (int or float): The number to subtract.

    Returns:
        int or float: The result of a - b.

    Example:
        >>> subtract_numbers(10, 4)
        6
    """
    return a - b


def multiply_numbers(a, b):
    """
    This function multiplies two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.

    Example:
        >>> multiply_numbers(3, 4)
        12
    """
    return a * b


def divide_numbers(a, b):
    """
    This function divides a by b.

    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        float: The result of a / b. If b is 0, returns 'Cannot divide by 0'.

    Example:
        >>> divide_numbers(10, 2)
        5.0
    """
    if b == 0:
        return "Cannot divide by 0"
    return a / b


def factorial(n):
    """
    This function calculates the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Example:
        >>> factorial(5)
        120
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(n):
    """
    This function checks if a number is prime.

    Args:
        n (int): An integer.

    Returns:
        bool: True if n is a prime number, False otherwise.

    Example:
        >>> is_prime(5)
        True
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    """
    This function calculates the nth Fibonacci number.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The Fibonacci number at position n.

    Example:
        >>> fibonacci(6)
        8
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def power(base, exponent):
    """
    This function calculates the power of a number.

    Args:
        base (int or float): The base number.
        exponent (int): The exponent.

    Returns:
        int or float: The result of base raised to the power of exponent.

    Example:
        >>> power(2, 3)
        8
    """
    return base ** exponent


def is_palindrome(s):
    """
    This function checks if a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Example:
        >>> is_palindrome('madam')
        True
    """
    return s == s[::-1]


def find_max(a, b, c):
    """
    This function finds the maximum value among three numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.
        c (int or float): The third number.

    Returns:
        int or float: The largest number among a, b, and c.

    Example:
        >>> find_max(1, 4, 3)
        4
    """
    return max(a, b, c)
