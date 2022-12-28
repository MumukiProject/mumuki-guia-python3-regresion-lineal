Ajustar el modelo consiste en estimar, a partir de los datos disponibles:

- la recta que minimice la distancia entre mis datos y ésta
- encontrar los valores de los coeficientes de regresión que maximizan la probabilidad de que la recta prediga los valores observados.

El método  más utilizado para el ajuste del modelo lineal es el de mínimos cuadrados.

```python
X = diabetes[['body_mass_index']]
y = diabetes['response']

modelo = LinearRegression()
modelo.fit(X = X, y = y)
```

Podemos imprimir los valores de ordenada al origen (`intercept_`) y toda la información de nuestro modelo haciendo:

```python
print("Intercept:", modelo.intercept_)
print("Coeficiente:", list(zip(X.columns, modelo.coef_.flatten())))
```

> Probá el código anterior y respondé. ¿Cuál de las ecuaciones representa al modelo obtenido?