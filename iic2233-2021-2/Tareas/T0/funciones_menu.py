import parametros
from datetime import datetime
from clases import User, Post, Comment


# Este es el archivo principal, el cual se tiene que correr para que funcione DDCommerce
# Pensé en agregar una zona donde se mostraran todos lo comentarios de un usuario,
# como también buscar un usuario donde ver sus publicaciones y comentarios
# Al final decidí, por honor a mi tiempo, solo programar los requisitos dados en el enunciado.


def menu_de_inicio(estados_programa, archivo_de_usuarios):
    usuario = False
    respuesta_usuario = '5'
    nombre_usuarios = [u.name for u in archivo_de_usuarios]
    print('** Menú de inicio **\n')
    while respuesta_usuario not in ['1', '2', '3', '4']:
        respuesta_usuario = input(f"[1] REGISTRATE ¡YA!\t[2] Ingresar sesión\t"
                                  f"[3] Ingreso anónimo\t[4] Salir\n")
        if respuesta_usuario not in ['1', '2', '3', '4']:
            print('Ingrese una respuesta válida >:( [1, 2, 3, o 4]\n')

    if respuesta_usuario == '1':
        usuario = input('Username: ')
        invalid_user = False
        if usuario in nombre_usuarios:
            print('Se más original, este nombre ya está ocupado.\n')
            invalid_user = True
        elif ',' in usuario:
            print('Nombre inválido, no se permiten las comas.\n')
            invalid_user = True
        elif parametros.MIN_CARACTERES > len(usuario) \
                or parametros.MAX_CARACTERES < len(usuario):
            print(f'El nombre tiene que tener entre {parametros.MIN_CARACTERES}'
                  f' y {parametros.MAX_CARACTERES} caracteres.\n')
            invalid_user = True
        if not invalid_user:
            User(usuario)
            with open('usuarios.csv', 'a') as file:
                file.write('\n'+usuario)
            print(f'Tu usuario ({usuario}) ha sido creado correctamente.\n')
            estados_programa = cambio_de_estado('principal', estados_programa)

    elif respuesta_usuario == '2':
        usuario = input('Username: ')
        if usuario in nombre_usuarios:
            print(f'Bienvenido, {usuario} :)\n')
            estados_programa = cambio_de_estado('principal', estados_programa)
        else:
            print(f'Usuario ({usuario}) no existe.\n')

    elif respuesta_usuario == '3':
        print('Entrando como usuario anónimo\n')
        estados_programa = cambio_de_estado('publicaciones', estados_programa)

    elif respuesta_usuario == '4':
        print('¡ADIÓS!\n')
        estados_programa = cambio_de_estado('cerrar', estados_programa)

    return usuario, estados_programa


def menu_principal(estados_programa):
    print('\n** Menú principal **\n')
    respuesta_usuario = '4'

    while respuesta_usuario not in ['1', '2', '3']:
        respuesta_usuario = input(f"[1] Menú de Publicaciones\t"
                                  f"[2] Menú de Publicaciones Realizadas\t[3] Volver\n")
        if respuesta_usuario not in ['1', '2', '3']:
            print('Ingrese una respuesta válida >:( [1, 2, o 3]\n')

    if respuesta_usuario == '1':
        print('Entrando al menú de publicaciones\n')
        estados_programa = cambio_de_estado('publicaciones', estados_programa)

    elif respuesta_usuario == '2':
        print('Entrando al menú de publicaciones realizadas\n')
        estados_programa = cambio_de_estado('publi_realizadas', estados_programa)

    elif respuesta_usuario == '3':
        print('Volviendo al menú de inicio\n')
        estados_programa = cambio_de_estado('inicio', estados_programa)

    return estados_programa


def menu_de_publicaciones(estados_programa, lista_publicaciones, usuario_no_anonimo):
    print('** Menú de Publicaciones **\n')
    respuesta_usuario = ''
    respuestas_posibles = []

    for numero in range(1, len(lista_publicaciones) + 2):  # Generador inputs posibles
        respuestas_posibles.append(str(numero))

    string_resp_usuario = ''
    numero_publicacion = 1

    publicaciones_ordenada = sorted(lista_publicaciones,
                                    key=lambda post: post.fecha, reverse=True)

    for publi in publicaciones_ordenada:
        string_resp_usuario += f'[{numero_publicacion}] {publi.titulo} {publi.fecha}\n'
        numero_publicacion += 1
    string_resp_usuario += f'[{numero_publicacion}] Volver\n'

    while respuesta_usuario not in respuestas_posibles:
        respuesta_usuario = input(string_resp_usuario)
        if respuesta_usuario not in respuestas_posibles:
            print('Ingrese una respuesta válida >:(\n')

    if respuesta_usuario == str(numero_publicacion):
        print('Volviendo a página anterior\n')
        if usuario_no_anonimo:
            estados_programa = cambio_de_estado('principal', estados_programa)
        else:
            estados_programa = cambio_de_estado('inicio', estados_programa)

    else:
        publicacion = publicaciones_ordenada[int(respuesta_usuario) - 1]
        abrir_publicacion(publicacion, usuario_no_anonimo)

    return estados_programa


def menu_de_publi_realizadas(estados_programa, nombre_usuario):
    print('\n** Menú de Publicaciones Realizadas **\n')
    respuesta_usuario = ''
    respuestas_posibles = ['1', '2', '3']

    user = [u for u in User.users if u.name == nombre_usuario][0]

    print(f'Publicaciones de {user.name}:\n')
    for post in user.posts:
        print('-', post.titulo)

    while respuesta_usuario not in respuestas_posibles:
        respuesta_usuario = input('\n[1] Crear publicación\t'
                                  '[2] Eliminar publicación\t[3] Volver\n')
        if respuesta_usuario not in respuestas_posibles:
            print('Ingrese una respuesta válida >:(\n')

    if respuesta_usuario == '1':
        print('\nDatos de tu nueva publicación')
        titulo = input('Título: ')
        precio = input('Precio: ')
        descripcion = input('Descripción: ')
        fecha = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        id_publicacion = str(int(Post.posts[-1].id) + 1)
        # El id más alto siempre va a ser el último,
        # por lo tanto el siguiente número está libre

        publicacion_nueva = Post(id_publicacion, titulo,
                                 nombre_usuario, fecha, precio, descripcion)
        user.posts.append(publicacion_nueva)
        with open('publicaciones.csv', 'w') as file:
            file.write('id_publicacion,nombre_publicacion,'
                       'usuario,fecha_creacion,precio,descripcion')
            for publi in Post.posts:
                file.write(f'\n{publi.id},{publi.titulo},{publi.username},'
                           f'{publi.fecha},{publi.precio},{publi.descripcion}')
        print('Publicación creada\n')

    elif respuesta_usuario == '2':
        print('\n¿Cuál publicación quieres borrar?')
        for i, post in enumerate(user.posts):
            print(f'\n[{i + 1}] {post.titulo} -- Creado el {post.fecha}')
        numero_publicacion = 0
        respuestas_posibles = []
        for numero in range(1, len(user.posts) + 1):  # Generador inputs posibles
            respuestas_posibles.append(str(numero))
        while numero_publicacion not in respuestas_posibles:
            numero_publicacion = input('\nSeleccione publicación: ')
            if numero_publicacion not in respuestas_posibles:
                print('Ingrese una respuesta válida >:(\n')
        post_a_eliminar = user.posts[int(numero_publicacion) - 1]
        for comment in Comment.comments:
            if comment.id == post_a_eliminar.id:
                Comment.comments.remove(comment)
        Post.posts.remove(post_a_eliminar)
        user.posts.remove(post_a_eliminar)

        with open('comentarios.csv', 'w') as file:
            file.write('id_publicacion,usuario,fecha_emision,contenido')
            for comentario in Comment.comments:
                file.write(f'\n{comentario.id},{comentario.username},'
                           f'{comentario.fecha},{comentario.contenido}')

        with open('publicaciones.csv', 'w') as file:
            file.write('id_publicacion,nombre_publicacion,'
                       'usuario,fecha_creacion,precio,descripcion')
            for publi in Post.posts:
                file.write(f'\n{publi.id},{publi.titulo},{publi.username},'
                           f'{publi.fecha},{publi.precio},{publi.descripcion}')
        print('Publicación eliminada\n')

    elif respuesta_usuario == '3':
        print('Volviendo a página anterior\n')
        estados_programa = cambio_de_estado('principal', estados_programa)

    return estados_programa


def abrir_publicacion(post, usuario):
    ver_publicacion = True
    while ver_publicacion:
        print(f"""
** {post.titulo} **

Creado:      {post.fecha}
Vendedor:    {post.username}
Precio:      {post.precio}
Descripción: {post.descripcion}

Comentarios de la publicación:""")
        for coment in post.comments:
            print(f'{coment.fecha} -- {coment.username}: {coment.contenido}')

        respuesta_usuario = '0'
        while respuesta_usuario not in ['1', '2']:
            respuesta_usuario = input('\n[1] Agregar comentario\t[2] Volver\n')
            if respuesta_usuario not in ['1', '2']:
                print('Ingrese un input válido.\n')
            if respuesta_usuario == '1' and not usuario:
                print('Para poder comentar, crea una cuenta en DCCommerce.\n')

        if respuesta_usuario == '1' and usuario:
            contendio = input('¿Qué quieres comentar?: ')
            fecha = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            comentario = Comment(post.id, usuario, fecha, contendio)
            post.comments.append(comentario)
            with open('comentarios.csv', 'w') as file:
                file.write('id_publicacion,usuario,fecha_emision,contenido')
                for comentario in Comment.comments:
                    file.write(f'\n{comentario.id},{comentario.username},'
                               f'{comentario.fecha},{comentario.contenido}')
        elif respuesta_usuario == '2':
            ver_publicacion = False


def cambio_de_estado(estado_deseado, estados_programa):
    for estado in estados_programa:
        if estado == estado_deseado:
            estados_programa[estado] = True
        else:
            estados_programa[estado] = False
    return estados_programa