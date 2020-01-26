import Foundation

//String en una linea
var myString = "Bienvenido al curso de Swift"

//String en varias lineas (Se deben de colocar 3 comillas al inicio y al final)
var myMultipleString = """
Bienvenidos al curso de Swift

Espero que les parezca interezante el curso
"""

//String en una sola linea (Se deben de colocar 3 comillas al inicio y al final)
var myFalseMultipleString = """
Bienvenidos al curso de Swift\
\
Espero que les parezca interezante el curso
"""

//String vacio
var myEmptyString = ""
var myEmptyString2 = String()

//Caracter usando Unicode
var myCaracter = "\u{E9}"
var myCaracter2 = "\u{24}"

//Caracteres especiales (\n, \r, \t, \0, \')
myString = "Bienvenidos al\n curso de Swift"

//Emojis (Para agregar emojis directamente -> Ctrl + Cmd + Espacio)
var myEmoji = "\u{1F496}"
var myEmoji2 = "🧐"

//Concatenacion
myString = "Bienvenidos" + " al curso de Swift"
myString += "\n¿Les está gustando?"

//Interpolación (Colocando valores de una variable en un String)
let name = "Javier"
let country = "México"
let myPersonalInfo = "Mi nombre es \(name) y vivo en \(country)"

//Comparacion
let name1 = "Javier"
let name2 = "Juan"
let name3 = "Javier"

name1 == name2  //false
name1 == name3  //true

//Checa si el String contiene a otro
let myContent = "Mi nombre es Javier"
myContent.contains(name)    //true

//Vacia
myEmptyString.isEmpty   //true

//Recorrido
for valor in myContent
{
    print(valor)
}