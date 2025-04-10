import matematicas
num1 = 10
num2 = 5

suma_resultado = matematicas.suma(num1,num2)
resta_resultado =matematicas.resta(num1,num2)
multiplicacion_resultado =matematicas.multiplicacion(num1,num2)
division_resultado =matematicas.division(num1,num2)

print(f"suma {suma_resultado}")
print(f"resta {resta_resultado}")
print(f"Multiplicación: {multiplicacion_resultado}")
print(f"División: {division_resultado}")

num3 = 0;
division_cero = matematicas.division(num1,num3)
print(f"División por cero: {division_cero}")