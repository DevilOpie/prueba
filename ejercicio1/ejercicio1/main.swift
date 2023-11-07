//
//  main.swift
//  ejercicios
//
//  Created by Javier González on 20/9/23.
//

import Foundation



print("Introduce el primer numero")
let firstNText : String = readLine()!
let firstN : Int = Int(firstNText)!

print("Introduce el segundo numero")
let secondNText : String = readLine()!
let secondN : Int = Int(secondNText)!

print("Introduce el tercer numero")
let thirdNText : String = readLine()!
let thirdN : Int = Int(thirdNText)!

print("Introduce el cuarto numero")
let fourthNText : String = readLine()!
let fourthN : Int = Int(fourthNText)!

print("Introduce el quinto numero")
let fifthNText : String = readLine()!
let fifthN : Int = Int(fifthNText)!

let finalAgregation : Int = firstN + secondN + thirdN + fourthN + fifthN
let average : Int = finalAgregation / 5
print("La media aritmetica de los numeros proporcionados es", average)

