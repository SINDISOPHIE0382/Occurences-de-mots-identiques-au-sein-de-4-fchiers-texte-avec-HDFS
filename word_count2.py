#!/home/cloudera/anaconda3/bin/python3.7

##Import de la librairie HDFS3
import hdfs3
##import du dictionnaire de la librairie collections
from collections import defaultdict, Counter
from hdfs3 import HDFileSystem

hdfs=HDFileSystem(host='localhost',port=8020)

##affiche la liste des fichiers disponible dans le répertoire
filenames = hdfs.glob('/data_in')
print('Liste des fichiers :')
print(filenames)

##fonction permettant de supprimer les caractères spéciaux (,., \"*?!;:)
def cleanse_word(word):
	# find regex for word
	return word.lower().strip(',').strip('.').strip('\'').strip('"').strip('*').strip('?').strip('!').strip(';').strip(':')

##fonctiontion permettant de calculer le nombre d'occurences d'un mot d'un fichier
def count_words(file):
	word_counts = defaultdict(int)
	for line in file:
	#utilisation de la fonction decode pour l'encodage 
		line = line.decode('utf8').strip()
		for word in line.split():
		#appel de la fonction pour suppression des caractères spéciaux
			word = cleanse_word(word)
			word =(word)
			word_counts[word] += 1	
	return word_counts
##fonction permettant de calculer le nombre de mot pour l'ensemble des fichiers disponible dans le répertoire data_in
all_counts = Counter()
for fn in filenames:
##lecture des fichiers 
	with hdfs.open(fn) as f:
		data=f.read()
		counts = count_words([data])
		all_counts.update(counts)

## Afficage du nombre des mots répétés
print('Le nombre de mots qui se repète EN SUPPRIMANT LES CARACTERES SPECIAUX: '+str(len(all_counts)))
##Affichage du top 10 des mots les plus repétés en supprimant les caractères spéciaux
print('Le top 10 des mots les plus repétés EN SUPPRIMANT LES CARACTERES SPECIAUX est :  ')

for k,v in sorted(all_counts.items(), key=lambda p:p[1], reverse=True)[:10]:
    print('le mot ' + k, 'est repeté ' + str(v) + ' fois')
    print("\n")

