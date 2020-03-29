#!/usr/bin/python 
# coding:utf-8
# @author: @monkeyrp

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。# 同样的元素不能被重复利用指？
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

import sys
import os

class TwoSum(object):
	def __init__(self):
		pass
    # o(n^2)
	def two_sum_n2(self, num_target, nums_list):
		num_value = []
		if nums_list != None:
			for i in range(len(nums_list)):
				for j in range(i, len(nums_list)):
					if nums_list[i] + nums_list[j] == num_target:
						num_value.append(nums_list[i])
						num_value.append(nums_list[j])
		return num_value
	#o(n)
	def two_sum_n(self, num_target, nums_list):
		num_value = []
		if nums_list != None:
			for i in range(len(nums_list)):
				if (i == len(nums_list) - 1):
					return "no solution here!"
				else:
					num_sub = num_target - nums_list[i]
					if num_sub in nums_list[i+1:] and num_sub != nums_list[i]:
						num_value.append(i)
						num_value.append(nums_list.index(num_sub))
						return num_value
		else:
			return "no list!"

if __name__ == '__main__':
	ts = TwoSum()
	#print(ts.two_sum_n(9,[3,11,7,15]))
	#print(ts.two_sum_n(10,[2,7,11,15]))
	print(ts.two_sum_n(10,None))
	#print(ts.two_sum_n(10,[2]))
	#print(ts.two_sum_n(10,[2,7,11,8]))
	#print(ts.two_sum_n(10,[2,7,11,10]))
	print(ts.two_sum_n(12,[2,7,2,10]))