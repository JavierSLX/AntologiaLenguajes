import UIKit

//Arrays
var arreglo: Array<String>
var array: [Int] = []
var arregloNumeros = [1, 2, 3]
let arreggloNumerosInmutable = [3, 2, 1]

//Agregando más elementos (al final del array y especificandole en que posicion)
arregloNumeros.append(5)
arregloNumeros.insert(4, at: 3)

//Eliminar valores
arregloNumeros.remove(at: 0)
arregloNumeros.removeLast()

//Accediendo al array
print(arregloNumeros)
print(arregloNumeros[2])

//Eliminar todo el arreglo
arregloNumeros.removeAll()
print(arregloNumeros)

//Diccionarios
var myClassicDictionary = Dictionary<Int, String>()
var myModernDictionary = [Int:String]()

//Agregando elementos
myModernDictionary[003] = "Javier"
myModernDictionary = [001:"Juan", 002:"Brais"]

//Accediendo al diccionario
myModernDictionary[002]

//Borrar dato
myModernDictionary[002] = nil
myModernDictionary.removeValue(forKey: 001)