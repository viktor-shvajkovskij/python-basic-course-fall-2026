import ctypes
import gc

class MyObject:
    pass

obj1 = MyObject()
obj2 = MyObject()
obj1.ref = obj2
obj2.ref = obj1

id1 = id(obj1)
print(f"Объект создан с ID: {id1}")

del obj1
del obj2
print("Имена удалены...")

collected_count = gc.collect()
print(f"Сборщик мусора собрал объектов: {collected_count}")

print("Пытаемся получить доступ к освобожденной памяти...")
print(ctypes.cast(id1, ctypes.py_object).value)
