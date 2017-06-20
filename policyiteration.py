import objects
HAUT = 0 
DROITE = 1
BAS = 2
GAUCHE = 3
NB_ITER = 100


mdp = objects.amarkov( 0.5 )
valeur = 0
valeur_future = 0

mdp.print_tab


for iteration in range( NB_ITER ) :
	for i in range( mdp.nb_x ) : 
		for j in range( mdp.nb_y ) : 
			for k in range( mdp.nb_actions ) : 
				etati, etatj = mdp.action( k, i, j )
				valeur_future = mdp.value[etati][etatj]
				valeur += mdp.tab_trans[i][j][k]*( mdp.tab_reward[k] + mdp.discount*valeur_future )
			mdp.value[i][j] = valeur			
			valeur = 0 

mdp.greedy_policy()
mdp.value_to_zero()

for iteration in range( NB_ITER ) :
	for i in range( mdp.nb_x ) : 
		for j in range( mdp.nb_y ) : 
			for k in range( mdp.nb_actions ) : 
				etati, etatj = mdp.action( k, i, j )
				valeur_future = mdp.value[etati][etatj]
				valeur += mdp.tab_trans[i][j][k]*( mdp.tab_reward[k] + mdp.discount*valeur_future )
			mdp.value[i][j] = valeur			
			valeur = 0 

mdp.greedy_policy()
mdp.value_to_zero()



print( mdp.tab_trans )
print( mdp.value )