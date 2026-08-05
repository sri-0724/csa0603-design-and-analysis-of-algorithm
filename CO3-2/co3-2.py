import time
transactions = [
    {"Transaction ID": "T101", "Customer": "Arun", "Amount": 4500},
    {"Transaction ID": "T102", "Customer": "Priya", "Amount": 1200},
    {"Transaction ID": "T103", "Customer": "Rahul", "Amount": 9800},
    {"Transaction ID": "T104", "Customer": "Divya", "Amount": 3500},
    {"Transaction ID": "T105", "Customer": "Karthik", "Amount": 6700},
    {"Transaction ID": "T106", "Customer": "Meena", "Amount": 1500},
    {"Transaction ID": "T107", "Customer": "Ajay", "Amount": 8900},
    {"Transaction ID": "T108", "Customer": "Nisha", "Amount": 2500},
    {"Transaction ID": "T109", "Customer": "Ravi", "Amount": 5200},
    {"Transaction ID": "T110", "Customer": "Anu", "Amount": 7200}
]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]["Amount"] <= right[j]["Amount"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]["Amount"]
    left = [x for x in arr if x["Amount"] < pivot]
    middle = [x for x in arr if x["Amount"] == pivot]
    right = [x for x in arr if x["Amount"] > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def display(data):
    print("-" * 55)
    print("{:<8} {:<12} {:>10}".format("ID", "Customer", "Amount"))
    print("-" * 55)
    for item in data:
        print("{:<8} {:<12} {:>10}".format(
            item["Transaction ID"],
            item["Customer"],
            item["Amount"]
        ))
    print("-" * 55)
print("\nORIGINAL FINANCIAL TRANSACTIONS\n")
display(transactions)
merge_data = transactions.copy()
start = time.perf_counter()
merge_sorted = merge_sort(merge_data)
end = time.perf_counter()
print("\nTRANSACTIONS SORTED USING MERGE SORT\n")
display(merge_sorted)
print("Merge Sort Execution Time : {:.8f} seconds".format(end-start))
quick_data = transactions.copy()
start = time.perf_counter()
quick_sorted = quick_sort(quick_data)
end = time.perf_counter()
print("\nTRANSACTIONS SORTED USING QUICK SORT\n")
display(quick_sorted)
print("Quick Sort Execution Time : {:.8f} seconds".format(end-start))
