class Trie_Knot():
	def __init__(self,item = None,chave = None):
		self.item = item
		self.chave = chave
		self.pointer = [None] * 10
		self.mark = False
		
class Indice():
	def __init__(self):
		self.root = Trie_Knot()

	def inserirItem(self,item,chave):
		knot = self.root
		for digit in chave:
			if (knot.pointer[int(digit)] is None):
				knot.pointer[int(digit)] = Trie_Knot(None, digit)
				knot = knot.pointer[int(digit)]
			else:
				knot = knot.pointer[int(digit)]
		knot.item = item
		knot.mark = True
	
	def pesquisar(self,chave):
		knot_pesquisa = self.root
		for digit in chave:
			if (knot_pesquisa.pointer[int(digit)] is None):
				raise KeyError
			else:
				knot_pesquisa = knot_pesquisa.pointer[int(None,digit)]
		if (knot_pesquisa.mark == True):
			return knot_pesquisa.item
		else:
			raise KeyError
	
	def __getitem__(self,chave):
		return self.pesquisar(chave)
    
    def __setitem__(self,item,chave):
        inserirItem(item,chave)
