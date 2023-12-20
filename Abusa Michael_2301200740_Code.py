#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Code for scheduling Uganda Mass Verification exercise
def main():
	# Taking the number of processes
	n = int(input("Number of Settlements: "))
	# Matrix for storing settlement Id, activity duration (in days), average waiting time & Average turnaround time.
	A = [[0 for j in range(4)] for i in range(80)]
	total, avg_wt, avg_tat = 0, 0, 0
	print("Duration:")
	for i in range(n): # User input activity duration and allotting settlement Id.
		A[i][1] = int(input(f"Settlement{i+1}: "))
		A[i][0] = i + 1
	for i in range(n): # Sorting process according to their duration.
		index = i
		for j in range(i + 1, n):
			if A[j][1] < A[index][1]:
				index = j
                
		temp = A[i][1]
		A[i][1] = A[index][1]
		A[index][1] = temp
		temp = A[i][0]
		A[i][0] = A[index][0]
		A[index][0] = temp
	A[0][2] = 0 # Calculation of waiting time
	for i in range(1, n):
		A[i][2] = 0
		for j in range(i):
			A[i][2] += A[j][1]
		total += A[i][2]
	avg_wt = total // n
	total = 0
	# Calculation of time to completion and printing the data.
	print("Settlement	 Dtn	 Begin	 End")
	for i in range(n):
		A[i][3] = A[i][1] + A[i][2]
		total += A[i][3]
		print(f"Settlement {A[i][0]}	 {A[i][1]}	 {A[i][2]}	 {A[i][3]}")
	avg_tat = total // n
	print(f"Average Duration to begin= {avg_wt}")
	print(f"Average Duration to finish= {avg_tat}")
if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




