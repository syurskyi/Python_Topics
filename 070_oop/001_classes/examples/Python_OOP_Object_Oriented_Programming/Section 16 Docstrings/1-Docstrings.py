class Flight:
        
	def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
		self.number = number
		self.origin = origin
		self.destination = destination
		self.num_passengers = num_passengers
		self._total_weight = total_weight
		self._pilot = pilot 
		self._crew = crew

	@property
	def total_weight(self):
		return self._total_weight

	@total_weight.setter
	def total_weight(self, weight):
		if weight > 0 and isinstance(weight, float):
			self._total_weight = weight	

	@property
	def pilot(self):
		return self._pilot

	@pilot.setter
	def pilot(self, new_pilot):
		self._pilot = pilot

	@property
	def crew(self):
		return self._crew
	
	@crew.setter
	def crew(self, new_crew):
		self._crew = new_crew

	def display_flight_data(self):
		print("== Flight ==")
		print("Number:", self.number)
		print("Number of Passengers:", self.num_passengers)
		print("Weight:", self.weight)
		print("Pilot:", self._pilot)
		print("Crew:", self._crew)
