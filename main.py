nested_list = [
	['a', 'b', 'c'],
	['3', 4],
	[1, 2, 'can'],
	['d', 'e', 'f'],
	[1, 2, None],
	[1],
	[2, 3, 'rewrewr', 3, 4, 432, 5435],
]

class FlatIterator:

	def __init__(self, nested_list):
		self.nested_list = nested_list

	def __iter__(self):
		self.external_counter = 0
		self.external_counter_max = len(nested_list)
		self.counter_internal = -1
		self.counter_internal_max = len(nested_list[self.external_counter])
		return self

	def __next__(self):
		self.counter_internal += 1
		if self.counter_internal == self.counter_internal_max:
			self.external_counter += 1
			if self.external_counter == self.external_counter_max:
				raise StopIteration
			self.counter_internal = 0
			self.counter_internal_max = len(nested_list[self.external_counter])

		return self.nested_list[self.external_counter][self.counter_internal]



for item in FlatIterator(nested_list):
	print(item) #  