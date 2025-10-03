## Modificaciones de la gráfica del clima
<img width="1442" height="1200" alt="imagen" src="https://github.com/user-attachments/assets/7f2b783c-c802-472e-a03f-86d029cf31ed" />

Los cambios que realize fueron los siguientes:
 - Cambie las coordenadas, para que los datos fueran sobre el Monte Everest (Latitud: 27.9881°, Longitud: 86.9250°).
 - En lugar de la temperatura, estoy pidiendo la velocidad del viento, con el comando: windspeed_10m.
 - Ajusté los parametros para que me diera los datos de los ultimos 7 dias y las predicciones de los siguientes 7 dias, esto con el comando past_days=7 y forecast_days=7.

Con respecto a las gráficas los cambios que hice fueron:
 - En lugar de mostrar todos los datos que me regresa la API (porque son muchos y se amontonan las etiquetas), utilizé 1 de cada 5 datos para graficar, con el comando horas[0:len(horas):5].
 - Agregé la cuadrícula punteada, en la de línea con una transparencia de 0.2 y en la de barras del 0.5.
 - En el eje X, cambie las etiqueteas para que esten roatdas 90° y que no se amontonen, ademas estableci el tamaño de la fuente en 6.
 - Cambie los nombres de los gráficos y el nombre del eje Y de acuerdo a la información que muestran ahora.
 - 
 - En la gráfica de línea, cambié el marcador de la posición de un dato, de "o" a "^".
 - En la gráfica de línea, cambié el ancho de linea a .5.
 - En la gráfica de línea, cambié el color de la línea y de los puntos por "darkgoldenrod"
 - En la gráfica de barras, cambié el color de las barras a "goldenrod"
