Si bien partimos de la suposición que nuestros datos deberían caer sobre una recta que describe la relación entre nuestras variables, las observaciones nunca rara vez cumplirán con esta idealidad. Como cada valor valor se aparta de la "recta ideal" en un valor aleatorio de error (ϵ), es que la ecuación general correspondiente a un modelo de regresión lineal simple será más bien la siguiente:

```
f(x) = b + m * x + ϵ
```

Esta ecuación es frecuente también expresada en términos vectoriales, relacionando los valores X e Y de cada una las i observaciones:  

```
Yi = β0 + β1 * xi + ϵi
```

Nuevamente, β0 se corresponde con la ordenada al origen (es decir, el valor de y cuando las demás variables son cero), βi con el efecto promedio que tiene el cambio en X sobre Y y ϵi con la distancia entre nuestra recta ideal y cada observación. 
