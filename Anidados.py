def aventura_isla():
    print("¡Bienvenido a la Isla Misteriosa!")
    print("Te encuentras en una playa. Frente a ti hay dos caminos: uno lleva a la jungla y el otro a una cueva.")
    
    # Primera decisión: Jungla o Cueva
    decision1 = input("¿Qué camino eliges? (jungla/cueva): ").lower()
    
    if decision1 == "jungla":
        print("\nEntras en la jungla. Hace calor y hay muchos sonidos extraños.")
        print("Ves un río y un puente colgante. ¿Qué haces?")
        
        # Segunda decisión: Cruzar el puente o seguir el río
        decision2 = input("¿Cruzas el puente o sigues el río? (puente/rio): ").lower()
        
        if decision2 == "puente":
            print("\nEl puente se rompe y caes al río. ¡Pero encuentras un cofre con oro!")
            print("¡Felicidades, has encontrado el tesoro!")
        elif decision2 == "rio":
            print("\nSigues el río y encuentras una cascada. Detrás de ella hay una cueva con un tesoro.")
            print("¡Felicidades, has encontrado el tesoro!")
        else:
            print("\nNo tomaste una decisión válida. Te pierdes en la jungla.")
    
    elif decision1 == "cueva":
        print("\nEntras en la cueva. Está oscuro y húmedo.")
        print("Ves dos túneles: uno iluminado y otro oscuro. ¿Cuál eliges?")
        
        # Segunda decisión: Túnel iluminado o oscuro
        decision2 = input("¿Túnel iluminado o oscuro? (iluminado/oscuro): ").lower()
        
        if decision2 == "iluminado":
            print("\nEl túnel iluminado te lleva a una sala llena de tesoros.")
            print("¡Felicidades, has encontrado el tesoro!")
        elif decision2 == "oscuro":
            print("\nEl túnel oscuro está lleno de trampas. Caes en un pozo sin fondo.")
            print("¡Game Over!")
        else:
            print("\nNo tomaste una decisión válida. Te pierdes en la cueva.")
    
    else:
        print("\nNo elegiste un camino válido. Te quedas en la playa para siempre.")

# Llamar a la función para comenzar la aventura
aventura_isla()