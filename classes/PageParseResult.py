class PageParseResult():
	"""Structure class that contains the name of the file and a list of all the links found within. """
	document = ''
	documentLinks = []
	
	def __init__(self, htmlFile, pageLinks):
		self.document = htmlFile
		self.documentLinks = pageLinks

		