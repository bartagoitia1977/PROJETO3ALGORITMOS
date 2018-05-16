class Trie_Knot:
	def __init__(self,item = None):
		self.item = item
		self.zero = None
		self.um = None
		self.dois = None
		self.tres = None
		self.quatro = None
		self.cinco = None
		self.seis = None
		self.sete = None
		self.oito = None
		self.nove = None
		
	def pointer(self,digit):
		self.digit = digit
		if (self.digit == "0"):
			self.zero = self.digit
		if (self.digit == "1"):
			self.um = self.digit
		if (self.digit == "2"):
			self.dois = self.digit
		if (self.digit == "3"):
			self.tres = self.digit
		if (self.digit == "4"):
			self.quatro = self.digit
		if (self.digit == "5"):
			self.cinco = self.digit
		if (self.digit == "6"):
			self.seis = self.digit
		if (self.digit == "7"):
			self.sete = self.digit
		if (self.digit == "8"):
			self.oito = self.digit
		if (self.digit == "9"):
			self.nove = self.digit
		
class Indice:
	def __init__(self):
		self.__foot = Trie_Knot()		
		
	def arvore_vazia(self):
		self.__foot = Trie_Knot()
		
	def inserirItem(self,chave):
		self.__chave = chave
		for digit in self.__chave:
			self.__foot.Trie_Knot.pointer(digit) = Trie_Knot(digit)
			self.__foot = self.__foot.__foot
			
	def pesquisarItem(self,chave):
		self.__chave = chave
		self.__chave = None + self.__chave
		for digit in self.__chave:
			
			
			
		
			
			