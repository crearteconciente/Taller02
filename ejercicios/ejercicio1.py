def validar_usuario(nombre):
   if len(nombre) < 5 or len(nombre) > 15:
       return False
   if " " in nombre:
       return False
   for c in nombre:
       if not (c.isalnum() or c in ["_", "-"]):
           return False
   return True