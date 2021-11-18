import unittest

def add(numA: int, numB: int) -> int: 
    
    assert isinstance(numA, int), TypeError
    assert isinstance(numB, int), TypeError
    
    result = numA + numB
    return result

class testing(unittest.TestCase): 
    def test_add(self):
        
        result = add(1,2)
        assert result == 3
        
        self.assertRaises(TypeError, add, ('a', 2))
        

if __name__ == '__main__':
    unittest.main()