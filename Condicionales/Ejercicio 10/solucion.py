tipo = str(input("¿Desea una pizza con ingredientes vegetarianos? Y for yes o N for no: "))

if tipo in ['y', 'Y', 'yes', 'Yes', 'YES'] :
	print("Los ingredientes que puede añadir a la pizza vegetariana son: Pimiento y Tofu.")
	valor = int(input("Si desea agregar Pimiento presione [1] ó si desea agregar Tofu presione [2]. "))
else :
	print("Los ingredientes que puede añadir a la pizza no vegetariana son: Peperoni, Jamón y Salmón. ")
	valor = int(input("Si desea agregar Peperoni presione [1]; Si desea agregar Jamon presione [2]. ó Si desea agregar Salmon presione [3]. "))

if tipo in ['y', 'Y', 'yes', 'Yes', 'YES'] :
		if valor == 1 :
			print("Has elegido la pizza Vegetariana, los ingredientes de tu pizza son los siguientes: Mozzarella; Tomate y Pimiento.")
		else :
			print("Has elegido la pizza Vegetariana, los ingredientes de tu pizza son los siguientes: Mozzarella; Tomate y Tofu.")
else :
		if valor == 1 :
			print("Has elegido la pizza No vgetariana, los ingredientes de tu pizza son los siguientes: Mozzarella; Tomate y Peperoni. ")
		elif valor == 2 :
			print("Has elegido la pizza No vgetariana, los ingredientes de tu pizza son los siguientes: Mozzarella; Tomate y Jamon.")
		else :
			print("Has elegido la pizza No vgetariana, los ingredientes de tu pizza son los siguientes: Mozzarella; Tomate y Salmon.")
