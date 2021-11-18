def multiply(a: float, b:float):
    
    """Multiplies two float numbers

    Parameters
    ----------
    a : float
        A float number
    b : float
        A float number

    Returns
    -------
    float
        Returns the product of the two input numbers
    """
    assert isinstance(a, float), TypeError
    assert isinstance(b, float), TypeError

    return a*b
