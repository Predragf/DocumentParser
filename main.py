from classes.FileParser import FileParser
from classes.DirExplorer import DirExplorer
from classes.PageParseResult import PageParseResult
from classes.PagesLinksChecker import PagesLinksChecker
import urllib2
import os.path


def main():
	_cache = {}
	explorer = DirExplorer()
	#put the root directory where the files need to be checked
	rootDir = os.getcwd()
	filesForProcess = explorer.getFilesForProcessing(rootDir)
	for fileForProcess in filesForProcess:

		print 'Processing file: {0}'.format(fileForProcess)
		parseRes = FileParser.ParseFile(fileForProcess)
		pagesLinksChecked = PagesLinksChecker(parseRes)
		pagesLinksChecked.CheckLinks(_cache)
		
		for lnk in pagesLinksChecked.links:
			print lnk.linkName
			print lnk.statusCode
			print '------------------------'
		print 'total links {0} and links not working {1}'.format(len(pagesLinksChecked.links), pagesLinksChecked.totalInvalidLinks)
		print _cache


main()

	