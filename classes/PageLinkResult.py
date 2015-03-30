class PageLinkResult():
	"""Class without functionality used as a structure for storing PageLinks. The page link has name and a status code."""
	linkName = ''
	statusCode = 0
	def __init__(self, lnkName, stCode):
		self.linkName = lnkName
		self.statusCode = stCode

		