def tarjetas(x,y):
    p= (x*12)
    m= (y*35)
    if p<m:
        return(p)
    elif m<p: 
        return(m)  

def main():
    #escribe tu código abajo de esta línea
    p=int(input('Dame la cantidad de pliegos de papel albanene: '))
    m=int(input('Dame la cantidad de plumones: '))
    r=tarjetas(p,m)
    print('El número máximo de tarjetas que se pueden hacer es: '+str(r))
    

if __name__=='__main__':
    main()
