from classes.PageParseResult import PageParseResult
from classes.PageLinkResult import PageLinkResult
import httplib
from urlparse import urlparse

class PagesLinksChecker():
	"""Class that iterates though all the links extracted from the document and checks the status."""
	fileName = ''
	links = []
	totalInvalidLinks = 0
	def __init__(self, pageParseResult):
		self.fileName = pageParseResult.document
		for lnk in pageParseResult.documentLinks:
			#999 is default value for status of the link
			self.links.append(PageLinkResult(lnk, 999))

	def GetLinkStatusCode(self, _url, _cache):
		#the request is implemented using httplib to request only the header for optimization
		try:
			parsedUrl = urlparse(_url)
			rCode = _cache.get(_url)
			if rCode is None:
				conn = httplib.HTTPConnection(parsedUrl.netloc)
				conn.request('HEAD', parsedUrl.path)
				rCode = conn.getresponse().status
				_cache[_url] = rCode
		
		except Exception as e:
			print e
			rCode = '408'
			_cache[_url] = rCode
		finally:
			return rCode

	def CheckLinks(self, _cache):
		"""Function that iterates though all the links extracted from the document and checks the status. """
		for lnk in self.links:
			lnk.statusCode = self.GetLinkStatusCode(lnk.linkName, _cache)
			#we account status codes 4xx and 5xx to be invalid
			if(lnk.statusCode >= 400):
				self.totalInvalidLinks = self.totalInvalidLinks + 1
				

		