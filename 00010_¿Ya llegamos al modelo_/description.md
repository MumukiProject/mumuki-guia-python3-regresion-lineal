¿Terminamos? Sí y no. Si bien por un lado, establecer que existe un vínculo entre ambas variables (correlación ~~ 0.6) y que dicho vínculo no parece el mero producto del azar (p-value >> 0.05), y por otro pudimos aproximarlo a una recta, aún estamos lejos de haber evaluado completamente al modelo. 

Por ejemplo: ¿Cuán bueno es? ¿Los datos caen efectivamente en la recta? ¿Cuánto se alejan de ella?

Una primera aproximación a las dos primeras preguntas: 

```
# R2 is a measure of the goodness of fit of a model.[11] In regression, 
# the R2 coefficient of determination is a statistical measure of how well the regression predictions approximate
# the real data points. An R2 of 1 indicates that the regression predictions perfectly fit the data. 
print("Coeficiente de determinación R^2:", modelo.score(X, y)) 
```

En los modelos de regresión lineal simple el valor de R2 se corresponde con el cuadrado del coeficiente de correlación de Pearson (r) entre x e y, no siendo así en regresión múltiple.

> En base a este resultado. ¿Cuán bueno resultó el modelo?
