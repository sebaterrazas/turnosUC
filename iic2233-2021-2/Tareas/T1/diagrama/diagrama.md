# Diagrama de clases T1

La relación entre las clases de este programa sigue al diagrama 
representado en ```diagrama_de_clases.pdf```.

En este se ve como están las clases Arena, Tributo, Ambiente, 
Playa, Montana, Bosque, Objeto, Arma, Consumible, y Especial.

La clase Arena es la clase de mayor jerarquía, al tener una relación
de composición con Tributo y Ambiente, significando que si se elimina 
un objeto de Arena, todas las demás objetos de las otras clases dejarán
de existir.

La clase Tributo es la que representará a los personajes que participan
en Los Juegos del Hambre, incluido al usuario. Este tiene una relación de
agregación con la clase Objeto.

La clase Objeto es abstracta y sirve de molde para Arma, Consumible, Especial.
Es por esto que su relación es de herencia. En estas clases hijas se redefinirá
(overriding) el método abstracto entregar_beneficio. La clase Especial también
heredará de Arma y Consumible, para así aprovechar el método de entregar_beneficio
de ambos. Esto genera que Especial entregue el beneficio de Arma, Consumible y
beneficios propios.

La clase Ambiente es parecida a la clase Objeto, es abstacta y sirve de molde para 
las clases Playa, Montana y Bosque. En este caso, el único método que hay que hacer
override es el calcular_dano. Además, cada clase hija sobre-escribe ciertos atributos.