from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo:str, numero_tarjeta:str):
        self.__correo = correo
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo(self):
        return self.__correo

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia:int):
        pass

    def _crear_nueva_membresia(self, nueva_membresia:int):
        if nueva_membresia == 1:
            return Basica(self.correo, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo, self.numero_tarjeta)
        
class Gratis(Membresia):
    costo = 0
    cantidad_dispositivos = 1
    
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia >= 1 and nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self

class Basica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo:str, numero_tarjeta:str):
        super().__init__(correo, numero_tarjeta)
        if isinstance(self, Pro):
            self.__dias_regalo = 15
        elif isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7

        
    @property
    def dias_regalo(self):
        return self.__dias_regalo
    
    #Se añade para heredarlos a todas las clases hijas
    def cancelar_suscripcion(self):
        return Gratis(self.correo, self.numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia >= 2 and nueva_membresia <= 4:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
    

class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5
    
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia in [1,3,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
    
    def modificar_control_parental(self):
        pass
    

class SinConexion(Basica):
    costo = 3500
    cantidad_dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia in [1,2,4]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
    
    def incrementar_cantidad_offline(self):
        pass

class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia in [1,2,3]:
            return self._crear_nueva_membresia(nueva_membresia)
        else:
            return self
        
    def modificar_control_parental(self):
        pass

    def incrementar_cantidad_offline(self):
        pass