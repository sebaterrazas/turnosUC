from menu import menu_inicio, menu_principal, eleccion_personaje, \
    eleccion_arena, actualizar_tributos
from cargar_archivos import cargar_objetos, cargar_partida

if __name__ == '__main__':

    game_over_string = """
  ********      **     ****     **** ********
  **//////**    ****   /**/**   **/**/**///// 
 **      //    **//**  /**//** ** /**/**      
/**           **  //** /** //***  /**/******* 
/**    ***** **********/**  //*   /**/**////  
//**  ////**/**//////**/**   /    /**/**      
 //******** /**     /**/**        /**/********
  ////////  //      // //         // //////// 
   *******   **      ** ******** *******  
  **/////** /**     /**/**///// /**////** 
 **     //**/**     /**/**      /**   /** 
/**      /**//**    ** /******* /*******  
/**      /** //**  **  /**////  /**///**  
//**     **   //****   /**      /**  //** 
 //*******     //**    /********/**   //**
  ///////       //     //////// //     // 
"""
    victory_string = """
 **      ** **   ******  **********   *******   *******   **    **
/**     /**/**  **////**/////**///   **/////** /**////** //**  ** 
/**     /**/** **    //     /**     **     //**/**   /**  //****  
//**    ** /**/**           /**    /**      /**/*******    //**   
 //**  **  /**/**           /**    /**      /**/**///**     /**   
  //****   /**//**    **    /**    //**     ** /**  //**    /**   
   //**    /** //******     /**     //*******  /**   //**   /**   
    //     //   //////      //       ///////   //     //    //   
"""
    salir = False
    while not salir:
        inp = menu_inicio()
        if inp == 1 or inp == 2:
            arena = ''
            if inp == 2:  # Si el input es 2, se selecciona una partida guardada
                arena = cargar_partida()
            if inp == 1:  # Si el input del usuario es 1, el juego continua.
                personaje, rivales = eleccion_personaje()
                arena = eleccion_arena(personaje, rivales)
            objetos = cargar_objetos()
            game_over = False
            if not arena:
                game_over = True
            while not game_over:
                volver, salir = menu_principal(arena, objetos)
                actualizar_tributos(arena)
                if volver:
                    game_over = True
                    print('Saliendo de la simulación...')
                elif not arena.jugador.esta_vivo:
                    game_over = True
                    print(f'Tu personaje, {arena.jugador}, ha sido aniquilado :(')
                    print(game_over_string)
                elif not arena.tributos:
                    game_over = True
                    print(f'¡Enorabuena {arena.jugador}, haz ganado los juegos!')
                    print(victory_string)
        elif inp == 3:
            salir = True
        if salir:
            print('Cerrando el programa...')
