import objects
import pickle 
import sys
HAUT = 0 
DROITE = 1
BAS = 2
GAUCHE = 3
NB_ITER = 100

mdp = objects.amarkov( 0.5 )
valeur = 0
valeur_future = 0
maxi = 0

for iteration in range( NB_ITER ) :
	for i in range( mdp.nb_x ) : 
		for j in range( mdp.nb_y ) : 

			if ( mdp.end( i, j ) ) : 
				continue

			#Bellman optimality equation
			valeur_future = mdp.max_reward( i, j )
			mdp.value[i][j] = mdp.discount*valeur_future
			valeur_future = 0

mdp.greedy_policy()

if( (len(sys.argv) > 1) and (sys.argv[1] == "yes") ) :
	pickle.dump( mdp, open( "mdp_valueite.p", "wb" ) )

#print( mdp.value )
#print( mdp.tab_trans )