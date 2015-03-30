import os.path
from classes.FileParser import FileParser

class DirExplorer:
	"""Provides a functinoality of finding all the .html, .htm and .php files on the file system begining from the root directory"""

	def getFilesForProcessing(self, rootPath):
		""" Find and return all the relevant files in the root and all of its subdirectories """
		filesForProcessing = []
		subDirsForProcessing = []
		items = os.listdir(rootPath)
		for itm in items:
			absItemPath = os.path.abspath(itm)
			if os.path.isdir(absItemPath):
				print 'directory found {0}'.format(absItemPath)
				subDirsForProcessing.append(absItemPath)
			elif os.path.isfile(absItemPath):
				if not(self.isRelevantFile(absItemPath)):
					continue
				else:
					#write parsing function
					print 'file found found {0}'.format(absItemPath)
					filesForProcessing.append(absItemPath)
		for subDir in subDirsForProcessing:
			filesForProcessing.extend(self.getFilesForProcessing(subDir))

		return filesForProcessing
			

	def isRelevantFile(self, filename):
		""" check if the file is of interest. Current files of interest .html, .htm, .php"""
		if filename.endswith('html') or filename.endswith('htm') or filename.endswith('.php'):
			return True
		else:
			return False
		
