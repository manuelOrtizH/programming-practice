#Manuel Ortiz Hernández at 2020
#LeetCode problem solving extracted from:

def two_sum(nums, target):
	nums_d = {}
	repeated = []
	index = 0

	for i in range(len(nums)):
		nums_d.setdefault(nums[i], [])
		if nums[i] in nums_d.keys():
			nums_d[nums[i]].append(i)#Can't be repeated keys... investigar :(
		else:
			nums_d[nums[i]] = i  


	for keys in nums_d.keys():
		complement = target - keys
		if complement in nums_d.items():
			if len(nums_d[keys]) >= 2:
				repeated.append(nums_d[keys][0])
				repeated.append(nums_d[keys][1])
			else:
				repeated.append(index)
				repeated.append(nums_d[keys].values())

		index+=1

	print(repeated)

def read_data():
	nums = list(map(int, input().split()))
	target = int(input())
	dict_data = {"nums": nums, "target": target}
	return dict_data

def main():
	dict_data = read_data()
	two_sum(dict_data["nums"], dict_data["target"])
	#print(result.values())

if __name__ == "__main__":
	main()
	


 		



        

