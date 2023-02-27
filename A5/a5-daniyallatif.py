
"""

The Gale-Shapely algorithm is an algorithm that, 
given two non-overlapping groups, group A and group B,
and each group members preference for the members of the other group
makes pairings of A and B members, so that no two people would both 
be happier if they switched partners with each other.

You will be *writing* methods in this class, and their definitions 
(what their method-name, parameters and return values are)
will need to match the specification below *exactly!*

Also note that the last 3 tasks 
DONT HAVE ASSERTS!!

Oh no!
How will you figure out if you have the right answer?
This is common in real-world code. You will have to rely 
on printing out information and asking yourself questions
Is this the best set of partnerships that could be found?

"""

import random
import time
import csv
from test_data import construct_dataset

class Student:


	"""
	A class to represent a student and their preferences for partner
	** Review https://www.programiz.com/python-programming/class
	if you don't know how to specify methods in a class **

	...

	Attributes
	----------
	all_students(list of Student): a list of all the Student instances in this 
		student's matchmaking set. Both group A and group B are in here
	
	name(str): the (unique) name for this student
		Later, we will finding a student's information by their name
		In the real world, names are not unique, 
		so we would use an unique identifier like a NetID
	
	partner_ratings(list of str): a list of the names of all students in the 
		other group, sorted by how much this student prefers them
		e.g ["Alice", "Adam", "Anya", "Allen"] <- prefers "Allen" *the most*
	
	potential_partners(list of str): 
		starts as [] until we reset it with reset_partnerships
			and it becomes a copy of partner_ratings that we can remove  
			names from (without affecting the original partner ratings)
	
	partner(Student): this student's current partner
		starts as None until we reset it with reset_partnerships
		

	Methods
	-------


	__init__(self, all_students, name, partner_ratings):
		initialize this Student by storing these as attributes
		Also initializes potential_partners to [] and partner to None
		Parameters:
			name(str): student's name
			all_students(list): all Student instances in this set
			partner_ratings(list of strings): this student's prefered partners
				e.g ["Alice", "Adam", "Anya", "Allen"] <- prefers "Allen" *the most*

	__str__(self):
		"stringify" this Student by just returning their name
	
	reset_partnerships(self):
		Remove the current partner and initialize our
		potential_partners to a copy of the partner_ratings

	has_partner(self):
		returns True if has a partner, False otherwise
	
	get_rating(self, name)
		Given a name, return their index in the ratings
		e.g. name="Candy", ratings=["Chaz", "CJ", "Candy"] -> 2

		Parameters:
			name(str)
		Returns:
			(int): the index of that name in this Student's partner ratings
		Raises: ValueError if there is no such name in our partner ratings


	get_rating_of_partner(self)
		How satisfied are we with our current partner?

		Returns:
			(int): the index of the current partner in this Student's partner ratings
				if we have a partner, otherwise returns 0
	
	break_partnership(self):
		If this student has a partner, remove them as their partner's partner
		then remove their partner

	make_partnership(self, new_partner):
		Make a partnership with this new partner
		If they have a partnership already, break up that partnership
		Set these two to be each other's partners

		Parameters:
			new_partner(Student)

	offer_to_top_choice(self):
		Offer a partnership to the top choice still in potential_partners
		The potential partner may
			Accept because they have no partner (make the partnership)
			Accept because like us better than their current partner
				(make the partnership)
			Reject because they like their current partner better
		in any case, remove that person's name from our potential partners

	"""


	#------------------------------------------------------
	# Task 0: Create an __init__ method for this Student Class
	# Store all_students, name, and partner_ratings as attributes 
	# (i.e., self.some_attribute_name) on this student object. 
	# Also initialize the attribute's potential_partners to [] 
	# and partner to None, and append this student to all_students

	def __init__(self, all_students, name, partner_ratings):
		all_students.append(self)
		self.all_students = all_students
		self.name = name
		self.partner_ratings = partner_ratings
		self.potential_partners = []
		self.partner = None


	#------------------------------------------------------
	# Task 1: Create an __str__ method for this Student Class
	# It needs to return a string (all __str__ methods return a string)
	# which in this case, is just the Student's name
		
	def __str__(self):
		return f"{self.name}"

	#------------------------------------------------------
	# Task 2: Implement has_partner
		
	def has_partner(self):
		return self.partner is not None

	#------------------------------------------------------
	# Task 3: Implement get_rating
	# Given a name, return how much this student wants to work with 
	#	the student by that name (higher numbers are better)
	# Given a name, return their index in the ratings
	#	e.g. name="Candy", ratings=["Chaz", "CJ", "Candy"] -> 2 (top rated!)
	#	If this name is not in the ratings, 
	#		it is ok not handle that and to let Python raise a ValueError: 
	#   	it suggests a problem somewhere else, which we want to be alerted to
	#	Note that Python lists have an easy-to-use method
	#	to find the index of an element in a list: 
	#	https://www.programiz.com/python-programming/methods/list
	def get_rating(self, name):
		if name not in self.partner_ratings:
			raise ValueError(f"{name} isn't in {self.name}'s partner ratings: {self.partner_ratings}")
		return self.partner_ratings.index(name)


	#------------------------------------------------------
	# Task 4: Implement get_rating_of_partner
	# 	If there is no current partner, return 0,
	# 		Otherwise, return our rating for our current partner
	def get_rating_of_partner(self):
		if self.partner is None:
			return 0
		return self.get_rating(self.partner.name)

	#------------------------------------------------------
	# Task 5: Implement break_partnership
	# 	If we have a partner, set our partner's partner to None
	# 	then set our partner to None
	def break_partnership(self):
		if self.partner is not None:
			self.partner.partner = None
			self.partner = None


	#------------------------------------------------------
	# Task 6: Implement make_partnership
	# 	Form a partnership with this person
	#	If the new_partner already has a partner, we need to break them up
	#	If we already have a partner, we need to break up, too
	#	Then set this person as our partner, and set us as this person's partner
	def make_partnership(self, new_partner):
		if new_partner.partner is not None:
			new_partner.break_partnership()
		if self.partner is not None:
			self.partner.break_partnership()
		self.partner = new_partner
		new_partner.partner = self
	
	#------------------------------------------------------
	# Task 8: Implement offer_to_top_choice
	# This student is going to propose a partnership with their 
	# 	current top choice (who has not already rejected them)

	# 	*Pop* the top name from potential_partners 
	# 	(this will remove it from the list)
	# 	Use this name to get the Student object with that name from our all_students
	# 	We then propose a partnership to that student

	# 	There are three outcomes:
	# 	- this potential partner does not have a partner yet
	# 		- they accept the proposal, make the partnership			
	# 	- they *do* have a partner
	# 		- get their rating of their current partner, and their rating of us
	# 		- if we are higher, they accept the proposal 
	# 			and break up with their current partner
	# 			- make the partnership
	# 		- if we are lower, nothing happens, but they are now 
	# 			removed from our list of potential partners
	def offer_to_top_choice(self):
		top_choice_name = self.potential_partners.pop()
		top_choice = None
		for student in self.all_students:
			if student.name == top_choice_name:
				top_choice = student
		if top_choice.partner is None:
			self.make_partnership(top_choice)
		elif top_choice.get_rating_of_partner() < top_choice.get_rating(self.name):
				top_choice.break_partnership()
				self.make_partnership(top_choice)
		else:
			return None



	#-----------------------------------------------		
	# Methods for you
	def reset_partnerships(self): 
		"""
		This is a method that is called when we are about to begin matchmaking
		It clears our our partner (if we had one)
		And initializes our potential_partners to a copy of our partner_ratings
		(so we can run different matchmaking algorithms, 
		 and reset back to the same conditions each time)
		
		Returns: None
		"""
		self.potential_partners = [s for s in self.partner_ratings]
		self.partner = None


	def find_by_name(self, name):
		""" 
		Given a name (str), 
		return the Student with that name in our all_students
		"""
		matches = [s for s in self.all_students if s.name == name]
		if len(matches) > 0:
			return matches[0]
		return None


def make_partnerships(group_a, group_b):
	"""
	Make not-very good partnerships by pairing up the first person 
	in group_a with the first person in group_b... etc

	Parameters:
		group_a (list of Student): a list of students
		group_b (list of Student): a list of students (the same size as group_a)
	"""

	# Task 7: Make naive partnerships for each student in group_a
	#   (hint: use a for loop over an *enumerated* list of group_a)
	for i, student in enumerate(group_a):
		student.partner = group_b[i]
		group_b[i].partner = student

def make_gale_shapely_partnerships(proposers, partners):
	"""
	Make partnerships with the Gale Shapely algorithm
	This should result in better partnerships than the previous approach

	Some visual animations of how it works 
	if that helps you understand the algorithm
	(https://www.youtube.com/watch?v=fudb8DuzQlM)
	(https://mindyourdecisions.com/blog/2015/03/03/the-stable-marriage-problem-gale-shapley-algorithm-an-algorithm-recognized-in-the-2012-nobel-prize-and-used-in-the-residency-match/)

	Parameters:
		proposers (list of Student): a list of students 
			who get to make offers to their favorite potential partners
		group_b (list of Student): a list of students 
			who decide whether or not to accept the offers
	"""

	# Task 9: Implement the Gale Shapely algorithm
	#	Notice: you already have the most complex part (offer_to_top_choice)
	# 	
	# 	While there are any unpartnered proposers left:
	#		Each unpartnered proposer offers to their top choice partner
	#			That partner may accept or not (that is handled by offer_to_top_choice) 
	#		Eventually, if the algoritm is implemented correctly, 
	#		everyone will be partnered
	#	Why is offer_to_top_choice a method on a Student instance, 
	#		rather than part of this function?
	#		It is easier to think about it as *one* student making a choice!

	# This is the only time we need the partners list
	# otherwise, the partners are stored in 
	# the preferences of the proposers
	[s.reset_partnerships() for s in  proposers]
	[s.reset_partnerships() for s in  partners]

	while get_unpartnered(proposers) != []:
		for p in get_unpartnered(proposers):
			p.offer_to_top_choice()


#---------------------------------------------------------------
# Utility functions


def get_unpartnered(group):
	"""
	Return a list of all unpartnered Students in this group
	"""
	return [s for s in group if not s.has_partner()]

def get_partnerships(group): 
	"""
	Return a list of all partnerships in this group
	"""
	return [(s,s.partner) for s in group if s.has_partner()]

def count_partnerships(group): 
	"""
	Return the number of partnerships in this group 
	"""
	return len(get_partnerships(group))


def partnerships_to_string(group):
	"""
	Return a string of all the partnerships in this group (useful for debugging)
	"""
	return " ".join([f"{s0.name}-{s1.name}" for (s0,s1) in get_partnerships(group)])


def print_partnership_quality(all_students, group):
	partnerships = get_partnerships(group)

	# Keep track of how happy A and B are
	a_total_happiness = 0
	b_total_happiness = 0
	for (a, b) in partnerships:
		a_happy = a.get_rating_of_partner()
		b_happy = b.get_rating_of_partner()
		a_total_happiness += a_happy 
		b_total_happiness += b_happy
		print(f"{a.name:10}({a_happy}) {b.name:10}({b_happy})") 

	unpartnered = get_unpartnered(all_students)
	print("Unpartnered: " + ", ".join([str(s) for s in unpartnered])) 

	print(f"Group A happiness = {a_total_happiness}")
	print(f"Group B happiness = {b_total_happiness}")
	print(f"  Total happiness = {a_total_happiness + b_total_happiness}")


def print_student_information(students):
	# ** Reuse this code if you want to print students later! **
	print("\nAll students:  name (partner:satisfaction)")
	for s in students:
		print(f"\t{s} ({s.partner}:{s.get_rating_of_partner()}), ratings: {','.join(s.partner_ratings)}")

#---------------------------------------------------------------											

def load_groups(file_name=None,count=None):
	""" 
	Given a filename (to load existing data) or a count (to create new data)
	Make an array of Student instances
	"""

	# Make THREE empty lists, one for all the students, 
	#  and two for students in each group
	all_students = []
	students_a = []
	students_b = []
	lines = []

	# Is there a file? Open the file	
	if file_name != None:
		file = open(file_name, "r")
		lines = list(csv.reader(file))
	# Is there a count? Make some fake lines
	elif count != None:
		lines = construct_dataset(count)
	else:
		print("we need either a count or a file_name")
		return ()

	# For each line of data, construct students
	for line in lines:
		name = line[1]
		ratings = line[2:]

		s = Student(all_students, name, ratings)

		# Also add this student to the correct group
		if line[0] == "a":
			students_a.append(s)
		else:
			students_b.append(s)

	# Return all the students, and also the two separate groups
	return (all_students, students_a, students_b)



if __name__ == '__main__':

	#------------------------------------------------------
	# If you see "TypeError: Student() takes no arguments"
	# you haven't implemented __init__ yet

	# Create some test students, with names and rankings of prefered partners
	all_test_students = []
	s0 = Student(all_test_students, "Jason", ["Rachael", "Ryan", "Riley", "Richard"])
	s1 = Student(all_test_students, "Joy", ["Rachael", "Ryan", "Richard", "Riley"])
	s2 = Student(all_test_students, "Ryan", [ "Joy", "Jeremiah","Jason", "Jessica"])
	s3 = Student(all_test_students, "Riley", ["Jason", "Joy", "Jeremiah", "Jessica"])
	
	# Set these two as partners (not using the class method from task 6 yet)
	s0.partner = s2
	s2.partner = s0

	# Test Task 0:
	assert s0.name == "Jason", "Did you store the Student's name?"
	assert isinstance(s0.all_students, list), "Did you store all_students in the Student instance?"
	assert s0.all_students[1] == s1, "Did you add the Students to self.all_students when they are initialized?"
	assert len(all_test_students) == 4, "Did you add the Students to self.all_students when they are initialized?"

	# Test Task 1:
	assert str(s0) == "Jason", "__str__ not implemented correctly"

	# Test Task 2:
	assert s2.has_partner(), "has_partner returns False even if there is a partner"
	assert not s1.has_partner(), "has_partner returns True even if there isn't a partner"

	# Test Task 3:
	assert s2.get_rating("Jessica") == 3, "Ryan should rank Jessica as 3 (top choice!)"

	# Test Task 4:
	assert s0.get_rating_of_partner() == 1, "Jason should rank their current partner Ryan as 1 (not very good)"
	assert s1.get_rating_of_partner() == 0, "Joy doesn't have a partner, should return 0"
	
	print_student_information(all_test_students)
	
	#-----------------
	# Partner swapping

	# Test Task 5:
	s0.break_partnership()
	assert not s0.has_partner(), "Remove partnership not working"
	assert not s2.has_partner(), "Remove partnership not working. Remember to remove the partner's partner as well"

	# Test Task 6:
	# Jason partners with Riley
	s0.make_partnership(s3)
	print(f"Switch 1: {s0}-{s0.partner}, {s3}-{s3.partner}")
	assert f"{s0}-{s0.partner}, {s3}-{s3.partner}" == "Jason-Riley, Riley-Jason", "Make partnership not working"
	
	# Riley partners with Joy, breaking up with Jason
	s3.make_partnership(s1)
	print(f"Switch 2: {s1}-{s1.partner}, {s3}-{s3.partner}")
	assert not s0.has_partner(), "Remove partnership not working"
	
	# Riley partners back with Jason, breaking up with Joy
	s3.make_partnership(s0)
	print(f"Switch 3: {s0}-{s0.partner}, {s3}-{s3.partner}")
	assert not s1.has_partner(), "Remove partnership not working"
	
	print_student_information(all_test_students)

	print("Tasks 0-6 seem to be working....how can you be sure?")

	#------------------------------------------------------
	# Task 7, Task 8 and Task 9
	# No asserts, so how will you test whether it is working?
	# Print statements and logic!  
	# Print out each action/choice a student makes.
	#   Follow the logic at each step, is it correct?


	# Load data from the ratings file
	(all_test_students, students_a, students_b) = load_groups(file_name="ratings.csv")
	
	# Test Task 7
	# First we will try making pairings *without using Gale Shapeley*
	
	print("-"*40 + "\nTest 'make_partnerships' \n")
	

	# Remove any existing partnerships 
	# and set up the "potential_partners" copy of "partner _ratings"
	#  (although only gale_shapely uses the preferences,
	#   ...make_partnerships ignores preferences!) 
	[s.reset_partnerships() for s in  all_test_students]
	
	# Make the naive partnerships
	make_partnerships(students_a, students_b)

	# Print out how satisfied everyone is
	print_partnership_quality(all_test_students, students_a)
	assert students_a[0].partner == students_b[0], "a1 partner wrong"
	assert students_a[1].partner == students_b[1], "a2 partner wrong"
	assert students_a[2].partner == students_b[2], "a3 partner wrong"
	assert students_a[3].partner == students_b[3], "a4 partner wrong"
	assert students_a[4].partner == students_b[4], "a5 partner wrong"

	assert students_b[0].partner == students_a[0], "b1 partner wrong"
	assert students_b[1].partner == students_a[1], "b2 partner wrong"
	assert students_b[2].partner == students_a[2], "b3 partner wrong"
	assert students_b[3].partner == students_a[3], "b4 partner wrong"
	assert students_b[4].partner == students_a[4], "b5 partner wrong"
	

	# Test Task 8 and 9
	print("-"*40 + "\nTest 'make_gale_shapely_partnerships' \n")
	
	# Now try making pairs again 
	# ...but now with the Gale Shapeley smarter algorithm

	# Reset
	[s.reset_partnerships() for s in  all_test_students]
	
	# Make Gale-Shapeley pairings
	
	make_gale_shapely_partnerships(students_a, students_b)
	
	# Print out how satisfied everyone is
	print_partnership_quality(all_test_students, students_a)

	# How much happier is everyone with Gale Shapely?

	# Try it out with random data
	for i in range(0, 5):
		print(f"\nRandom data #{i}")
		# Uncomment this line to run with random data
		(all_test_students, students_a, students_b) = load_groups(count=5)
		[s.reset_partnerships() for s in  all_test_students]
		make_gale_shapely_partnerships(students_a, students_b)
		print_partnership_quality(all_test_students, students_a)
		
		# Notice that group A is almost always happier than group B
		# It's a stable pairing...but is it fair?

	all_test_chars_and_partner_pokemon = []
	elsa = Student(all_test_chars_and_partner_pokemon, "Elsa", ["Squirtle", "Charmander","Bulbasaur"])
	judy = Student(all_test_chars_and_partner_pokemon, "Judy", ["Charmander", "Squirtle", "Bulbasaur"])
	harry = Student(all_test_chars_and_partner_pokemon, "Harry", [ "Bulbasaur", "Squirtle", "Charmander"])

	bulbasaur = Student(all_test_chars_and_partner_pokemon, "Bulbasaur", ["Elsa", "Judy", "Harry"])
	squirtle = Student(all_test_chars_and_partner_pokemon, "Squirtle", ["Judy", "Harry", "Elsa"])
	charmander = Student(all_test_chars_and_partner_pokemon, "Charmander", ["Harry", "Elsa", "Judy"])	

	make_gale_shapely_partnerships([harry, judy, elsa], [bulbasaur, squirtle, charmander])
	assert elsa.partner == charmander, "elsa-charmander"
	assert judy.partner == bulbasaur, "judy-bulbasaur"
	assert harry.partner == squirtle, "harry-squirtle"
	assert charmander.partner == elsa, "charmander-elsa"
	assert squirtle.partner == harry, "squirtle-harry"
	assert bulbasaur.partner == judy, "bulbasaur-judy"

	make_gale_shapely_partnerships([judy, elsa, harry], [squirtle, charmander, bulbasaur])
	assert elsa.partner == charmander, "elsa-charmander"
	assert judy.partner == bulbasaur, "judy-bulbasaur"
	assert harry.partner == squirtle, "harry-squirtle"
	assert charmander.partner == elsa, "charmander-elsa"
	assert squirtle.partner == harry, "squirtle-harry"
	assert bulbasaur.partner == judy, "bulbasaur-judy"

	make_gale_shapely_partnerships([harry, elsa, judy], [charmander, bulbasaur, squirtle])
	assert elsa.partner == charmander, "elsa-charmander"
	assert judy.partner == bulbasaur, "judy-bulbasaur"
	assert harry.partner == squirtle, "harry-squirtle"
	assert charmander.partner == elsa, "charmander-elsa"
	assert squirtle.partner == harry, "squirtle-harry"
	assert bulbasaur.partner == judy, "bulbasaur-judy"
	#------------------------------------------------------
	# Run an experiment
	# How long does Gale Shapeley take to run?

	def run_experiment(trials_count=10):
		# Running an experiment
		# What is the O(N) of this algorithm?
		# As the number of students goes up, how does the number of rounds change?
		# This can take a long time to run on some machines, 
		# ....watch it until you see what is going on

		print("Time to run Gale-Shapely for N students")
		for i in range(1, 50):

			# How many students?
			student_count = 10*i
			
			# Start the performance counter (like a stopwatch for Python)
			start = time.perf_counter()

			# Run some number of trials (since its random data, some iterations 
			# will be solvable faster or slower than others)
			for j in range(0, trials_count):
				# Make fake data for a *large* number of students
				(_, students_a, students_b) = load_groups(count=student_count)
				# Make the partnerships
				make_gale_shapely_partnerships(students_a, students_b)
			
			# End the performance counter
			end = time.perf_counter()

			# How long did each test take?
			avg_time = (end - start)/trials_count
			bar = "■"*round(400*avg_time)
			print(f"\t{student_count:4}: {avg_time:.2f}ms {bar}")

	#----------------------------------------------------------------		
	# Run this experiment
	# You can reduce the trials_count if your computer is slow
	# Or increase it if you want more precision

	#run_experiment(trials_count=5)
