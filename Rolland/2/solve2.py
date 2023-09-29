def attack(c1, c2, e1, e2, N):
    if libnum.gcd(e1, e2) != 1:
        print ("Exponents e1 and e2 cannot be coprime")
        sys.exit(0)
    x,y,_=libnum.xgcd(e1,e2)
    val = (pow(c1,x,N) * pow(c2,y,N)) % Nreturn (val)bits=128