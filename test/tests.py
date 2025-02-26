from ejercicios.ejercicio1 import validar_usuario
from ejercicios.ejercicio2 import calcular_puntuacion
from ejercicios.ejercicio3 import validar_email
from ejercicios.ejercicio4 import validar_telefono


def test_validar_usuario():
    # Casos inválidos
    assert validar_usuario("User!") == False    # Carácter especial
    assert validar_usuario("  Hello  ") == False  # Espacios
    assert validar_usuario("A") == False        # Muy corto
    assert validar_usuario("12345678910111212131415")== False  #Mas de 15 caracteres
    assert validar_usuario("abddefghijklmnopqrsruvwxyz")== False #Mas de 15 caracteres

    """
    casos validos
    Longitud entre 5 y 15 caracteres.
    Sin espacios.
    Solo letras (mayúsculas/minúsculas) y números.
    """
    assert validar_usuario("Laura2024") == True
    assert validar_usuario("Pedro5") == True
    assert validar_usuario("Andres") == True   
    assert validar_usuario("CAMILO") == True 
    assert validar_usuario("Diego") == True 
    print("Verificador test validar usuario") #Se hace para verificar que entra a la función


#ejercicio2************************************************************************************************

def test_calcular_puntuacion():
   assert calcular_puntuacion(100, True) == "Oro"
   assert calcular_puntuacion(200, True) == "Oro"
   assert calcular_puntuacion(500, True) == "Oro"
   assert calcular_puntuacion(100, False) == "Plata"
   assert calcular_puntuacion(500, False) == "Plata"
   assert calcular_puntuacion(50, True) == "Plata"
   assert calcular_puntuacion(99, True) == "Plata"
   assert calcular_puntuacion(49, False) == "Bronce"
   assert calcular_puntuacion(4, True) == "Bronce"
   assert calcular_puntuacion(1, True) == "Bronce"
   assert calcular_puntuacion(4, True) == "Bronce"
   print("Verificador test calcular puntacion") #Se hace para verificar que entra a la función 

#ejercicio3************************************************************************************************
def test_validar_email():
    # pruebas acertadas
    assert validar_email("test@example.com")==True
    assert validar_email("juan.perez@empresa.com") == True
    assert validar_email("andrez@gmail.com") == True
    assert validar_email("pepito123@gmail.com") == True

    #pruebas no acertadas
    assert validar_email("maria@dominio")== False #falta extensión
    assert validar_email("pedro#2024@mail.org")== False # no permitido hashtag en usuario
    assert validar_email("pedro#2024@mail.org00000")== False # supera el limite de la extension
    assert validar_email("@mail.org")== False # no tiene usuario
    assert validar_email("andres@ .org")== False # no tiene dominio
    assert validar_email("pedro2024@###.org")== False # el dominio tienen hashtag
    print("Verificador test validar mail") #Se hace para verificar que entra a la función 

    #ejercicio4************************************************************************************************

def test_validar_telefono():
    #pruebas correctas
    assert validar_telefono("+12-345-678-9111")== True
    assert validar_telefono("+34-562-201-1234")== True

    #pruebas incorrectas
    assert validar_telefono("+12-345-678-9")== False #falta digitos al final
    assert validar_telefono("+12-345-6-9111")== False #falta digitos ante ultima
    assert validar_telefono("+12-3-678-9111")== False #falta digitos ante ante ultima
    assert validar_telefono("+1-345-678-9")== False #falta digitos al principio
    assert validar_telefono("12-345-678-9111")== False #falta el simbolo +
    assert validar_telefono("+12-345-678-")== False #falta digitos al final
    assert validar_telefono("+12-345-678-9111111")== False #sobran digitos al final
    assert validar_telefono("+12111111-345-678-9111")== False #sobran digitos al inicio


    print("Verificador test validar telefono") #Se hace para verificar que entra a la función 