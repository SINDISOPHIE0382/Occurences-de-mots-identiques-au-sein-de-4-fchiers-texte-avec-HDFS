#!/home/cloudera/anaconda3/bin/python3.7
## import de la librairie HDFS3
import hdfs3
#import du dictionnaire de la librairie collections
from collections import defaultdict, Counter
from hdfs3 import HDFileSystem

hdfs=HDFileSystem(host='localhost',port=8020)

#affiche la liste des fichiers disponible dans le répertoire
filenames = hdfs.glob('/data_in')
print ('Liste des fichiers :')
print(filenames)

##fonction permet de compter le nombre de mot d'un fichier
def count_words(file):
	word_counts = defaultdict(int)
	for line in file:
	#utilisation de la fonction decode pour l'encodage
		line = line.decode('utf8').strip()
		for word in line.split():
			word_counts[word] += 1	
	return word_counts
	
##fonction permet de compter le nombre dans l'ensemble des fichiers disponibles dans le répertoire data_in
all_counts = Counter()
for fn in filenames:
##lecture fichiers avec hfds
	with hdfs.open(fn) as f:
		data=f.read()
		counts = count_words([data])
		all_counts.update(counts)

##affiche le nombre de mot répetés
print('Le nombre de mots qui se repète SANS SUPPRESSION DES CARACTERES SPECIAUX : '+str(len(all_counts)))

##affiche le top 10 des mots les plus repetés 
print('Le top 10 des mots les plus repétés SANS SUPPRESSION DES CARACTERES SPECIAUX est :  ')

for k,v in sorted(all_counts.items(), key=lambda p:p[1], reverse=True)[:10]:
    print('le mot ' + k, 'est repeté ' + str(v) + ' fois')
    print("\n")

 
