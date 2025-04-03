#17) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.


numero1 = int(input("informe o primeiro numero"))
numero2 = int(input("informe o segundo numero"))
numero3 =int(input("informe o terceiro numero"))

if numero1 > numero2 and numero1 > numero3:
    print("primeiro é maior")
if numero2 > numero1 and numero2 > numero3:
    print ("segundo é maior")
else:
    print("terceira é meior")
