class Trie_Knot:
	def __init__(self,item = None,chave = None):
		self.__item = item
		self.__chave = chave
		self.__pointer = [None] * 10
		self.__mark = False
		
class Indice:
	def __init__(self):
		self.__root = Trie_Knot()		
		
	def inserirItem(self,item,chave):
		self.__chave = chave
		self.__item = item
		for digit in self.__chave:
			self.__root = Trie_Knot()						
			
	def pesquisarItem(self,chave):
		self.__chave = chave
		self.__chave = None + self.__chave
		for digit in self.__chave:
			
			
			
		
			
			