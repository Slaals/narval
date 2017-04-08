'''
	This file is part of Narval :
	an opensource and free rights static blog generator.
'''

#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re, os

############################### HELPERS #######################################

def convertBlogVars(blogUrl, content):
	path = blogUrl + '/'
	regex = r"{blog:(.*?):(.*?)}"
	allVars = re.findall(regex, content)
	for v in allVars:
		if v[0] == 'post':
			url = 'posts/'
		elif v[0] == 'page':
			url = 'pages/'
		if url :
			listing = os.listdir(url)
			for infile in listing:
				fileNum = int(infile.split('.')[0])
				if fileNum == int(v[1]):
					with open(os.path.join(url, infile), 'r') as postOrPage:
						while 1:
							line = postOrPage.readline().rstrip('\n\r')
							lineElts = line.split()
							if lineElts[0] == 'title':
								title = ' '.join(lineElts[2:])
								if v[0] == 'post':
									url += niceURL(title, '.html')
								elif v[0] == 'page':
									url = niceURL(title, '.html')
								content = re.sub(regex, path + url, content, 1)
								url = ''
								break
	return content

def dateLitteral(dateNum):
	m = ('', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre')
	num = dateNum.split('/')
	return num[0] + ' ' + m[int(num[1])] + ' ' + num[2]

def niceURL(title, suffix=''):
	result = re.sub("<.*?>", "", title)
	result = re.sub("&.*?;", "", result)
	result = re.sub("/", "sur", result)
	result = re.sub("[^0-9a-zA-ZÀÉÈÙàéèêëùîô]+", "-", result).lower()
	result = re.sub("^-", "", result)
	result = re.sub("-$", "", result)
	return result + suffix

def getHead(params, helpers, tmps, path='', head={}): # used on all pages
	if head=={}:
		head['title'] = ''
		head['author'] = params.blogDefaultAuthor
		head['desc'] = params.blogSubTitle

	url, separator = '', ''
	if head['title'] != '':
		url = 'posts/' + helpers.niceURL(head['title'], '.html')
		separator = ' — '
	if head['desc'] == '':
		head['desc'] = params.blogSubTitle
	fullUrl = params.blogUrl + '/' + url

	data = (
		helpers.cleanhtml(head['title'] + separator + params.blogTitle),
		head['author'],
		path,
		params.blogTitle,
		fullUrl,
		helpers.cleanhtml(head['desc'])
	)

	return tmps.TMP_head(data), fullUrl

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext
