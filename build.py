'''
	This file is part of Narval :
	an opensource and free rights static blog generator.
'''

#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os, filecmp, random, webbrowser
from shutil import copyfile
params = __import__('config')
helpers = __import__('helpers')
tmps = __import__('template')


def build(params, helpers, tmps, isLocal=False):

	if isLocal == True:
		params.folder = params.folder + '-local'
		params.blogUrl = os.path.abspath('') + '/' + params.folder

	pathPosts, pathPages, myPosts, myPages, nbPosts, catsList = 'posts/', 'pages/', [], [], 0, []

	### Build vars (categories, myPosts, myPages) using the source files

	# posts folder
	listing = os.listdir(pathPosts)
	for infile in listing:
		fileNum = int(infile.split('.')[0])
		with open(os.path.join(pathPosts, infile), 'r') as post:
			myPost = {'title': '', 'date': '', 'cats': '', 'intro': '', 'desc': '', 'author': '', 'content': '', 'id': fileNum, 'titleHead': '', 'thumb': ''}
			while 1:
				line = post.readline().rstrip('\n\r')
				if line != '---':
					lineElts = line.split()
					if lineElts[0] == 'title': myPost['title'] = ' '.join(lineElts[2:])
					elif lineElts[0] == 'date': myPost['date'] = ' '.join(lineElts[2:])
					elif lineElts[0] == 'cats': myPost['cats'] = ' '.join(lineElts[2:]).split('+')
					elif lineElts[0] == 'intro': myPost['intro'] = ' '.join(lineElts[2:])
					elif lineElts[0] == 'author': myPost['author'] = ' '.join(lineElts[2:])
					elif lineElts[0] == 'desc': myPost['desc'] = ' '.join(lineElts[2:])
					elif lineElts[0] == 'thumb': myPost['thumb'] = ' '.join(lineElts[2:])
				else:
					break

			myPost['content'] = post.read()
			myPosts.append(myPost)
			for cat in myPost['cats']: catsList.append(cat)

	myPosts = sorted(myPosts, key=lambda k: k['id'], reverse=True)

	catsList = sorted(set(catsList))
	catsList2 = []
	for cat in catsList: catsList2.append({"name": cat, "path": helpers.niceURL(cat, '/')})
	categories = tuple(catsList2)

	for post in myPosts:
		myList = []
		for cat in post['cats']:
			match = next((c for c in categories if c['name'] == cat), None)
			myList.append(match)
		post['cats'] = tuple(myList)

	# pages folder
	listing = os.listdir(pathPages)
	for infile in listing:
		with open(os.path.join(pathPages, infile), 'r') as page:
			myPage = {'title': '', 'desc': '', 'content': ''}
			while 1:
				line = page.readline().rstrip('\n\r')
				if line != '---':
					lineElts = line.split()
					if lineElts[0] == 'title': myPage['title'] = ' '.join(lineElts[2:])
					elif lineElts[0] == 'desc': myPage['desc'] = ' '.join(lineElts[2:])
				else:
					break
			myPage['content'] = page.read()
			myPages.append(myPage)


	header = tmps.TMP_header(params, helpers, tmps, categories, myPages, 0) #0 pour une liste
	footer = tmps.TMP_footer(params, helpers, tmps)

	### Build tree (folders & files)

	def copyFolderFiles(src, dest): # source folder, destination folder
		srcFiles = os.listdir(src) # all files in source folder
		for srcFile in srcFiles:
			if os.path.isfile(dest + srcFile) == True:
				# exists
				if filecmp.cmp(src + srcFile, dest + srcFile) == False:
					# not same files
					copyfile(src + srcFile, dest + srcFile)
			else:
				# not exists
				copyfile(src + srcFile, dest + srcFile)
		# clean folder (remove all files who isn't in source folder)
		destFiles = os.listdir(dest)
		for destFile in destFiles:
			if os.path.isfile(src + destFile) == False:
				os.remove(dest + destFile)

	# si le dossier du blog généré n'existe pas, on le crée
	if os.path.isdir(params.folder) == False: os.mkdir(params.folder)
	if os.path.isdir(params.folder + '/posts') == False: os.mkdir(params.folder + '/posts')
	if os.path.isdir(params.folder + '/theme') == False: os.mkdir(params.folder + '/theme')
	if os.path.isdir(params.folder + '/cats') == False: os.mkdir(params.folder + '/cats')
	if os.path.isdir(params.folder + '/medias') == False: os.mkdir(params.folder + '/medias')
	if os.path.isdir(params.folder + '/thumbs') == False: os.mkdir(params.folder + '/thumbs')

	with open(params.folder + '/RSSfeed.xml', 'w') as rssRender:
		rssRender.write(tmps.TMP_rss(params, helpers, tmps, myPosts))

	with open(params.folder + '/README.md', 'w') as rmRender:
		rmRender.write(tmps.TMP_readme(params, helpers, tmps, myPosts))

	copyFolderFiles('theme/', params.folder + '/theme/')
	copyFolderFiles('medias/', params.folder + '/medias/')
	copyFolderFiles('thumbs/', params.folder + '/thumbs/')
	copyfile('favicon.ico', params.folder + '/favicon.ico')
	copyfile('ui.js', params.folder + '/ui.js')

	for categorie in categories:
		path = params.folder + '/cats/' + categorie['path']
		if os.path.isdir(path) == False: os.mkdir(path)
		myPostsFiltred = []
		for post in myPosts:
			if categorie in post['cats']: myPostsFiltred.append(post)
		array = [myPostsFiltred[i:i+params.blogNbPostsByPage] for i in range(0, len(myPostsFiltred), params.blogNbPostsByPage)]
		i, nbLots = 1, len(array)
		for lot in array:
			result = tmps.TMP_posts(params, helpers, tmps, categorie['name'], header, footer, lot, (i, nbLots), '../../')
			if i == 1:
				with open(path + 'index.html', 'w') as r: r.write(result)
				with open(path + 'page1.html', 'w') as r: r.write(result)
			else:
				with open(path + 'page' + str(i) + '.html', 'w') as r: r.write(result)
			i += 1

	array = [myPosts[i:i+params.blogNbPostsByPage] for i in range(0, len(myPosts), params.blogNbPostsByPage)]
	i = 1
	nbLots = len(array)
	for lot in array:
		if i == 1:
			result = tmps.TMP_posts(params, helpers, tmps, '', header, footer, lot, (i, nbLots))
			with open(params.folder + '/index.html', 'w') as r: r.write(result)
			with open(params.folder + '/page1.html', 'w') as r: r.write(result)
		else:
			with open(params.folder + '/page' + str(i) + '.html', 'w') as r:
				r.write(tmps.TMP_posts(params, helpers, tmps, '', header, footer, lot, (i, nbLots)))
		i += 1

	header = tmps.TMP_header(params, helpers, tmps, categories, myPages, 1) #1 pour un post ou une page

	for post in myPosts:
		with open(params.folder + '/posts/' + helpers.niceURL(post['title'], '.html'), 'w') as r:
			r.write(tmps.TMP_post(params, helpers, tmps, header, post, footer))

	for page in myPages:
		with open(params.folder + '/' + helpers.niceURL(page['title'], '.html'), 'w') as r:
			r.write(tmps.TMP_page(params, helpers, tmps, header, page, footer))

build(params, helpers, tmps)
build(params, helpers, tmps, True)

exprs = [
	'Nom d\'une corne !',
	'Bien joué !', 'Bravo !', 'Hihihi !', 'Félicitations !',
	'La corne du narval est une dent !',
	'Les femelles narval, sauf exceptions, n\'ont pas de corne.',
	'Une corne de narval peut mesurer 3 mètres !',
	'Une corne de narval peut peser jusqu\'à 10 kg !',
	'Le narval vivrait en moyenne une cinquantaine d\'années.',
	'Le narval est un cétacé à dents.',
	'Outre l\'humain, le narval a 2 prédateurs : l\'orque et l\'ours polaire.',
	'Le narval raffole des flétans, des raies et des morues.',
	'Le narval peut descendre à 1500 mètres de profondeur.',
	'Le narval peut rester en apnée près d\'une demi heure.'
]

print('\033[92m>>> ' + random.choice(exprs) + '\033[0m')
resp = input('Le blog est consultable hors ligne dans "' + params.folder + '".\nVoir dans un navigateur ? (O/n)').lower()
if resp != 'n':
	webbrowser.open(params.folder + '/index.html', new=2)
