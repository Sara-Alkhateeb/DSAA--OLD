from cc2.ArrayInsertShift import newArr 

def test_newArr():
        arr = [1, 2, 3, 4, 5]
        val = 10
        actual=newArr(arr, val)
        expected = [1, 2, 10, 3, 4]
        assert actual == expected

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

