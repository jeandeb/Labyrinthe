import objects
HAUT = 0 
DROITE = 1
BAS = 2
GAUCHE = 3
NB_ITER = 10


mdp = objects.amarkov( 0.5 )
valeur = 0
valeur_future = 0

mdp.print_tab

for greed in range( 5 ) : 
	for iteration in range( NB_ITER ) :
		for i in range( mdp.nb_x ) : 
			for j in range( mdp.nb_y ) : 

				#Si case goal -> ne pas faire les calculs
				if( mdp.end( i, j )) :
					continue
					
				for k in range( mdp.nb_actions ) : 

					etati, etatj = mdp.action( k, i, j )

					#Bellman expectation equation
					reward = mdp.tab_reward[k]
					valeur_future = mdp.value[etati][etatj]
					valeur += mdp.tab_trans[i][j][k]*( reward + mdp.discount*valeur_future )

				mdp.value[i][j] = valeur			
				valeur = 0 

	#Changement de la politique + reinitialisation du tableau de valeurs
	mdp.greedy_policy()
	mdp.value_to_zero()

print( mdp.tab_trans )











