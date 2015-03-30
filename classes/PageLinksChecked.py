from classes.PageParseResult import PageParseResult
from classes.PageLinkResult import PageLinkResult
import urllib2

class PageLinksChecked():
	"""Class that iterates though all the links extracted from the document and checks the status."""
	fileName = ''
	links = []
	totalInvalidLinks = 0
	def __init__(self, pageParseResult):
		self.fileName = pageParseResult.document
		for lnk in pageParseResult.documentLinks:
			#999 is default value for status of the link
			self.links.append(PageLinkResult(lnk, 999))

	def CheckLinks(self):
		"""Function that iterates though all the links extracted from the document and checks the status. """
		for lnk in self.links:
			try:
				response = urllib2.urlopen(lnk.linkName)
				lnk.statusCode = response.code
				if(str(lnk.statusCode).startswith('4') or str(lnk.statusCode).startswith('5')):
					self.totalInvalidLinks = self.totalInvalidLinks + 1
			except:
				self.totalInvalidLinks = self.totalInvalidLinks + 1

		