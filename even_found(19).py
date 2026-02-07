nums =[1,2,3]
def even_found(nums):
	for i in nums:
		if i % 2==0:
			print("Even found")
			break
	else:
		print("No even found")
print(even_found(nums))