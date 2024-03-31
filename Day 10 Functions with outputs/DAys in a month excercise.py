def is_leap(year):
	"""This takes a year and determines if it is a leap year. Will
	return true or false"""
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				# print("Leap year")
				return True
			else:
				# print("Not leap year")
				return False
		else:
			# print("Leap year")
			return True
	else:
		# print("Not leap year")
		return False


# TODO: Add more code here 👇
def days_in_month(year, month):
	"""Takes a year and a month and will give you the days in the month"""
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if is_leap(year) is True and month == 2:
		days = 29
	else:
		days = month_days[month-1]
	return days


# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
