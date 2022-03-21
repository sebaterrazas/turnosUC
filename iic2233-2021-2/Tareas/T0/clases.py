class User:
    users = list()  # Lista con todos los usuarios creados

    def __init__(self, name):
        self.name = name
        self.posts = list()
        User.users.append(self)


class Post:
    posts = list()  # Lista con todas las publicaciones creadas

    def __init__(self, id, titulo, username, fecha, precio, descripcion):
        self.id = id
        self.username = username
        self.descripcion = descripcion
        self.titulo = titulo
        self.precio = precio
        self.fecha = fecha
        self.comments = list()
        Post.posts.append(self)


class Comment:
    comments = list()  # Lista con todos los comentarios creados

    def __init__(self, id, username, fecha, contenido):
        self.id = id
        self.username = username
        self.fecha = fecha
        self.contenido = contenido
        Comment.comments.append(self)