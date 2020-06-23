# PruebaTecnica
to use:
docker-compose up
post to:
http://127.0.0.1:5000/{{ejercicio}}
ejercicio = {iterador_celdas_libres, maximo_rectangulo, maximo_cuadrado}


ejemplo:
curl --location --request POST 'http://127.0.0.1:5000/maximo_cuadrado' \
--header 'Content-Type: text/plain' \
--data-raw \
'1 0 0 0 
0 0 0 0 
1 0 0 0 '

curl --location --request POST 'http://127.0.0.1:5000/maximo_cuadrado' \
--header 'Content-Type: text/plain' \
--data-raw \
'1 2
1 0 0 0 
0 0 0 0 
1 0 0 0 '
