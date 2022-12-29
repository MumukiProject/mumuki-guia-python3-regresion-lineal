🔮 Al trabajar con modelos predictivos, no solo es importante ajustarlos, sino también cuantificar su capacidad para predecir nuevas observaciones.

Para poder hacer esta evaluación, vamos a volver a entrenarlo, pero aplicando una metodología  muy frecuente en el campo del aprendizaje automático: separar los datos en dos conjuntos de datos, uno de entrenamiento (`train`) y otro de prueba (`test`). 

Esto lo resolveremos con la ayuda de la función `train_test_split` de `sklearn`, que partcionará nuestras `X` e `y`, cada una, en dos conjuntos: 

```python
X = diabetes[['body_mass_index']]
y = diabetes['response']

X_train, X_test, y_train, y_test = train_test_split(
                                        X.values.reshape(-1,1),
                                        y.values,
                                        train_size   = 0.8,
                                        random_state = 1, 
                                        shuffle      = True
                                    )
```                                    

Luego, usaremos el par `(X_train, y_train)` para ajustar los coeficientes de nuestro regresor:

```python
modelo = LinearRegression()
modelo.fit(X = X_train, y = y_train)
```
