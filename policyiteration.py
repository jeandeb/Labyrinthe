import objects
import pickle 
import sys
HAUT = 0 
DROITE = 1
BAS = 2
GAUCHE = 3
NB_ITER = 10
DISCOUNT = 0.5


mdp = objects.amarkov( DISCOUNT )
valeur = 0
valeur_future = 0

mdp.print_tab

for greed in range( 5 ) : 
	for iteration in range( NB_ITER ) :
		for i in range( mdp.nb_x ) : 
			for j in range( mdp.nb_y ) : 

				#Si case goal -> ne pas faire les calculs
				

				for k in range( mdp.nb_actions ) : 

					etati, etatj = mdp.action( k, i, j )
				
					#Bellman expectation equation
					reward = mdp.tab_reward[k]
					if( mdp.end( i, j )) :
						reward += 20
					valeur_future = mdp.value[etati][etatj]
					valeur += mdp.tab_trans[i][j][k]*( reward + mdp.discount*valeur_future )

				mdp.value[i][j] = valeur			
				valeur = 0 

	#Changement de la politique + reinitialisation du tableau de valeurs
	mdp.greedy_policy()
	mdp.value_to_zero()

print( mdp.tab_trans )

if( (len(sys.argv) > 1) and (sys.argv[1] == "yes") ) :
	pickle.dump( mdp, open( "mdp_policyite.p", "wb" ) )










