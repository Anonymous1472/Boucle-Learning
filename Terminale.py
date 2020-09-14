#coding:utf-8

user = "UserVisite"
jeu_lance = True
print("")
print("T-Force One Terminal 0.1")
print("Pour plus d'aide tape : -help")
print("Connecter en tant que :",user)
print("")


while jeu_lance:
	#Creation des instructions et commandes
	choixMenu = input("One> ") #Laisser One> (Prompt)

	if choixMenu == "-again": #Commande
		continue #Continuer la boucle

	elif choixMenu == "-quitter":
		jeu_lance = False #Binaire
		break #Couper la boucle

	elif choixMenu == "-hi": #Commande
		print("Salut User Bip Boop, j'ai 180 ans")
		print("")

	elif choixMenu == "-help": #Commande
		print("Liste des commandes :")
		print("-again : Reload le programme")
		print("-quitter : Ferme le programme")
		print("-hi : Salutation du bot")
		print("-info : Présentation système")
		print("")

	elif choixMenu == "-info": #Commande
		print("Informations :")
		print("Créateur, Mr_Size")
		print("Actuel : 0.1")
		print("Private No Copyright T-Force")
	else: #Sinon
		print("Commande introuvable !")
		print("")