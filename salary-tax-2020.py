#!/usr/bin/python3
import sys
#run script "./salary-tax-2020.py 1000" where 1000 is example of gross monthly salary.

monthly_salary = int(sys.argv[1])   

###tax7
#seg0: 

result0 = 0
result2 = 0
result10 = 0
result15 = 0
result20 = 0
result22 = 0
result25 = 0


yearly_salary0 = (monthly_salary * 12) - 9000
if yearly_salary0 >= 0: 
  result0 = 0
#seg2.5
yearly_salary2 = yearly_salary0 - 15000 
if yearly_salary2 > 0: 
  result2 = min([yearly_salary2, 15000]) * 0.025

#seg10
yearly_salary10 = yearly_salary2 - 15000 
if yearly_salary10 > 0: 
  result10 = min([yearly_salary10, 15000]) * 0.1

#seg15
yearly_salary15 = yearly_salary10 - 15000 
if yearly_salary15 > 0: 
  result15 = min([yearly_salary15, 15000]) * 0.15

#seg20
yearly_salary20 = yearly_salary15 - 15000 
if yearly_salary20 > 0: 
  result20 = min([yearly_salary20, 140000]) * 0.2

#seg22.5
yearly_salary22 = yearly_salary20 - 140000 
if yearly_salary22 > 0: 
  result22 = min([yearly_salary22, 200000]) * 0.225

#seg25
yearly_salary25 = yearly_salary22 - 200000 
if yearly_salary25 > 0: 
  result25 = yearly_salary25 * 0.25

print("result0: " + str(result0), "result2.5: " + str(result2), "result10: " + str(result10), "result15: " + str(result15), "result20: " + str(result20), "result22.5: " + str(result22), "result25: " + str(result25), sep='\n=========================\n')


total_yearly  = result0 + result2 + result10 + result15 + result20 + result22 + result25
total_monthly = total_yearly / 12
print('\n------------------------------------------\n')
print("Total per Month: " + str(total_monthly), "Total per Year: " + str(total_yearly), sep='\n=========================\n')
