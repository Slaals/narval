# Documentation

**_Narval_** is a static blog generator written in Python.
This project is OpenSource and copyright free. You're welcome to contribute to this project.

## Prerequisites

- Having Python3.
- Modifying the file `config.py` to setup the blog

## Quick start

See section ["Quick setup"](#quick-setup).

## Add a post

One post per files. You can find the posts files in the folder `/posts` once the blog has been generated.

### File name

File name example : `3.how_to_build_an_house.html` or `3.html`.

In the file name you can find :

- A unique number which allows to ordonates the posts (the greatest number means that the post will be the first listed in the blog)
- A name which is the filename (no necessarily the post title)

### File content

Inside the file you may find 2 sections splitted by `---`. The first section is about the post parameters, the second section is about your post content that will be display in the blog.

For the first section, here are the parameters :

- **title** : post title,
- **cats** : post categories, put a `+` to append some categories,
- **date** : post date, it should be in the following format (J)J/(M)M/AAAA,
- **intro** (optional) : post's abstract (or introduction),
- **author** (optional) : you can specify the author name here,
- **thumb** (optional) : post's thumbnail.

The second article is the post in HTML format.

Here is a minimal example :


### Contenu du fichier
```
title = How to build an House
cats = Building+House+LifeStyle
date = 6/4/2017
intro = <p>Have you ever thought of building your house yourself? This post will tell you how.</p>
---
<h2>Introduction</h2><p>Bla bla bla...</p>
```

Notice that the `Introduction` uses a `h2` block, the reason is that the post title uses `h1` automatically.

## Add a page

As for posts there is one page per files. The pages folders is called `/pages`, and is contains only two parameters such as :

- **title** : page title,
- **desc** : page description mostly for SEO.

## Add a draft

The drafts folder is name `/drafts`. A draft is not published. It is useful to save posts in progress.

## Internal links

It is possible to use a special syntax to link posts inside the blog. For instance you can write :

`<a href="{blog:post:3}">Link text</a>`

This will create a link to the post with the ID 3. If you want to link to a page, replace `post` by `page` which the page ID you want to link to.

## Templates

The file `template.py` allows to configure how the blog looks. The code is commented to help you to do edit it.

## Styles

To edit the styles you can find the styles file in the folder `/theme`. For dynamic interactions, the blog uses the file `/ui.js`.

## Assets

Assets are located in the folder `/medias`. You can put all your audio files, images or video files in this folder.

## <a name="quick-setup"></a>Quick setup

- `git clone https://github.com/yultivert/narval`
- `cd narval && python3 build.py`

If the generation worked out, you will see a green text telling what eats a narval. If anything goes wrong, submit an issue here, I'll be able to help you.

You should now see two folders :

- _NARVAL
- _NARVAL-local

The first folder is the blog to publish in a web server, the second one is for testing purposes. Please, do not move the `_NARVAL-local` folder.

## Deploy your first blog

You can use Github Pages which is very convenient

1. Create a new repository name `githubaccount.github.io` (replace "githubaccount" by your Github's account name).
2. Open the file `config.py` and edits the parameter `blogUrl` to put your repository URL such has `blogUrl = https://githubaccount.github.io`
3. Generate your blog (explained in section )
4. With the terminal, go to the folder `_NARVAL`
5. Type :
```
git init
git commit -am "first commit"
git remote add origin https://github.com/[MONCOMPTE]/[MONCOMPTE].github.io.git
git push -u origin master
```

Github will ask you your credentials.

That's it! The blog is online.

When you want to add posts, pages or assets, you have to add it to the `_NARVAL` folder (has it is explained through this README, then you have to type in the terminal :
```
git commit -am "message"
git push origin master
```

# Documentation

**_Narval_** est un générateur de blog statique écrit en Python.
Le projet est opensource et entièrement libre de droits. Il est également possible d'y participer pour le faire évoluer.

## Prérequis

- Disposer de Python 3.* sur sa machine.
- Configurer le blog en modifiant le fichier `config.py`

## Démonstration rapide

Une fois le projet *Narval* téléchargé, il est possible de le générer directement puisqu'il contient déjà 4 articles et 1 page tests. Pour se faire, aller à la section "Générer le blog".

## Ajout d'un article

Un article par fichier. Ce fichier est à placer dans le dossier "posts".

### Nom du fichier

Il se compose :

- d'un nombre unique qui permet d'ordonner les fichiers (le fichier portant le nombre le plus grand sera le dernier ajouté et se trouvera en tête de liste des articles sur le blog;
- d'un point suivi d'un nom (celui de l'article en général, en version abrégée) sans caractère spécial et sans espace (facultatif, mais utile);
- de l'extension ".html".

Par exemple : "3.laPermaculture.html" ou encore "3.html".

### Contenu du fichier

Le contenu du fichier se divise en 2 sections séparées de `---`. La première contient les paramètres de l'article et la seconde contient l'article à proprement parler.

Les paramètres sont les suivants :

- **title** : Le titre de l'article (peut contenir du HTML de type *inline*),
- **cats** : le nom des catégories auxquelles l'article appartient séparées par le signe "+" (sans espaces),
- **date** : la date de publication ou de rédaction au format (J)J/(M)M/AAAA,
- **intro** (facultatif) : le chapeau de l'article (texte qui introduit l'article et qui est visible dans la liste des articles (doit contenir du HTML de type *block* et peut contenir du HTML de type *inline*),
- **author** (facultatif) : si l'auteur n'est pas l'auteur principal du blog,
- **thumb** (facultatif) : la miniature associée à l'article.

La seconde section contient l'article formaté en HTML.

Voici un exemple minimal du contenu d'un article bien formaté :

	title = La permaculture&nbsp;: les avantages
	cats = Nature+Autonomie
	date = 6/4/2017
	intro = <p>Nous allons voir ici en quoi la permaculture peut arranger les choses.</p>
	---
	<h2>Introduction</h2><p>Bla bla bla...</p>

On peut remarque que le contenu de l'article commence par un titre de niveau 2 (h2). Cela est dû au fait que le niveau 1 est attribué automatiquement au titre de l'article. On peut voir aussi que du HTML se trouve dans le titre de l'article (`&nbsp;`) pour obtenir une espace insécable.

## Ajout d'une page

L'ajout d'une page se fait de la même manière que l'ajout d'un article, à la diffèrence que le fichier doit se trouver dans le dossier "pages" et que seuls 2 paramètres sont disponibles :

- **title** : le titre de la page,
- **desc** : une description de la page utile pour le référencement (sans HTML).

## Ajout d'un brouillon

Un brouillon de page ou d'article se place dans le dossier "drafts". Un brouillon n'est pas publié. C'est simplement un dossier utile pour stocker son travail en cours.

## Liens internes

Il est possible d'utiliser quelques petits morceaux de code pour se simplifier la vie avec les liens. Ainsi, dans le contenu d'un article ou d'une page, on peut écrire ceci :

	<a href="{blog:post:3}">Texte du lien</a>

Cela aura pour effet de créer le lien vers l'article 3. `post` peut être remplacé par `page` pour une page et le numéro identifie l'article ou la page.

## Templates

Le fichier "template.py" permet de gérer l'affichage de tout : mise en place générale, liste d'articles, article, page. Le code est grandement commenté pour en permettre sa compréhension. Le dossier "thumbs" permet de stocker les miniatures de certains articles, car le template d'une liste d'articles peut varier selon la catégorie choisie. On peut afficher des miniatures pour une catégorie spécifique.

## Styles

Le dossier "theme" contient les feuilles de styles CSS ainsi que les images nécessaires au(x) thème(x). _Narval_ est fourni avec deux thèmes de bases changeables par les utilisateurs à l'aide d'une icône présente dans le coin supérieur droit de la fenêtre du navigateur. Le fichier "template.py" permet de définir les thèmes chargés. Le basculement d'un thème à l'autre se fait à l'aide de javascript à partir du fichier "ui.js". Ce fichier est destiné à contenir tout le code relatif à l'interaction dynamique avec l'utilisateur ("ui" pour "user interface").

## Médias

Le dossier "medias" permet d'y stocker toutes les images, vidéos et sons qui seront présents dans les articles ou les pages, pour une question d'organisation.

## Générer le blog

Dans un terminal, il faut saisir :

	python3 build.py

Si un message en vert apparaît, c'est que la génération a fonctionné. S'il y a une ou plusieurs erreurs mentionnées, il faudra chercher à les comprendre ou demander (à moi ou à quelqu'un qui programme un minimum).

Si "folder" n'a pas été changé dans le fichier "config.py", alors 2 dossiers seront construits :

- _NARVAL
- _NARVAL-local

Le premier est à déployer sur un serveur web, tandis que le second permet de tester le blog hors ligne en ouvrant le fichier "index.html". Cela peut servir à vérifier qu'il s'agit bien de ce que l'on souhaite publier ou de voir les changements apportés au thème facilement, sans avoir à déployer.
Ce second dossier ne doit pas être bougé de place dans le système d'exploitation, afin que tous les liens internes que contient le blog restent corrects.

## Déployer le blog

Le déploiement peut se faire sur Github Pages ou ailleurs. Github Pages étant un service gratuit et très pratique, nous allons voir comment procéder avec.

1. Créer un compte sur Github (ce nom se retrouvera dans l'url du blog)
2. Ajouter un nouveau "Repository" portant le nom du compte + ".github.io" et cliquer sur "Create repository"
3. Modifier la valeur de "blogUrl" dans "config.py" pour mettre le nom du "repository" précédé du protocole (ex: "https://moncompte.github.io")
4. Générer le blog (voir la section précédente)
5. Se rendre dans le dossier "_NARVAL" (ou autre nom si ce nom a été changé dans "config.py");
6. Ouvrir le terminal dans ce dossier et saisir :

	git init
	git commit -am "first commit"
	git remote add origin https://github.com/[MONCOMPTE]/[MONCOMPTE].github.io.git
	git push -u origin master

Github demandera le nom et le mot de passe de l'utilisateur.
Et voilà, le blog est en ligne pour la première fois (à l'adresse définie dans "blogUrl"). Après le premier déploiement, il n'y a plus qu'à faire :

	git commit -am "message"
	git push origin master

Attention : Il ne faut pas supprimer le dossier "_NARVAL" après un déploiement. Il se mettra à jour sans intervention avec les futurs déploiements. Cela permet de conserver le dossier ".git" qu'il contient et donc, de ne pas avoir à tout resaisir dans le terminal à chaque fois (seulement les 3 lignes de code ci-dessus).
