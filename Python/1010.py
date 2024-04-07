
cod1,npeca1,vapeca1=input().split()
npeca1 = float(npeca1)
vapeca1 = float(vapeca1)

cod2,npeca2,vapeca2=input().split()
npeca2 = float(npeca2)
vapeca2 = float(vapeca2)


result = (npeca1*vapeca1)+(npeca2*vapeca2)

print(f"VALOR A PAGAR: R$ {result:.2f}")
