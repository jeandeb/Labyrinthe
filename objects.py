import numpy as np 
#from enum import Enum
HAUT = 0
DROITE = 1
BAS = 2
GAUCHE = 3


class amarkov( object ) : 

	def __init__( self, discount ):

		self.nb_x = 6
		self.nb_y = 4
		self.nb_actions = 4
		self.nbstate = self.nb_x * self.nb_y
		self.discount = discount #valeur de reduction des rewards par etapes
		self.value = np.zeros(( self.nb_x, self.nb_y ))

		#intialisation du tableau d'etat (plateau du jeu)
		self.tab_state = np.zeros(( self.nb_x, self.nb_y ))

		self.tab_state[self.nb_x-1][self.nb_y-1] = 2

		#case pleine(block)
		self.tab_state[0][2] = 1
		self.tab_state[0][3] = 1
		self.tab_state[1][3] = 1
		self.tab_state[2][0] = 1
		self.tab_state[2][1] = 1
		self.tab_state[4][2] = 1
		self.tab_state[4][3] = 1
		self.tab_state[5][0] = 1

		#initialisation des rewards a -1
		self.tab_reward = np.zeros(( self.nb_actions ))
		for i in range( 4 ) : 
			self.tab_reward[i] = -5

		#intialisation de la politique
		self.tab_trans = np.zeros(( self.nb_x, self.nb_y, self.nb_actions ))
		for i in range( self.nb_x ) : 
			for j in range( self.nb_y ) :
				for k in range( self.nb_actions ) : 
					self.tab_trans[i][j][k] = 0.25

		
	def get_state( self, i, j ) :

		return self.tab_state[i][j]

	#si la case n'est pas un block
	def is_jouable( self, i, j ) : 

		if( self.tab_state[i][j] != 1 ) : 
			return True
		return False

	#les regles du jeu, renvoie la case atteinte lors de laction num
	def action( self, num, i, j ):

		if( (self.tab_state[i][j] == 1 ) or (self.end( i, j ))  ) : 
			return i,j
		#action haut
		if( num == DROITE) : 
			if( i == self.nb_x - 1 ):
				return i,j
			elif( self.get_state(i+1, j) == 1 ) : 
				return i,j
			return i+1,j

		#action droite
		if( num == HAUT) : 
			if( j == self.nb_y - 1 ):
				return i,j
			elif( self.get_state( i, j+1 ) == 1 ) : 
				return i,j
			return i,j+1

		#action bas
		if( num == GAUCHE) : 
			if( i == 0 ):
				return i,j
			elif( self.get_state( i-1, j ) == 1 ) : 
				return i,j
			return i-1,j

		#action droite
		if( num == BAS) : 
			if( j == 0 ):
				return i,j
			elif( self.get_state( i, j-1 )== 1 ) : 
				return i,j
			return i,j-1

	#boolean renvoyant si oui ou non i et j correspondent à un état final
	def end( self, i, j ) : 

		if ( self.tab_state[i][j] == 2 ) : 
			return True
		return False

	#change la politique en fonction du tableau de valeur
	def greedy_policy( self ):
		 
		 #tableau qui contient la valeur de chaque action
		tab_optimal = np.zeros( self.nb_actions )

		for i in range( self.nb_x ) : 
		 	for j in range( self.nb_y ): 
		 		cpt = 0
		 		tab_optimal = [0,0,0,0]
		 		maxi = self.max_reward( i, j )

		 		#remplissage de taboptimal par les action avec un valeur max
		 		for k in range( self.nb_actions ) : 
		 		
		 			x, y = self.action( k, i, j )
		 			value = self.value[x][y] + self.tab_reward[k]

		 			if( value == maxi ) :
		 	
		 				tab_optimal[k] = maxi
		 				cpt += 1

		 		#calcul de la proba de chaque actions
		 		for k in range( self.nb_actions ) : 
		 			if( tab_optimal[k] != 0 ) : 

			 			proba = 1./cpt
			 			self.tab_trans[i][j][k] = proba
			 		else :
			 			self.tab_trans[i][j][k] = 0
	
	#met a zero les valeurs de value
	def value_to_zero( self ) :

		 for i in range( self.nb_x ) : 
		 	for j in range( self.nb_y ): 
		 		self.value[i][j] = 0	 

	#renvoie le reward maximum atteignable quelque soit les actions
	def max_reward( self, i , j ) : 

		maxi = -10000

		for k in range( self.nb_actions ) : 
			x, y = self.action( k, i, j )
			if ( (self.value[x][y] + self.tab_reward[k]) >= maxi ) : 
				maxi = self.value[x][y] + self.tab_reward[k]

		return maxi

	#mis en forme "graphique" du labyrinthe
	@property 
	def print_tab( self ) : 

		ligne = ""
		haut = ""
		for j in range( self.nb_x + 2 ):
			haut += "-"
		print haut 
		for j in range( self.nb_y ) :
			ligne += "|" 
			for i in range( self.nb_x ) : 
				typ = self.tab_state[i][self.nb_y-1-j]
				if( typ == 1 ) : 
					ligne += "X"
				elif( typ == 0 ) : 
					ligne += "O"
				else : 
					ligne += "$"
			ligne += "|"
			print ligne
			ligne = ""
		print haut 










