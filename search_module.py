# search_module.py

def Sequential_Search(dlist, item):
    """
    Hàm tìm kiếm tuyến tính
    :param dlist: Danh sách cần tìm kiếm
    :param item: Phần tử cần tìm
    :return: Vị trí của phần tử nếu tìm thấy, -1 nếu không tìm thấy
    """
    for index in range(len(dlist)):
        if dlist[index] == item:
            return index
    return -1
