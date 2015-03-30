from bs4 import BeautifulSoup
from classes.PageParseResult import PageParseResult

class FileParser(object):
	"""Class that parses files."""
	__baseUrl = 'http://www.es.mdh.se/'

	@staticmethod
	def readFile(filePath):
		"""Function that reads file from a disk. Accepts absolute path to the file and returns its contents. """
		openedFile = open(filePath)
		return openedFile.read()


	@staticmethod
	#the file should be updated 
	def extractAllLinks(fileContents):
		"""Function that extracts all links from a file. Input parameter is the contents of a file. """
		links = []
		bsObject = BeautifulSoup(fileContents)
		for link in bsObject.find_all('a'):
			#this is okay for absolute URLs. What to do with relative? Append baseURL or simply ignore?
			links.append(link.get('href'))
		return links


	@staticmethod
	def ParseFile(fileName):
		"""Public function of the FiLeParser class that provides the functionality of finding all hyperlinks within a given file.
		returns result of type PageParseResult."""
		print 'parsing file: {0}'.format(fileName)
		parseResult = PageParseResult(fileName, FileParser.extractAllLinks(FileParser.readFile(fileName)))
		return parseResult

		