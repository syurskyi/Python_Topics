class Player:
	def __init__(self, username, rank, time_played, id_num):
		self.username = username
		self._rank = rank
		self.__time_played = time_played
		self.__id_num = id_num
