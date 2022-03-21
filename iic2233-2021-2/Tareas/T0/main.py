from clases import User, Post, Comment
from funciones_menu import menu_de_inicio, menu_principal, \
    menu_de_publicaciones, menu_de_publi_realizadas


def funcion_principal():
    # font de aqui http://www.network-science.de/ascii/
    print('''                                                                                                                                                                                    
     ______   _______  _______  _______  _______  _______  _______  _______  _______ 
    (  __  \ (  ____ \(  ____ \(  ___  )(       )(  ____ \(  ____ )(  ____ \(  ____ \\
    | (  \  )| (    \/| (    \/| (   ) || () () || (    \/| (    )|| (    \/| (    \/
    | |   ) || |      | |      | |   | || || || || (__    | (____)|| |      | (__    
    | |   | || |      | |      | |   | || |(_)| ||  __)   |     __)| |      |  __)   
    | |   ) || |      | |      | |   | || |   | || (      | (\ (   | |      | (      
    | (__/  )| (____/\| (____/\| (___) || )   ( || (____/\| ) \ \__| (____/\| (____/\\
    (______/ (_______/(_______/(_______)|/     \|(_______/|/   \__/(_______/(_______/

                        +-+-+ +-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+
                        |L|o| |q|u|i|e|r|e|s|,| |l|o| |t|e|n|e|m|o|s|
                        +-+-+ +-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+
        ''')

    estados_programa = {'inicio': True, 'principal': False,
                        'publicaciones': False, 'publi_realizadas': False,
                        'cerrar': False, 'abrir_publicacion': False}
    # También, se me ocurrió aplicar stack para cambiar entre estados.
    # Al final preferí esta opción de utilizar un diccionario, donde
    # mi idea es que solo una llave tenga como valor True, el cual se
    # logra con la función cambio_de_estado() en el archivo funciones_menu.py


    # A continuación, obtengo toda la info de los arhivos .csv entregados.
    # Para guardar los datos, al generar un objeto, este se guarda automáticamente
    # en una lista dentro de cada clase, como se ve en el archivo clases.py
    with open('usuarios.csv', encoding='utf-8') as file:
        [User(f.strip()) for f in file.readlines()[1:]]

    with open('publicaciones.csv', encoding='utf-8') as file:
        [Post(*f.strip().split(',', maxsplit=5)) for f in file.readlines()[1:]]

    with open('comentarios.csv', encoding='utf-8') as file:
        [Comment(*f.strip().split(',', maxsplit=3)) for f in file.readlines()[1:]]

    for comentario in Comment.comments:
        for publicacion in Post.posts:
            if comentario.id == publicacion.id:
                publicacion.comments.append(comentario)

    for publicacion in Post.posts:
        for user in User.users:
            if publicacion.username == user.name:
                user.posts.append(publicacion)


    # Código principal del programa. Dependiendo del estado/página en
    # el cual el programa está, es que se cumple un solo if.
    usuario_inscrito = False
    while not estados_programa['cerrar']:

        if estados_programa['inicio']:
            usuario_inscrito, estados_programa = menu_de_inicio(estados_programa,
                                                                User.users)

        elif estados_programa['principal']:
            estados_programa = menu_principal(estados_programa)

        elif estados_programa['publicaciones']:
            estados_programa = menu_de_publicaciones(estados_programa,
                                                     Post.posts, usuario_inscrito)

        elif estados_programa['publi_realizadas']:
            estados_programa = menu_de_publi_realizadas(estados_programa,
                                                        usuario_inscrito)


if __name__ == '__main__':
    funcion_principal()
