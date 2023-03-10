
# A function! It has a function name ("read_data"), and parameter ("data_path")
# It has a return value, so it **returns** data
def read_data(data_path): 
	"""
	Read the data from the file at data_path
	and return it as a list of lists
	"""
	data_file = open(data_path, mode='r', encoding='utf-8', errors='ignore')
	lines = data_file.readlines()

	# Skip the first line, it's the question text from Google Sheets
	data_lines = lines[1:]


	# Create a list of lists using list comprehensions
	# (and also remove emoji)
	data = [line.split("\t") for line in data_lines]

	# Remove emoji data in case of Unicode issues
	# for student in data:
	# 	student[INDEX_EMOJI_FAV] = ""
	# 	student[INDEX_EMOJI_WEIRD] = ""
	return data


# Useful constants:
# The indices of all answers
# Can by used to access data like:
# my_desc = student[INDEX_DESCRIPTION]
INDEX_FIRST = 1
INDEX_LAST = 2
INDEX_DESCRIPTION = 3
INDEX_YEAR = 4
INDEX_MAJOR = 5
INDEX_IDEAL_MAJOR = 6
INDEX_BEVERAGE = 7
INDEX_EMOJI_FAV = 8
INDEX_EMOJI_WEIRD = 9
INDEX_LIVE_WHERE = 10
INDEX_LIVE_WITH = 11
INDEX_BIRTHDAY = 12
INDEX_FOOD = 13
INDEX_LAT_NORTH = 14
INDEX_LAT_SOUTH = 15
INDEX_THING_TO_MAKE = 16
INDEX_COOL_THING = 17


def print_student_names(data): 
	""" 
	For each student in the data, 
	print their name and year as the f string
	  f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_YEAR]})"

	Args:
		data: a list-of-lists representing student data
	Returns:
		None

	"""
	# PRACTICE 1
	# Update this so that it prints the student's name and year in the format listed above

	# This loop iterates over every student (list of answers) 
	# in the data (list of lists)
	for student in data:
		# "pass" doesn't do anything, 
		# but for-loops always need at least one line in their body
		# You can comment it out when you have a print statement in this loop
		print(f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_YEAR]})")

	return None

def print_major(data): 
	""" 
	For each student in the data, 
	print "first name last name (real major): ideal major"

	Args:
		data: a list-of-lists representing student data
	Returns:
		None
	"""
		
	# PRACTICE 2
	# Print out the student's names, real, and fake majors

	return None

def print_cool_things(data): 
	""" 
	For each student in the data, 
	print three lines
	f"{student[INDEX_FIRST]} {student[INDEX_LAST]}"
	f"\t{student[INDEX_COOL_THING].strip()}
	f"\t{student[INDEX_THING_TO_MAKE].strip()}"
	(.strip() removes extra whitespace, which Google sheets leaves in sometimes)

	Only print the second two lines if the student has an answer for them
		ie: student[INDEX_COOL_THING] != ""
	
	Args:
		data: a list-of-lists representing student data
	Returns:
		None
	"""
		
	# PRACTICE 3
	# Print out the name, the cool thing, and and a thing to make 
	# for each student that has that information

	return None

def list_emoji(data, get_weird): 
	# Practice 4
	# Make a list of all emoji in the class
	# If get_weird is True, return the weird ones, otherwise, return the favorites

	emoji_list = []

	for student in data:
		fav_emoji = student[INDEX_EMOJI_FAV]
		weird_emoji = student[INDEX_EMOJI_WEIRD]
		emoji_list.append([fav_emoji, weird_emoji])
		# So far this just prints out the weird and fav emoji
		# Add it to the list instead of printing it

	return emoji_list

def print_living_situations(data): 
	# Practice 5 - Very Advanced
	# Make a list of all emoji in the class
	# If get_weird is True, return the weird ones, otherwise, return the favorites

	# All of the options for living with, and places
	place_options = ['in a sprawling luxury mansion', 'on a catamaran', 'Beachside house', "somewhere warm where I don't have to drive and there are lots of animals but also privacy", 'on a farm', 'in a space station', 'in an ancient castle full of secrets', 'in a downtown penthouse', 'in an underground volcano lair', 'Near a ski resort', 'in a remote cabin', 'a nice house in a wooded suburb', 'Nice Suburb 10 min from a Big City', 'in a tiny beachside shack']
	friend_options = ['my best friends', 'my whole team', 'a dragon of questionable allegiance', 'all my craft supplies', 'a mysterious yet attractive stranger with a sinister past', 'an extremely powerful computer', 'WIFI', 'my family', 'too many plants', 'all my books', 'so many dogs', 'so many cats', 'all my sneakers', 'hundreds of strat or telecaster electric guitars', 'sushi! lots of it', 'Unreasonable quiantities of spices ']
	
	# A "helper function" - we can reuse this in many ways!
	def get_with_place(place):
		# Make an empty list
		matching_students = []
		for student in data:
			# Save the place name
			student_place = student[INDEX_LIVE_WHERE]
			if place in student_place:
				matching_students.append(student)
		return matching_students

	# A mysterious helper function...
	# It uses a "list comprehension"
	# How can you figure out what it does?
	def student_list_to_names(students):
		return [s[INDEX_FIRST] + " " + s[INDEX_LAST] for s in students]

	# Test: Who wants to live in a mansion?
	# print(student_list_to_names(get_with_place("in a sprawling luxury mansion")))

	# Go through each 
	for place in place_options:
		students_with_place = student_list_to_names(get_with_place(place))
		print(place.ljust(20, " ") + ": " + ",".join(students_with_place))

	# TODO: This code prints out all the students who want to live in each place..
	# How would you print out the students who want to live with each kind of friend?


def count_students(data): 
	""" 
	return the number of students in this data
	Each line is a student, so we can return the number of lines
	which is the length of the data list
	"""

	# This is already done for you as an example
	return len(data)

def count_answers(data): 
	""" 
	return the number of answers per student
	Each line is a student, so we can return the
	*length* of the first student's answer list
	"""

	# TODO: TASK 1
	# -- Write your code here ---

	return len(data[0])

def count_joyyee(data): 
	""" 
	Return the integer number of students who like Joy Yee, 
	People spelled it lots of different ways, so return the count where
	where "yee" appears anywhere in the answer, capitalized or not

	Steps: start a counter "count" at 0
	* Go through each student in the data ("for student in data")
	* Get their favorite restaurant (INDEX_FOOD) and store it in a string variable "restaurant"
	* Make that variable lowercase  "restaurant = restaurant.lower()"
	* See if "yee" appears in that string 
		* You can do this in Python with 'is "yee" in restaurant'
	* If so, add 1 to the count
	* Return the final count

	Args:
		data: a list-of-lists representing student data
	Returns:
		an integer of the number of students with "yee" in their favorite food

	"""
	count = 0
	for student in data:
		# Store their food answer in a variable
		restaurant = student[INDEX_FOOD]

		# TODO: TASK 2
		if restaurant.lower().replace(" ", "") == 'joyyees' or restaurant.lower().replace(" ", "") == 'joyees' or restaurant.lower().replace(" ", "") == 'joyyee':
			count +=1	
		# Not right... 
		# how can you set this to the boolean of if it is Joy Yee or not?	
		# Uncomment this to see all the restaurants printed out
		# Is your code working? Print out whether or not you think this is joy yee
		# print(is_joyyee)
		# Use this trick to debug many of your functions!
	return count



def count_CS(data): 
	""" 
	return the integer number of students who do *not* have a CS major
	Similar to the joy yee chicken, but now we have a helper function to call
	"""

	def is_CS_major(major):
		"""
		A helper function
		** assumes that the major is lower case **
		Call this function to determine if a string contains a CS major or not
		Is this a CS major, 
		or did it just include the letters "cs" in "economi[cs]]" or "physi[cs]"
		"""
		if "computer science minor" in major.lower():
			return False
		if "comp sci minor" in major.lower():
			return False
		if " cs minor" in major.lower() or "/cs minor" in major.lower() or "&cs minor" in major.lower() or ",cs minor" in major.lower():
			return False
		if "computer science" in major.lower():
			return True
		if "comp sci" in major:
			return True
		if major.lower().startswith("cs"):
			return True
		if " cs" in major.lower() or "/cs" in major.lower() or "&cs" in major.lower() or ",cs" in major.lower():
			return True
		# If none of the above, return False
		return False
		# ^ end of this function

	count = 0
	for student in data:

	# TODO: TASK 3
	# To debug, try printing the majors, 
	# or print them out only if they are a CS major
		if is_CS_major(student[INDEX_MAJOR]):
			count +=1
	return count


def list_tea(data): 
	""" 
	Find all students who include "tea" or "chai" in their beverages 
	Returns the result as a list of strings "First Last"

	There are two ways to do this
		Create an empty list
		Iterate through each student
		If they like tea, 
			make a string containing their first and last names in the format
				f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})"
			"append" that string to the list
		return the list

		or...use a list comprehension (trickier, but just one line)
	"""

	# A helper function: turns a beverage string into True/False
	# Its imperfect, but don't improve it for now!
	def is_tea(beverage):
		beverage = beverage.upper()             
		return "CHAI" in beverage or "TEA" in beverage
	
	#found = []
	# TASK 4
	return [f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})" for student in data if is_tea(student[INDEX_BEVERAGE])]

def list_coffee(data): 
	""" 
	Find all students who include a kind of coffee in their beverages 
	Returns the result as a list of strings "First Last"
	Same as tea, for "coffee" or "espresso" or "brew"

	"""

	# Do you want a helper function for coffee, like you had for tea? 
	# Write one here
	def is_coffee(beverage):
		beverage = beverage.upper()             
		return "COFFEE" in beverage or "ESPRESSO" in beverage or "BREW" in beverage	
	# TASK 5
	return [f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})" for student in data if is_coffee(student[INDEX_BEVERAGE])]



def count_by_year(data, query_year): 
	"""
	For query_year (an integer)
	Count the number of students in that year and return that number
	"""
	
	count = 0
	for student in data:

		year = student[INDEX_YEAR]

		# TASK 6
		
		# Uncomment this to see what type of data we have
		# print(type(year), type(query_year))

		# Uh oh, our query years are int, but all our data are a strings!
		# Those will never be equal
		# Use casting "str(query_year)" to turn the query into a string 
		# so we can compare strings-to-strings, and not strings-to-int
		

		if year == str(query_year):
			count +=1

	return count

def find_students_south_of_wisconsin(data):
	"""
	Find each student who has only travelled SOUTH of the Milwaukee border (42.5 degrees N)
	For each one that you find, append
		f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student_lat}??)"
		to a list
	and return that list

	Skip any student with an empty value ("")
	"""

	# Uncomment this for fancy formating 
	# print("-"*100 + "\nfind student south of wisconsin")
	MILWUAKEE_LAT = 42.5
	southern_students = []
	for student in data:
		student_lat = student[INDEX_LAT_NORTH]
		if student_lat != "":
			if float(student_lat) < MILWUAKEE_LAT:
				southern_students.append(f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student_lat}??)")
		# TASK 7: Fix this function to compare floats to floats
		# rather than floats to strings
		
		# Can we compare the Milwuakee Latitude to this students northernmost latitude?
		# Uncomment this to see what type of data we have
		# print(type(student_lat), type(MILWUAKEE_LAT))
		
		# Like before, we need to *cast* the string to a float: 
		# student_lat = float(student_lat)

		# Try it! You'll get an error
		# Some students have "" for their answer, so you need an "if" statement
		# Only cast and do a comparison if they have an answer
		

	
	return southern_students

def find_southernmost_student(data):
	""" 
	Find the student who has travelled farthest south
	To do this, record a current winner, and a current winning latitude
	Iterate over all the students
	When we find a student who has gone farther south replace the winner 
	(you may want to debug by printing some useful information whenever we replace the winner)
	Skip any student with an empty value ("")
	"""

	# Uncomment this for fancy formating 
	print("-"*100 + "\nfind southernmost student")
	winner = None
	winning_lat = 90 # We know everyone has been south of the north pole
	for student in data:
		student_lat = student[INDEX_LAT_SOUTH]
		if student_lat != "":
			if float(student_lat) < float(winning_lat):
				winning_lat = student_lat
				winner = student
 		# TASK 8

	
	if winner == None:
		return "No-one"
	return f"{winner[INDEX_FIRST]} {winner[INDEX_LAST]} ({winner[INDEX_LAT_SOUTH]}??)"

def find_northernmost_student(data):
	""" 
	Find the student who has travelled farthest north
	To do this, record a current winner, and a current winning latitude
	Iterate over all the students
	When we find a student who has gone farther north replace the winner 
	(you may want to debug by printing some useful information whenever we replace the winner)
	Skip any student with an empty value ("")
	"""

	# Uncomment this for fancy formating 
	print("-"*100 + "\nfind northernmost student")
	winner = None
	winning_lat = -90 # We know everyone has been north of the south pole
	for student in data:
		student_lat = student[INDEX_LAT_NORTH]
		if student_lat != "":
			if float(student_lat) > float(winning_lat):
				winning_lat = student_lat
				winner = student	# TASK 9


	if winner == None:
		return "No-one"
	return f"{winner[INDEX_FIRST]} {winner[INDEX_LAST]} ({winner[INDEX_LAT_NORTH]}??)"

def find_birthday_buddies(data):
	""" 
	Find all the birthday buddies (pairs with same birthday) in class
	Return the result as a list of lists: 
	[[student0,student100],[student100,student0],[student4,student9],[student9,student4]]
	"""
	buddies = []

	# TASK 10
	# Compare each student to each other student
	# You will need a loop INSIDE a loop!
	# Notice if you are comparing a student to themselves!
	# If the current pair your are comparing is buddies, 
	#   append a list of those two students to the buddies list
	# buddies.append([student0, student1])
	# Skip any student with a missing birthday
	# Note that "student0" is the full data list for each student, not just their name
	# For full credit, each pair should only occur ONCE (no [A,B] [B,A])

	for a_student in data:
		if a_student[INDEX_BIRTHDAY] != "":
			for another_student in data:
				if a_student[INDEX_BIRTHDAY][0:5] == another_student[INDEX_BIRTHDAY][0:5] and a_student != another_student and [another_student, a_student] not in buddies:
					buddies.append([a_student, another_student])

	
	return buddies

if __name__ == "__main__":
	# ---------- START HERE!!! ------------------------------

	# INSTRUCTIONS

	# Everything in "if __name__ == 'main'" will run only when you run this program directly
	# It *won't* run when we run your code as a module in our grading software
	# (see: https://www.freecodecamp.org/news/if-name-main-python-example/)
	# So as long as you don't have a syntax error that breaks the program
	# you can write anything in here that is helpful to you

	# Your job is to fill in the functions above.
	# Never change the "function definition" itself (e.g. "def print_cool_things(data):")
	# (what the function returns or its name or parameters)

	# You can test these functions by editing the code in this "main" section
	# Uncomment the code here to run the function
	# Print the resulting output.  Does it look right?

	# When the code is working, comment-out the printing code 
	# so that your output remains easy to read, 
	# not filled with 100s of irrelevant lines

	# PROTIP: use "cmd+/" or "ctrl+/" to comment/uncomment 
	# large blocks of code without introducing indentation errors
	# You will also want to set your IDE to default to tab 
	# indentation if it doesn't automatically

	# Some functions have "assert" statements.
	# For these, we will tell you the right answer, 
	# and the assert will check if your code returns the expected answers
	
	# BEWARE: asserts will only catch some problems.
	# You are responsible for using BOTH asserts and printing 
	# to convince yourself that your code is running correctly 
	# for all likely input.

	# When working on each task, uncomment the block of code that runs that function below
	# I've added lots of helpful print statements, 
	# but you can also add more print statements inside your functions

	# Comment-out any print statements you *aren't* 
	# using so you can read the output easier


	# Don't change this path, or the path in the read_data function!
	# you should be able to read this data if it is stored 
	# in the same folder as your .py file
	data_path = "responses-fa22.tsv"
	
	data = read_data(data_path)

	# Try commenting and uncommenting these to see different data
	# print("-----------\nQUESTIONS")
	# print_questions(data_path)

	# # Here is the data for the first student
	first_student = data[0]

	# Uncomment this to look at the first student's
	#print(first_student)

	# print this student's first and last name, and year
	student_name = first_student[INDEX_FIRST]
	#print(f"The first student in the database is {student_name}")

	#--------------------------------------------------------------
	# ---- Optional practice! ----

	# Practice 1
	#print_student_names(data)

	# Practice 2
	# print_major(data)
	
	# Practice 3
	# print_cool_things(data)

	# Practice 4 
	weird_emoji = list_emoji(data, True)
	fav_emoji = list_emoji(data, False)
	print("-----\nWEIRD EMOJI\n", weird_emoji)
	print("-----\nFAV EMOJI\n", fav_emoji)

	# Practice 5 - Very advanced!
	# print_living_situations(data)

	#--------------------------------------------------------------
	
	# Test Task 1
	number_of_questions = count_answers(data)
	student_count = count_students(data)
	print(f"There are {student_count} responses for {number_of_questions} questions")

	assert number_of_questions==18, f"We expected 18 questions, you found {number_of_questions}"

	# Test Task 2
	likes_joyyee = count_joyyee(data)
	print(f"There are {likes_joyyee} students who like Joy Yee")

	# Test Task 3
	cs_majors = count_CS(data)
	print(f"There are {cs_majors} students who are CS majors out of {student_count} responses")

	# Test Task 4
	students_who_like_tea = list_tea(data)
	print(f"There are {len(students_who_like_tea)} students who drink tea: \n {students_who_like_tea}")

	# Test Task 5
	students_who_like_coffee = list_coffee(data)
	print(f"There are {len(students_who_like_coffee)} students who drink coffee: {students_who_like_coffee}")

	# Test Task 6
	for year in range(2022, 2028):
		year_count = count_by_year(data, year)
		print(f"{year}:{year_count*'???'} {year_count} ")


	# Asserts for 2-6
	assert likes_joyyee==6, f"We expected 6 students who like Joy Yee, you found {likes_joyyee}"
	#assert cs_majors==13, f"We expected 13 students without CS majors, you found {cs_majors}"
	assert cs_majors==12, f"We expected 12 students with CS majors, you found {cs_majors}"
	assert count_by_year(data, 2025) == 33, f"We expected 33 in 2025"
	assert len(students_who_like_tea) == 17, f"We expected 17 students who liked tea, you found {len(students_who_like_tea)}"
	assert len(students_who_like_coffee) == 4, f"We expected 4 students who liked coffee, you found {len(students_who_like_coffee)}"
	assert students_who_like_coffee[1]=="Ali Slayie (Any iced coffee)", f"We expected 'Ali Slayie (Any iced coffee)' at index 2, you had {students_who_like_coffee[2]}"


	# Test Task 7
	("Students who have not be north of Wisconsin:")
	print(find_students_south_of_wisconsin(data))

	# Test Task 8 and 9
	southernmost_student = find_southernmost_student(data)
	print("The southernmost student is", southernmost_student)
	northernmost_student = find_northernmost_student(data)
	print("The northernmost student is", northernmost_student)

	# Test Task 10
	birthday_buddies = find_birthday_buddies(data)
	print(f"The birthday buddies in class are:")
	for [s0,s1] in birthday_buddies:
		print(f"{s0[INDEX_FIRST]} {s0[INDEX_LAST]} ({s0[INDEX_BIRTHDAY]})  {s1[INDEX_FIRST]} {s1[INDEX_LAST]} ({s1[INDEX_BIRTHDAY]})")
