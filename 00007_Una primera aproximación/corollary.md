¡Muy bien! Si nos basamos exclusivamente en la correlación, _parece_ que las personas con mayor índice de masa corporal presentan un mayor desarrollo de la enfermedad. Esto lo podemos afirmar porque: 

  * En términos absolutos, la correlación entre estas dos variables es mayor a `0.5` (recordemos que `0` representa la no-correlación y `1`, la correlación máxima); 
  * Y además la correlación es positiva, lo que indica una relación directa. 

Otra forma útil de visualizar estas correlaciones es mediante un _mapa de calor_, que asigna puntos más claros a aquellos pares con mayor correlación: 

```python
sns.heatmap(correlaciones.abs())
```

¡Probalo y continuá al siguiente ejercicio!
  