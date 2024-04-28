from AdminService import AdminService
from User import User


def main():
    adminService = AdminService()
    
    while True:
        print("\nOptions:")
        print("1. Add ")
        print("2. Update ")
        print("3. Delete ")
        print("4. List ")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Ocassional, 2. Wholesaler): ")
            
            """if type.upper() == 'O':
                user = CompradorOcasional(nombre, identificacion, direccion, telefono, correo, intereses)
            elif tipo_usuario.upper() == 'M':
                user = CompradorMayorista(nombre, identificacion, direccion, telefono, correo, intereses)
            else:
                print("Tipo de usuario no válido.")
              continue"""
            
            user = User(name,phone,email,type)
            adminService.Add(user)
            print("User added.")

        elif choice == '2':
            id1 = int(input("Id: "))
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            type = input("Type of client (1. Ocassional, 2. Wholesaler): ")
            user2 = User(name,phone,email,type)
            adminService.Edit(id1, user2)
            print("User updated.")

            """ if tipo_usuario.upper() == 'O':
                usuario = CompradorOcasional(nombre, identificacion, direccion, telefono, correo, intereses)
            elif tipo_usuario.upper() == 'M':
                usuario = CompradorMayorista(nombre, identificacion, direccion, telefono, correo, intereses)
            else:
                print("Tipo de usuario no válido.")
                continue """
       
        elif choice == '3':
            id2 = int(input("Ingrese el índice del usuario a eliminar: "))
            adminService.Delete(id2)
            print("User deleted.")
        
        elif choice == '4':
            print("Users:")
            adminService.List()
        
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Option No Valid.")

if __name__ == "__main__":
    main()
