import pytest
from LinkedList.LinkedList import *

# Test empty linked list
def test_empty_ll():
    ll = LinkedList()
    expected = "Empty LinkedList"
    actual = str(ll)
    assert expected == actual

# Test insert 3 nodes
def test_insert(ll):
    expected = "{ 2 } -> { 5 } -> { 3 } -> NULL"
    actual = str(ll)
    assert expected == actual

# Test includes 
def test_includes(ll):
    expected = "True"
    actual = str(ll.includes(5))
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(5)
    ll.insert(2)
    ll.includes(5)
    return ll