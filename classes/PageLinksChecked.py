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

	def CheckLinks(self, _cache):
		"""Function that iterates though all the links extracted from the document and checks the status. """
		for lnk in self.links:
			try:
				#here cache first needs to be implemented. Implement hash using dictionary
				rCode = _cache.get(lnk.linkName)
				if rCode is None:
					print 'cache miss'
					rCode = urllib2.urlopen(lnk.linkName).code
					_cache[lnk.linkName] = rCode
				else:
					print 'cache hit'

				lnk.statusCode = rCode					
				if(str(lnk.statusCode).startswith('4') or str(lnk.statusCode).startswith('5')):
					self.totalInvalidLinks = self.totalInvalidLinks + 1
			except urllib2.URLError:
				print 'timeout {0}'.format(lnk.linkName)
				_cache[lnk.linkName] = '408'
			except:
				self.totalInvalidLinks = self.totalInvalidLinks + 1
				

		