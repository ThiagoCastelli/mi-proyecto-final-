from ejemplo.models import Familiar

Familiar(nombre="Trinidad", direccion="Tissera 2722", numero_pasaporte=41879047).save()
Familiar(nombre="Thiago", direccion="Arbolada", numero_pasaporte=41835285).save()
Familiar(nombre="Messi", direccion="París", numero_pasaporte=32890345).save()
Familiar(nombre="Nala", direccion="La calle", numero_pasaporte=10002442).save()

print("Se cargó con éxito los usuarios de pruebas")