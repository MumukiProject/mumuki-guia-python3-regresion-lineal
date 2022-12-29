El método  más utilizado para el ajuste del modelo lineal es el de mínimos cuadrados, que identifica como mejor modelo la recta (o plano si es regresión múltiple) que minimiza la suma de los cuadrados de los errores:

$ϵ^2  = ∑ (yi - ŷi)^2$

Es  decir,  la  suma  de  los  cuadrados  de  las  diferencias  entre  los  valores  reales  observados  (yi)  y los valores estimados (ŷi). Entonces podemos usar ese error como otro parámetro para entender la bondad del modelo.


¿Pero cómo podemos saber si las predicciones son buenas o malas? Pues podemos calcular el error, teniendo en cuenta el valor predicho y respecto de un valor observado o conocido. El error cuadrático medio (RMSE) mide la cantidad de error que hay entre dos conjuntos de datos:

```python
# gracias a la division train test, nos permite contrastar 
y_pred = modelo.predict(X = X_test)

rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = y_pred,
        squared = False
       )

print("El error (rmse) de test es:", rmse)

```

> Calculá el valor de `RMSE`