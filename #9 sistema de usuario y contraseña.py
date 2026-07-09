#9 sistema de usuario y contraseña
usuario = "jaenooo"
co = "1289".lower()
i=1
while (i==1):
    
    n = input("Ingresa tu nombre de usuario:" ).lower()
    if n == usuario:
        c = input("Ingresa tu contraseña: ")
        if c == co:
            print ("Bienvenido al sistema :)")
            break
        else:
            print ("contraseña incorrecta")
            print ("Intentalo de nuevo")
    else:
        print ("Usuario no registrado")
        print ("Vuelve a intentarlo")
        s = input("Deseas salir (Si/No)?").lower()
        if s == "si":
            i=i-1
        
    
        
        
