'''
tempo_perdido = 3h57min
número primo me mata, puta merda

'''

def questao14e15():
    qntDivisores = 0
    for i in range(1, numeroDiv+1):
        if numeroDiv % i == 0:
            print("%i é divisor do número informado" % i)
            qntDivisores+=1
    print("A quantidade de divisores foi de: %i"%qntDivisores)

def questao16(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print("%i não é um número primo" % num)
                print("%ix%i é %i"%(i, num//i, num))
                break
        else:
            print("%i é um número primo" % num)
    else:
        print("%i não é um número primo" % num)

def questao17e18(numero):
    numPrimos = []
    somaPrimos = 0
    for k in range(2, numero + 1):
       if k > 1:
           for j in range(2, k):
               if (k % j) == 0:
                   break
           else:
               numPrimos.append(k)
               somaPrimos += k
               
    print("Os números primos entre 1 e %i: ", numero, numPrimos)
    print("A soma de todos os primos de %i até %i é: %i" %(1, numero,somaPrimos))

numeroDiv = int(input("Digite um número a ser calculado o divisor: "))
questao14e15()

numeroPrimo = int(input("\nO número é primo? Digite aqui e veja: "))
questao16(numeroPrimo)
questao17e18(numeroPrimo)