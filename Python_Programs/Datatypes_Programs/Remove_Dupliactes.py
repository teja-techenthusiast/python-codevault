unique_lst = []
for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)
print("List without Duplicates:", unique_lst)