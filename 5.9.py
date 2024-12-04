print("LE HOANG VIET DUNG")
print("235752021610104")
from search_module import binary_search

def main():
    arr = [1, 2, 3, 5, 8]
    x1 = 6
    x2 = 5

    result1 = binary_search(arr, x1)
    result2 = binary_search(arr, x2)

    print(f"binary_search({arr}, {x1}) -> {result1}")
    print(f"binary_search({arr}, {x2}) -> {result2}")

if __name__ == "__main__":
    main()
