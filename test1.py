import change_list;

def test1():
    assert change_list.change_list([1,2,3,4,5,6,7,8,9,10]) == ([10, 8, 7, 6, 5, 5, 4, 3, 2], 9)
    assert change_list.change_list([12,32,17,5,11,2,72,9]) == ([32, 17, 11, 9, 5, 5, 2], 7)
