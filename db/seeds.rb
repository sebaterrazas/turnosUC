# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

martin = User.create!(username: 'Martín Jara', email: 'martin@gmail.com', password: '123456')
martin.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/martin.png')),
    filename: 'martin.png')
manuel = User.create!(username: 'Manuel Jouanne', email: 'manuel@gmail.com', password: '123456')
manuel.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/manuel.png')),
    filename: 'manuel.jpg')
seba  = User.create!(username: 'Seba Terrazas', email: 'seba@gmail.com', password: '123456')
seba.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/seba.png')),
    filename: 'seba.jpg')
andres = User.create!(username: 'Andrés Pinto', email: 'andres@gmail.com', password: '123456')
andres.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/andres.jpg')),
    filename: 'andres.jpg')
esteban = User.create!(username: 'Esteban', email: 'esteban@gmail.com', password: '123456')
esteban.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/esteban.jpg')),
    filename: 'esteban.jpg')
elena = User.create!(username: 'Elena', email: 'elena@gmail.com', password: '123456')
elena.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/elena.jpg')),
    filename: 'elena.jpg')
sully = User.create!(username: 'Sully', email: 'sully@gmail.com', password: '123456')
sully.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/sully.jpg')),
    filename: 'sully.jpg')
drake = User.create!(username: 'Drake', email: 'drake@gmail.com', password: '123456')
drake.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/drake.jpg')),
    filename: 'drake.jpg')
laura = User.create!(username: 'Laura Smith', email: 'laura@gmail.com', password: '123456')
laura.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/laura.jpg')),
    filename: 'laura.jpg')
benja = User.create!(username: 'Benja', email: 'benja@gmail.com', password: '123456')
benja.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/benja.jpg')),
    filename: 'benja.jpg')
cata = User.create!(username: 'Cata', email: 'cata@gmail.com', password: '123456')
cata.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/cata.jpg')),
    filename: 'cata.jpg')
agustin = User.create!(username: 'Agustín Andrade', email: 'agustin@gmail.com', password: '123456')
agustin.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/agustin.jpg')),
    filename: 'agustin.jpg')
cristian = User.create!(username: 'Cristian Soto', email: 'cristian@gmail.com', password: '123456')
cristian.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/cristian.jpg')),
    filename: 'cristian.jpg')
ignacio = User.create!(username: 'Ignacio', email: 'ignacio@gmail.com', password: '123456')
ignacio.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/ignacio.jpg')),
    filename: 'ignacio.jpg')
nico = User.create!(username: 'Nico López', email: 'nico@gmail.com', password: '123456')
nico.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/nico.jpg')),
    filename: 'nico.jpg')
isi = User.create!(username: 'Isi Rojas', email: 'isi@gmail.com', password: '123456')
isi.profile_pic.attach(io: File.open(Rails.root.join('app/assets/images/isi.jpg')),
    filename: 'isi.jpg')
tomas = User.create!(username: 'Tomás', email: 'tomas@gmail.com', password: '123456')
elisa = User.create!(username: 'Elisa', email: 'elisa@gmail.com', password: '123456')
max = User.create!(username: 'Max', email: 'max@gmail.com', password: '123456')
lucho = User.create!(username: 'Lucho', email: 'lucho@gmail.com', password: '123456')
ignacia = User.create!(username: 'Ignacia', email: 'ignacia@gmail.com', password: '123456')
jose = User.create!(username: 'José Tomás', email: 'josetomas@gmail.com', password: '123456')
sofi = User.create!(username: 'Sofi Alvarado', email: 'sofi@gmail.com', password: '123456')
will = User.create!(username: 'Will Smith', email: 'will@gmail.com', password: '123456')
camila = User.create!(username: 'Camila', email: 'camila@gmail.com', password: '123456')


###### TURNO 1 ########
turno1 = Turno.create!(datetime: '2022-06-22 15:30', is_it_return: 0, arrival_address: 'Casa Central', departure_address: 'Valle Escondido', seats: 4, status: 'Finished' ,driver: manuel)
request1_1 = Request.create!(description: 'Siuuu', state: 'Accepted', requester: martin, turno: turno1)
request1_2 = Request.create!(description: '', state: 'Accepted', requester: camila, turno: turno1)
request1_3 = Request.create!(description: 'I need a one ride', state: 'Pending', requester: laura, turno: turno1)
request1_4 = Request.create!(description: '', state: 'Accepted', requester: sofi, turno: turno1)
request1_5 = Request.create!(description: 'Que pasa bro', state: 'Pending', requester: seba, turno: turno1)
message1_1 = Message.create!(text: 'Holaa, donde estás?', user: martin, turno: turno1)
message1_2 = Message.create!(text: 'Llego en 10 min más, es que habia taco', user: manuel, turno: turno1)
message1_3 = Message.create!(text: 'Okaa', user: martin, turno: turno1)
review1_1 = Review.create!(qualification: 4, content: 'Muy bueno en general, pero se atrazó y llegué tarde a mi prueba', reviewer: martin, turno: turno1)
review1_2 = Review.create!(qualification: 3, content: '#@%&', reviewer: sofi, turno: turno1)
review1_3 = Review.create!(qualification: 5, content: 'Buenísimo!', reviewer: camila, turno: turno1)

###### TURNO 2 ######
turno2 = Turno.create!(datetime: '2022-07-04 12:50', is_it_return: 0, arrival_address: 'San Joaquín', departure_address: 'La Reina', seats: 3, status: 'Scheduled', driver: seba)
request4 = Request.create!(description: '¿Qué tal?', state: 'Accepted', requester: manuel, turno: turno2)

###### TURNO 3 ######
turno3 = Turno.create!(datetime: '2022-07-05 11:30', is_it_return: 1, arrival_address: 'Lo Barnechea', departure_address: 'San Joaquín', seats: 6, status: 'Scheduled', driver: martin)
request3_1 = Request.create!(description: '¿Qué tal?', state: 'Accepted', requester: seba, turno: turno3)
request3_2 = Request.create!(description: '', state: 'Pending', requester: manuel, turno: turno3)

###### TURNO 4 ######
turno4 = Turno.create!(datetime: '2022-06-25 12:50', is_it_return: 0, arrival_address: 'Lo Contador', departure_address: 'Los Ángeles', seats: 4, status: 'Scheduled', driver: will)
request4_1 = Request.create!(description: '¿Qué tal?', state: 'Accepted', requester: martin, turno: turno4)
request4_2 = Request.create!(description: '¿Qué tal?', state: 'Accepted', requester: manuel, turno: turno4)
request4_2 = Request.create!(description: '¿Qué tal?', state: 'Accepted', requester: seba, turno: turno4)

###### TURNO 5 ######
turno5 = Turno.create!(datetime: '2022-06-20 18:30', is_it_return: 1, arrival_address: 'La Moneda', departure_address: 'Lo Contador', seats: 2, status: 'Finished', driver: elena)
request5_1 = Request.create!(description: '', state: 'Accepted', requester: ignacio, turno: turno5)
request5_2 = Request.create!(description: '', state: 'Accepted', requester: sully, turno: turno5)
request5_3 = Request.create!(description: "oli", state: 'Accepted', requester: max, turno: turno5)


###### TURNO 6 ######
turno6 = Turno.create!(datetime: '2022-06-24 11:30', is_it_return: 0, arrival_address: 'Casa Central', departure_address: 'Copec Los Trapenses', seats: 3, status: 'Travelling', driver: seba)
request6_1 = Request.create!(description: '', state: 'Accepted', requester: martin, turno: turno6)
request6_2 = Request.create!(description: '', state: 'Accepted', requester: manuel, turno: turno6)
request6_3 = Request.create!(description: "Porfa acéptame…", state: 'Pending', requester: elena, turno: turno6)
message6_1 = Message.create!(text: 'No quiero llegar tarde a la presentación de software', user: martin, turno: turno6)
message6_2 = Message.create!(text: 'Yo creo que ponen un 1 si llegamos tarde', user: manuel, turno: turno6)
message6_3 = Message.create!(text: 'Dale, voy a salir 10 min más temprano más temprano para estar seguros', user: seba, turno: turno6)
message6_4 = Message.create!(text: 'Oka :)', user: martin, turno: turno6)

###### TURNO 7 ######
turno7 = Turno.create!(datetime: '2022-06-24 8:30', is_it_return: 0, departure_address: 'Avenida Chicureo, Chicureo, Chile', arrival_address: 'San Joaquín', seats: 4, status: 'Scheduled', driver: manuel)
request7_1 = Request.create!(description: '', state: 'Accepted', requester: elena, turno: turno7)
request7_2 = Request.create!(description: 'Tengo que llegar puntual', state: 'Accepted', requester: sully, turno: turno7)
request7_3 = Request.create!(description: "Yooo porfa", state: 'Pending', requester: drake, turno: turno7)
message7_1 = Message.create!(text: 'Voy a salir a las 7 de mi casa', user: manuel, turno: turno7)
message7_2 = Message.create!(text: 'Perfect', user: elena, turno: turno7)
message7_3 = Message.create!(text: 'Okaaa', user: sully, turno: turno7)
message7_4 = Message.create!(text: 'Me atrasé un poco', user: manuel, turno: turno7)

###### TURNOS ######
turno8 = Turno.create!(datetime: '2022-06-20 17:00', is_it_return: 1, arrival_address: 'Jumbo La Reina', departure_address: 'San Joaquín', seats: 3, status: 'Finished' ,driver: martin)
turno9 = Turno.create!(datetime: '2022-06-21 10:00', is_it_return: 0, arrival_address: 'Casa Central', departure_address: 'Copec Providencia', seats: 4, status: 'Finished' ,driver: ignacio)
turno10 = Turno.create!(datetime: '2022-06-22 10:00', is_it_return: 1, arrival_address: 'Copec Chicureo', departure_address: 'Lo Contador', seats: 3, status: 'Finished' ,driver: elena)
turno11 = Turno.create!(datetime: '2022-06-23 10:00', is_it_return: 0, arrival_address: 'Campus Oriente', departure_address: 'Rotonda Chamisero', seats: 2, status: 'Finished' ,driver: cata)
turno12 = Turno.create!(datetime: '2022-06-27 10:00', is_it_return: 1, arrival_address: 'Plaza de Lampa', departure_address: 'Casa Central', seats: 4, status: 'Scheduled', driver: martin)
turno13 = Turno.create!(datetime: '2022-06-28 10:00', is_it_return: 0, arrival_address: 'Casa Central', departure_address: 'Laguna San Bernardo', seats: 4, status: 'Scheduled', driver: agustin)
turno14 = Turno.create!(datetime: '2022-06-29 10:00', is_it_return: 1, arrival_address: 'Unimarc San Carlos', departure_address: 'Campus Oriente', seats: 3, status: 'Scheduled', driver: cristian)
turno15 = Turno.create!(datetime: '2022-06-30 10:00', is_it_return: 0, arrival_address: 'Lo Contador', departure_address: 'Cruce Santiago', seats: 6, status: 'Scheduled' ,driver: nico)
turno16 = Turno.create!(datetime: '2022-06-27 10:00', is_it_return: 1, arrival_address: 'Plaza Maipú', departure_address: 'Casa Central', seats: 1, status: 'Scheduled', driver: manuel)


AdminUser.create!(email: 'admin@example.com', password: 'password', password_confirmation: 'password') if Rails.env.development?
AdminUser.create!(email: 'admin1@example.com', password: 'password', password_confirmation: 'password')
