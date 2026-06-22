import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
#=====================================
            #Question 1
#=====================================
#Objectif:
#IDentifier l'année durant laquelle l'interet mondial 
#pour le mot clé "workout" a atteint son niveau maximal
#dans les donnée google trends

#Stratégie:
# 1. charger le fichier contenant l'evolution mensuelle
#des recherche pour la mot clé workout
# 2 visualiser l'évolution pour comprendre la tendance
# 3 Identifier la valeur max dans la serie



#Charge les donnée google trends
fr=pd.read_csv("data/workout.csv")

#ViSualisation de l'evolution du mot workout
plt.figure(figsize=(12,6))
plt.plot(fr["month"],fr["workout_worldwide"])
plt.xticks(rotation=90)
plt.title("popularité du mot clé dans le temps")
plt.ylabel("indice de popularité")
plt.xlabel("mois")
plt.savefig("image/fic1.png")
plt.close()

# Recupere la ligne dont l'indice de popularité est plus elevé
# idmax() retourne l'index de la valeur maximal dans la colonne
# loc[] permet ensuite d'acceder a la ligne complete
l_ind_max=fr.loc[fr["workout_worldwide"].idxmax()]

#La colonne month contient une date au format AAAA-MM
#On extrait les 4 premiers caractere pour obtenir l'année
year_str=l_ind_max["month"][:4]
print(f"Le pic mondial des recherches pour workout a été ateint en: {year_str}")


#=======================================
            #Qustion2
#======================================
#objectif 
#comparer la popularité de trois mot liés au fitness
# 'home workout
# gym workout
# home gym
#L'objectif est d'identifier
#1 le mot ayant connu le plus fort interet pendant la pandémie (covid 19)
#  le mot clé le plus populaire actuellement
#Stratégie
# 1 charger le fichier contenant les donnés de popularité
# 2 visualiser leur evolution dans le temps afin de  réperer les tendances
# 3 Identifier le mot clé ayant atteint le niveau de popularité des trois mots
# 4 Observer les derniers valeurs de la series afin de determiner quel mot domine

clef=pd.read_csv("data/three_keywords.csv")

plt.figure(figsize=(12,6))
plt.plot(clef["month"],clef["home_workout_worldwide"],label="home workout")
plt.plot(clef["month"],clef["gym_workout_worldwide"],label="gym workout")
plt.plot(clef["month"],clef["home_gym_worldwide"],label="home gym")
plt.xticks(rotation=90)
plt.legend()
plt.savefig("image/fic2.png")
plt.close()

key_word={"home workout":clef["home_workout_worldwide"].max(),
             "gym workout":clef["gym_workout_worldwide"].max(),
             "home gym":clef["home_gym_worldwide"].max()}
peak_covid=max(key_word,key=key_word.get)
print(f"Le mot clé le plus populaire pendant la pandémie est {peak_covid}")
tail=clef.tail()
last={"home workout":tail["home_workout_worldwide"].max(),
      "gym workout":tail["gym_workout_worldwide"].max(),
      "home gym":tail["home_gym_worldwide"].max()}
current=max(last,key=last.get)
print(f"Le mot le plus populaire actuellement est {current}")

#=======================================
        #Question3
#=====================================
#Objectif :
#Determiner lequel des 3 pays suivants le plus fort
#interet pour le mot clé workout
#United states
#Australia
#Japan
#sTRATÉGIE
#1 charger le fichier contenant les donnés geographique
#2 filtrer le dataframe afin de conserver uniquement les Etats Unis,Autralie et le Japon
#3 visualiser les indice de popularité pour comparer rapidement les 3 pays
# 4 identifier le pays possédant l'indice le plus élevé

workout=pd.read_csv("data/workout_geo.csv")

#conserver uniquement les 3 pays
dt=workout[workout["country"].isin(["United States","Australia","Japan"])]
plt.figure(figsize=(12,6))
plt.bar(dt["country"],dt["workout_2018_2023"])
plt.title("popularité du mot clé workout par pays")
plt.xlabel("pays")
plt.ylabel("indice de popularité")
plt.plot(dt["country"],dt["workout_2018_2023"])
plt.savefig("image/fic3.png")
#print(workout.sort_values("country"))
#print(dt)
top_country=dt.loc[dt["workout_2018_2023"].idxmax(),"country"]
print(f"Le pays montrant avec plus d'interet est :{top_country}")


#========================================
        #Question4
#======================================
#Meme demarche que la question 3

three_keyword=pd.read_csv("data/three_keywords_geo.csv")

fr=three_keyword[three_keyword["Country"].isin(["Philippines","Malaysia"])]
#print(fr)
home_workout_geo=fr.loc[fr["home_workout_2018_2023"].idxmax(),"Country"]
print(f"le pays qui montre le plus d'interet est : {home_workout_geo}")
