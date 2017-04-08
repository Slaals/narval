'''
	This file is part of Narval :
	an opensource and free rights static blog generator.
'''

#!/usr/bin/python3
#-*- coding: utf-8 -*-

import time

### PARTS OF TEMPLATES

# between <head> and </head> (<head> and </head> includes)
def TMP_head(data):
	"""
		data = (
			0: titre de la page,    1: auteur du post,  2: chemin pour être à la racine du blog,
			3: titre de blog,       4: URL complète,    5: description de la page
		)
	"""
	return '''
		<head>
			<meta charset=utf-8 />
			<title>''' + data[0] + '''</title>
			<meta name=author content=''' + data[1] + ''' />
			<meta name=viewport content="width=device-width, initial-scale=1" />
			<link href="''' + data[2] + '''RSSfeed.xml" rel="alternate" type="application/rss+xml" title="Nouveautés sur ''' + data[3] + '''" />
			<link rel=canonical href="''' + data[4] + '''" />
			<link rel=icon href="''' + data[2] + '''favicon.ico" />
			<link rel=stylesheet type='text/css' href="''' + data[2] + '''theme/base.css" media=screen />
			<link id=theme rel=stylesheet type='text/css' href="''' + data[2] + '''theme/dark.css" media=screen />
			<link rel=stylesheet href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:700" />
			<meta name=description content="''' + data[5] + '''" />
		</head>'''

# in <body></body>, page header
def TMP_header(params, helpers, tmps, categories, myPages, typePage):
	# construction du menu des catégories
	c = ''
	if len(categories)>0:
		c = '<li class=menu>Catégories&nbsp;<span class=menuIndicator>»</span><ul class=submenu>'
	for cat in categories:
		c += '''<li><a href="''' + params.blogUrl + '''/cats/''' + cat['path'] + '''index.html">''' + cat['name'] + '''</a></li>'''
	if len(categories) > 0:
		c += '</ul></li>'

	# construction du menu des pages
	p = ''
	if len(myPages) > 0:
		p = '<li class=menu>Pages&nbsp;<span class=menuIndicator>»</span><ul class=submenu>'
	for page in myPages:
		p += '''<li><a href="''' + params.blogUrl + '''/''' + helpers.niceURL(page['title']) + '''.html">''' + page['title'] + '''</a></li>'''
	if len(myPages) > 0:
		p += '</ul></li>'

	if params.blogUrl[0:3] == 'http':
		url = params.blogUrl
	else:
		url = params.blogUrl + '/index.html'

	if typePage == 1:
		return '''
			<header>
				<div class=accroche1><span style="font-size:1.2em;">''' + params.blogTitle + '''</span> — ''' + params.blogSubTitle + '''</div>
				<nav style='margin-bottom:0px;'>
					<ul>
						<li><a href="''' + url + '''">Accueil</a></li>
						''' + c + p + '''
						<li><a type="application/rss+xml" href="''' + params.blogUrl + '''/RSSfeed.xml">RSS</a></li>
					</ul>
				</nav>
			</header>'''

	return '''
		<header>
			<div class=accroche>''' + params.blogSubTitle + '''</div>
			<h1>''' + params.blogTitle + '''</h1>
			<nav>
				<ul>
					<li><a href="''' + url + '''">Accueil</a></li>
					''' + c + p + '''
					<li><a type="application/rss+xml" href="''' + params.blogUrl + '''/RSSfeed.xml">RSS</a></li>
				</ul>
			</nav>
		</header>'''

# in <body></body>, page footer
def TMP_footer(params, helpers, tmps):
	# data = URL du blog
	return '''
		<footer id=footer>
			2017 – Blog de ''' + params.blogDefaultAuthor + '''.<br>
			Le contenu de ce blog est mis à disposition sous différentes licences<br>
			détaillées <a href="''' + helpers.convertBlogVars(params.blogUrl, "{blog:page:1}#droits") + '''">ici</a>.
		</footer>'''

# in <body></body>, olds and recents posts
def TMP_paginator(pagination):
	# pagination = (0: numéro de page, 1: total de page)
	page, total = pagination[0], pagination[1]
	html = '<div class=pagination>Page ' + str(page) + '/' + str(total) + '.'
	if total > 1:
		html += '<br>'
	if page < total:
		html += '<a href="page' + str(page + 1) + '.html">←&nbsp;Anciens&nbsp;articles</a>'
	if page > 1:
		html += '<a href="page' + str(page - 1) + '.html">Articles&nbsp;récents&nbsp;→</a>'
	return html + '</div>'

# in <body></body>, textual line of categories
def TMP_catsLine(params, helpers, tmps, cats):
	html, i, nb = '', 0, len(cats)
	for cat in cats:
		html += '<a href="' + params.blogUrl + '/cats/' + cat['path'] + 'index.html">' + cat['name'] + '</a>'
		i = i + 1
		if i < nb - 1: html += ', '
		elif i < nb: html += ' et '
	return html


### FULL TEMPLATES

def TMP_posts(params, helpers, tmps, catName, header, footer, posts, pagination, path=''):
	p = ''
	txtCat = ''
	for post in posts:
		if post['author'] == '': author = ''
		else: author = ' (par ' + post['author'] + ')'
		if catName == 'Cat 2':
			p += '''
				<article class=thumb>
					<a href="''' + params.blogUrl + '''/posts/''' + helpers.niceURL(post['title'], '.html') + '''">
						<img src="''' + params.blogUrl + '''/thumbs/''' + post['thumb'] + '''" alt="Image principale de l'article">
					</a>
					<div class=caption>
						<a href="''' + params.blogUrl + '''/posts/''' + helpers.niceURL(post['title'], '.html') + '''">''' + post['title'] + '''</a>
					</div>
				</article>'''
		else:
			postIntro = post['intro']
			if postIntro != '':
				postIntro = '''
					<div class=postIntro>
						''' + postIntro + '''
					</div>'''
			p += '''
				<article>
					<h2 class=postTitle><a href="''' + params.blogUrl + '''/posts/''' + helpers.niceURL(post['title'], '.html') + '''">''' + post['title'] + '''</a></h2>
					<p class=postInfos>Le ''' + helpers.dateLitteral(post['date']) + ''' dans ''' + tmps.TMP_catsLine(params, helpers, tmps, post['cats']) + author + '''.</p>
					''' + postIntro + '''
				</article>'''

	if catName != '':
		txtCat = '<p><strong>' + catName + '</strong>'
		for cat in params.catsList:
			if cat["name"] == catName:
				txtCat += '&nbsp;: ' + cat["desc"]
		txtCat += '</p><hr>'

	return '''
	<!DOCTYPE html>
	<html lang=fr>
		''' + helpers.getHead(params, helpers, tmps, path)[0] + '''
		<body><div class=page>
			''' + header + txtCat + p + tmps.TMP_paginator(pagination) + footer + '''
		</div></body>
		<script src="''' + params.blogUrl + '''/ui.js"></script>
	</html>'''

def TMP_post(params, helpers, tmps, header, post, footer):
	head = {'desc': post['intro']}
	if post['author'] == '':
		head['author'] = params.blogDefaultAuthor
		author = ''
	else:
		head['author'] = post['author']
		author = ' (par ' + post['author'] + ')'
	if post['titleHead'] == '':
		head['title'] = post['title']
	else:
		head['title'] = post['titleHead']
	resultHead = helpers.getHead(params, helpers, tmps, '../', head)

	if params.blogUrl[0:3] == 'http':
		url = params.blogUrl
	else:
		url = params.blogUrl + '/index.html'

	return '''
		<!DOCTYPE html>
		<html lang="fr">
			''' + resultHead[0] + '''
			<body><div class='page onlyPost'>
				''' + header + '''
				<article>
					<h1 class=postTitle>''' + post['title'] + '''</h1>
					<p class=postInfos>Le ''' + helpers.dateLitteral(post['date']) + ' dans ' + tmps.TMP_catsLine(params, helpers, tmps, post['cats']) + author + '''.</p>
					<div class=postIntro>''' + post['intro'] + '''</div>
					<div class=postContent>''' + helpers.convertBlogVars(params.blogUrl, post['content']) + '''</div>
				</article>
				<div class=comments>
					<p>Il est possible de <strong>commenter cette publication</strong> en écrivant un courriel à l’adresse mentionnée sur la page "À propos" (rubrique "Me contacter").</p>
				</div>

				<a class=btNav href="''' + url + '''">←&nbsp;Accueil</a>
				''' + footer + '''
			</div></body>
			<script src="''' + params.blogUrl + '''/ui.js"></script>
		</html>'''

def TMP_page(params, helpers, tmps, header, page, footer):
	head = {'title': page['title'], 'desc': page['desc'], 'author': params.blogDefaultAuthor}
	resultHead = helpers.getHead(params, helpers, tmps, '', head)

	if params.blogUrl[0:3] == 'http':
		url = params.blogUrl
	else:
		url = params.blogUrl + '/index.html'

	return '''
		<!DOCTYPE html>
		<html lang="fr">
			''' + resultHead[0] + '''
			<body>
				<div class='page onlyPost'>
					''' + header + '''
					<article>
						<h1 class=postTitle>''' + page['title'] + '''</h1>
						<div class=postContent>''' + helpers.convertBlogVars(params.blogUrl, page['content']) + '''</div>
					</article>
					<a class=btNav href="''' + url + '''">←&nbsp;Accueil</a>
					''' + footer + '''
				</div>
			</body>
			<script src="''' + params.blogUrl + '''/ui.js"></script>
		</html>'''

def TMP_rss(params, helpers, tmps, myPosts):
	items = ''
	for p in myPosts:
		items += '''<item>
			<title>''' + helpers.cleanhtml(p['title']) + '''</title>
			<link>''' + params.blogUrl + '/posts/'+ helpers.niceURL(p['title'], '.html') + '''</link>
			<description>''' + helpers.cleanhtml(p['intro']) + '''</description>
		</item>'''

	return '''<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE document [
		<!ENTITY nbsp " ">
	]>
	<rss version="2.0"><channel>
		<title>''' + helpers.cleanhtml(params.blogTitle) + '''</title>
		<link>''' + params.blogUrl + '''</link>
		<description>''' + helpers.cleanhtml(params.blogSubTitle) + '''</description>
		<language>fr-FR</language>
		<generator>Blogogo</generator>
		<ttl>120</ttl>
		''' + items + '''
	</channel></rss>'''

def TMP_readme(params, helpers, tmps, myPosts):
	liste = ''
	for p in myPosts:
		liste += '- ' + str(p['id']) + ' / **' + p['title'] +  '** / ' + p['date'] + '\n'

	return '''Blog généré avec Narval
(''' + time.strftime("le %e/%m/%Y à %Hh%M", time.localtime()) + ''').

# Liste des ''' + str(len(myPosts)) + ''' articles
*id / **titre** / date*
''' + liste
