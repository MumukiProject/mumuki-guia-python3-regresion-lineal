¡Excelente! :confetti_ball: 


```python
ムcorrelaciones['response']
age                          0.187889
sex                          0.043062
body_mass_index              0.586450 # <= esta es la correlación que nos interesa
average blood pressure       0.441484
total_serum_cholesterol      0.212022
low_density_lipoproteins     0.174054
high_density_lipoproteins   -0.394789
total_cholesterol            0.430453
blood_sugar_level            0.382483
response                     1.000000
```

Si nos basamos exclusivamente en la correlación, _parece_ que las personas con mayor [índice de masa corporal](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal) presentan un mayor desarrollo de la enfermedad. Esto lo podemos afirmar porque: 

  * En términos absolutos, la correlación entre estas dos variables es mayor a `0.5` (recordemos que `0` representa la no-correlación y `1`, la correlación máxima); 
  * Y además la correlación es de signo positivo, lo que indica una relación directa. 

Otra forma útil de visualizar estas correlaciones es mediante un [_mapa de calor_](https://es.wikipedia.org/wiki/Mapa_de_calor) 🥵, que asigne puntos más claros a aquellos pares con mayor correlación: 

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-regresion-lineal/master/assets/heatmap_1672264640360.png" alt="heatmap_1672264640360.png" width="auto" height="auto">

(:eyes: _observá la tercera columna de la última fila, o lo que es lo mismo, la tercera fila de la última columna_)

Para generarlo, podés hacer lo siguiente: 

```python
sns.heatmap(correlaciones.abs())
```

:wave: Probalo y nos vemos en el siguiente ejercicio.
  