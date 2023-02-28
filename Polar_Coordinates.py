from cmath import sqrt,phase
c = complex(input())

print (sqrt(pow(c.real,2)+pow(c.imag,2)).real)
print (phase(complex(c.real,c.imag)))
