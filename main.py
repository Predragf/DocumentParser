from classes.FileParser import FileParser
from classes.DirExplorer import DirExplorer
from classes.PageParseResult import PageParseResult
from classes.PageLinksChecked import PageLinksChecked
import urllib2
import os.path


def main():
	explorer = DirExplorer()
	#put the root directory where the files need to be checked
	rootDir = os.getcwd()
	filesForProcess = explorer.getFilesForProcessing(rootDir)
	for fileForProcess in filesForProcess:
		print fileForProcess
		parseRes = FileParser.ParseFile(fileForProcess)
		pagesLinksChecked = PageLinksChecked(parseRes)
		pagesLinksChecked.CheckLinks()
		for lnk in pagesLinksChecked.links:
			print lnk.linkName
			print lnk.statusCode
			print '------------------------'
		print 'total links {0} and links not working {1}'.format(len(pagesLinksChecked.links), pagesLinksChecked.totalInvalidLinks)


main()

	