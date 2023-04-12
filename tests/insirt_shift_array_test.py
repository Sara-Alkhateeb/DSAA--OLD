
# import the newArr function from the ArrayInsertShift module
from cc2.ArrayInsertShift import newArr 

# define a test function that tests the newArr function with specific inputs
def test_newArr():
        # define an input array and value
        arr = [1, 2, 3, 4, 5]
        val = 10
        # call the newArr function with the inputs and store the result in a variable
        actual=newArr(arr, val)
        # define the expected output
        expected = [1, 2, 10, 3, 4]
        # check if the actual result matches the expected result and raise an AssertionError if not
        assert actual == expected

# define additional test functions for different input arrays and values
def test_newArr_1():
        arr = [1, 2, 3, 4]
        val = 0
        actual=newArr(arr, val)
        expected= [1, 2, 0, 3]
        assert actual == expected

def test_newArr_2():
        arr = []
        val = 5
        actual=newArr(arr, val)
        expected = [5]
        assert actual == expected

def test_newArr_3():
        arr = [""]
        val = 1
        actual=newArr(arr, val)
        expected = [1]
        assert actual == expected


