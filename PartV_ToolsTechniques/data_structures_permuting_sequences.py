from datastructures_lib import permute_subset_combo

print(permute_subset_combo.permute([1,2,3]))
print(permute_subset_combo.permute('abc'))
print(permute_subset_combo.subset([1,2,3], 3))
print(permute_subset_combo.subset('abc', 3))
print(permute_subset_combo.subset('abc', 2))
print(permute_subset_combo.combo([1,2,3], 2))
for i in range(0, 6):
    print(i, permute_subset_combo.combo('help', i))
