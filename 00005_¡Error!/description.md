Si bien partimos de la suposición que nuestros datos deberían caer sobre una recta que describe la relación entre nuestras variables, las observaciones nunca rara vez cumplirán con esta idealidad :disappointed:. Como cada valor valor se aparta de la _recta ideal_ en un valor aleatorio de error (`ε`), es que la ecuación general correspondiente a un modelo de regresión lineal simple será más bien la siguiente:

<pre>
<code>f(x) = b + m * x + ε</code>
</pre>

Esta ecuación es frecuente también verla expresada en términos vectoriales, relacionando los valores que `x` e `y` toman como una serie de `i` observaciones, donde para cada una ellas se cumple que:  

<pre>
<code>y<sub>i</sub> = β<sub>0</sub> + β<sub>1</sub> * x<sub>i</sub> + ε<sub>i</sub></code>
</pre>

Análogamente, <code>β<sub>0</sub></code> se corresponde con la ordenada al origen (es decir, el valor de y cuando las demás variables son cero), <code>β<sub>1</sub></code> con el efecto promedio que tiene el cambio en `x` sobre `y` y <code>ε<sub>i</sub></code> con la distancia entre nuestra recta ideal y cada observación.



