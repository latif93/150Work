import random



def construct_dataset(count):
	"""
	Create a dataset of students and their preferences 

	Parameters:
		count(int): the number of student-pairs to create
	Returns: 
		list: A list of data rows [group_id, name, ...preferences]
	"""
	
	surname = [ "Chao", "Fillmore", "Freeman", "Quincy", "Quigley", "Bannister", "García", "Ginsburg", "Kuhn", "Khan", "La Fontaine", "Friedman", "Schmidt", "St. Ives", "Gabor", "Cherenkov", "Jensen", "Dalén", "Luther", "Powell", "Thompson", "Stern", "Richardson", "Raman", "Martin", "St. James", "Grey", "O'Reilly", "MacDuff", "McGregor", "Bradshaw", "Hoover", "Goldman", "Wells", "Watson", "Goldsmith", "Poe", "Yarrow", "Irving", "Buckley", "Tang", "Bond", "Wong", "Wei", "Goldsmith", "Tran", "Chu", "Baudin", "Montagne", "Green", "Porter", "Moulin", "Villeneuve", "Victor", "Rodríguez", "Smith", "Johnson", "Williams", "Miller", "Stockton", "Patel", "Chaudri", "Jahan", "Christiansen", "Jones", "Stein", "Hirviniemi", "Hampton", "Kiuru", "Ovregard", "Singh", "Noriega", "Pine", "Clarion", "Belden", "Jaware", "Keita", "Kanu", "Geary", "Norton", "Kearny", "Aliyev", "Sato", "Tanaka", "Kim", "Lee", "Gray", "Yang", "Li", "Çelik", "Davis", "Knox", "Griffin", "Leon", "Finch", "Yoo", "Gupta", "Flores", "Lopez", "Moon", "Sun", "Castro", "Suzuki", "Torres", "Pineda", "Tsao", "Romero", "Wolf"]

	a_names = ["Amelia", "Anna", "Avery", "Abby", "Alastair", "Ahmed", "Allen", "Ali", "Antonia", "Agatha", "Augustine", "Amy", "Addison", "Atticus", "Adelle", "Alfred", "Aphrodite", "Alphonso", "Alex", "Allie", "Allegria", "April", "Ada"]
	b_names = ["Biyu", "Bailey", "Beverly", "Bob", "Brian", "Bintou", "Bruno", "Brandon", "Bridget", "Bertie", "Beatrice", "Bruce", "Buffy", "Billy", "Bryce", "Blake", "Ben", "Belle", "Britney", "Boone", "Buddy"]
	

	if count < len(b_names):
		random.shuffle(a_names)
		random.shuffle(b_names)
		a_names = a_names[0:count]
		b_names = b_names[0:count]
	else:
		# Need to make duplicate names
		a_names2 = []
		b_names2 = []
		for i in range(0,count//20 + 1):
			a_names2 += [f"{name}{i}" for name in a_names]	
			b_names2 += [f"{name}{i}" for name in b_names]	


		a_names = a_names2[0:count]
		b_names = b_names2[0:count]


	# Create a shuffled copy
	def copy_shuffle(arr):
		arr1 = [a for a in arr]
		random.shuffle(arr)
		return arr
	
	students_a = [["a", name] + copy_shuffle(b_names) for name in a_names]
	students_b = [["b", name] + copy_shuffle(a_names) for name in b_names]
	
	return students_a + students_b
