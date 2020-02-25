# Occurences-de-mots-identiques-au-sein-de-4-fchiers-texte-avec-HDFS

Objectif : comptage du nombre de mots présents dans 4 fichiers txt avec l’utilisation de HDFS3
Les étapes suivies :
	Création d’un répertoire (data_in) dans HDFS et chargement des 4 fichiers txt.
	Création d’un code python qui permet de compter le nombre de mot présent dans tous les fichiers et affichage du nombre de mots répétés et les 10 mots les plus répétés.
Dans les 4 fichiers il y a des caractères spéciaux (,  .  ) et sans suppression de ces caractères spéciaux, un mot avec un caractère spécial peut être compté autant qu’un autre mot, pour illustration dans l’exemple ci-dessous « ex » et « ex. » sont comptés autant que deux mots différents et non pas un seul.
 
Deux programmes python ont été créé :
	Un programme qui compte le nombre de mots dans les 4 fichiers txt sans suppression des caractères spéciaux (word_count1.py)
	Un programme qui compte le nombre de mots dans les 4 fichiers txt avec suppression des caractères spéciaux (word_count2.py)

