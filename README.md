# REAL-TIME ELECTION RESULTS: PORTUGAL 2019
Proyecto ML-Ops. Desarrollo y automatización de un problema de regresión

***Autor:** Alejandra Elizabeth Moreno Morales*

**Objetivo:**
Desarrollar, implementar y automatizar un modelo de aprendizaje automático usando el conjunto de datos: 'Real-time Election Results: Portugal 2019'.

**Acerca del Dataset:**
Conjunto de datos que describe la evolución de los resultados de las elecciones parlamentarias portuguesas del 6 de octubre de 2019. Los datos abarcan un intervalo de tiempo de 4 horas y 25 minutos, en intervalos de 5 minutos, sobre los resultados de los 27 partidos involucrados en las elecciones. 
El conjunto de datos está diseñado para tareas de modelado predictivo, principalmente centrado en tareas de pronóstico numérico, regresión ordinal y clasificación.

La Secretaria-Geral do Minist´erio da Administra¸c˜ao Interna (SGMAI) maneja los resultados de las elecciones procesos en Portugal. Estos resultados se publican en línea continuamente a medida que están disponibles. 
El proceso general de comunicación/publicación de resultados es el siguiente:
1. Los votos se cuentan cuando cierran las urnas;
2. Una vez finalizado el escrutinio de las secciones electorales, se recogen los resultados y se comunican a la SGMAI;
3. Los resultados se verifican y publican.
Los resultados de las elecciones parlamentarias de 2019 en Portugal se presentan en el siguiente sitio web. En este sitio web se publica lo que se considerados resultados provisionales. Los resultados finales se ponen a disposición después de un debido proceso por parte de las autoridades competentes.
Como tal, *este conjunto de datos se relaciona con dichos resultados provisionales*.

Cabe señalar que hubo dos procesos de adquisición de datos: un proceso en línea y otro fuera de línea. En otras palabras, cierta información (información a nivel de distrito) se adquiere mientras se publican los resultados, y otra información (información a nivel parroquial) adquirida después del proceso.

**Adquisición en línea**
Atributos recopilados en tiempo real relacionados con la información general del proceso electoral a nivel de distrito.
![image](https://github.com/aleksmoreno2/Real-time-Election-Results-Portugal-2019/assets/91718364/37082157-4804-4850-b0bb-afbe89aa58fa)

**Adquisición sin conexión**
Atributos recopilados fuera de linea relacionados con los datos de granularidad más fina.
![image](https://github.com/aleksmoreno2/Real-time-Election-Results-Portugal-2019/assets/91718364/c39b65b3-c03b-405e-8c98-5419f9487c45)

Los datos originales son sometidos a un proceso de limpieza y tratamiento de datos para análisis y trabajar la consistencia de la información, entrada/formato de los datos, errores y cuestiones relacionadas que puedan afectar su uso.
El tipo de datos en cada atributo del conjunto de datos final sobre los resultados electorales para el El Parlamento portugués en 2019 se presenta en la Tabla 3
![image](https://github.com/aleksmoreno2/Real-time-Election-Results-Portugal-2019/assets/91718364/0ae50493-d5e6-4897-9322-b1682049289d)

*Referencia: Moniz, N. (2019, December 5). Real-time 2019 Portuguese parliament election results dataset. arXiv.org. https://arxiv.org/abs/1912.08922*

**Acerca de la Pólitica en Portugal:**

La política en Portugal opera como una república democrática representativa semipresidencial, multipartidaria y unitaria, en la que el Primer Ministro de Portugal es el jefe de gobierno y el Presidente de Portugal es el jefe de estado no ejecutivo, con varios poderes políticos importantes que ejercen a menudo. .[1] El poder ejecutivo lo ejerce el Gobierno, cuyo líder es el Primer Ministro. El poder legislativo reside principalmente en la Asamblea de la República (el parlamento portugués), aunque el gobierno también puede legislar sobre determinadas materias.[2] El poder judicial de Portugal es independiente del ejecutivo y del legislativo. El Presidente ejerce una especie de "poder moderador", que no se puede clasificar fácilmente en ninguno de los tres poderes tradicionales del gobierno.[1]

Los gobiernos nacional y regional están dominados por dos partidos políticos, el Partido Socialista (PS), de centro izquierda, un partido socialdemócrata, y el Partido Socialdemócrata (PSD), de centro derecha y liberal-conservador.

 Otros partidos con escaños en el parlamento son Chega, el Partido Comunista Portugués, el Bloque de Izquierda, el Partido Ecologista "Los Verdes", LIVRE y Personas-Animales-Naturaleza. Los comunistas y los verdes están en coalición como Coalición Democrática Unitaria.

Referencia: https://en.wikipedia.org/wiki/Politics_of_Portugal

## ANÁLISIS EXPLORATORIO DE DATOS
Desarrollo en el jupyter notebook

## OBJETIVO DEL MODELO DE APRENDIZAJE AUTOMATICO
Determinar las características o variables que influyen en el número final de parlamentarios electos a nivel de distrito/nacional (FinalMandates) con el fin de establecer un modelo que sea capaz de predecir este valor.

## MOTIVACIÓN DE ESTRATEGIA ML-OPS 
El conjunto de fenómenos que rodean e influyen en los resultados electores son determinantes para entender el comportamiento del evento electoral de Portugal por lo que el análisis númerico y esadistico a través de un modelo de aprendizaje automatico lleva a la capacidad significativa de anticipación de los resultados finales.
La disposición de los datos,tanto historico como en tiempo real, da la oportunidad de crear un modelo que explique este fenómeno por lo que elaborar una modelo ML-Ops que permita automatizar el ciclo de vida del modelo que permita entrenar, desplegar y retroalimentar el mismo será decisivo para extender predicciones que se acoplen al comportamiento dinamico del evento.

## ARQUITECTURA DEL MODELO ML-OPS
![MLOPS flow](https://github.com/aleksmoreno2/Real-time-Election-Results-Portugal-2019/assets/91718364/ea48238e-9590-48d3-8b0a-1aa0ca2a90b8)

## MODELO DE PREDICCIÓN
Como parte de esta primera fase de desarrollo del proyecto se evaluarán los siguientes algoritmos:
1. Linear regression
2. Decision Tree
3. Random Forest

Con el fin de evaluar el rendimiento de los modelos de regresión lineal y determinar la relación entre las observaciones y los valores predichos se utilizaran las siguientes métricas:
* Error Cuadrático Medio (RMSE): Cantidad de error que hay entre el valor predicho y un valor observado o conocido.
* Coeficiente de determinación (R2): Medida de precisión del modelo. Cómo se ajusta el modelo de regresión a los datos reales.



## GESTIÓN DEL VERSIONAMIENTO DE DATOS Y MODELOS [DVC] [GIT]
1.	Instalación de paquetes
```
pip install dvc
pip boto3 dvc[all] dvc[s3]
```
2.	Inicializar DVC en la ubicación del proyecto
```
dvc init
```
```
git init
```
3.	Consultar estatus de cambios
```
dvc status
```
```
git status
```
4.	Agregar las carpetas o archivos  a los que se le dará seguimiento
```
dvc add [carpeta/archivo]
```
```
git add [carpeta/archivo
```
5.	Realizar commit de los cambios realizados
```
git commit -m “[mensaje]”
```
6.	Actualizar los cambios en el repositorio
```dvc push
```
```
git push origin master
```
7.	Considerar el uso de los siguientes comandos para cambiar entre las diferentes versiones de los datos
```
dvc checkout
```
```
git checkout
```


## GESTIÓN DEL ALMACENAMIENTO REMOTO [DVC] [BUCKET S3]

**Opcion 1. Actualizar archivo de configuración del proyecto**
1.	Agregar el almacenamiento remoto
```
dvc remote add -d remote [s3://…/]
```
2.	Agregar credenciales del servicio de almacenamiento S3
```
dvc remote modify remote access_key_id [AWS_ACCESS_KEY_ID]
dvc remote modify remote secret_access_key [AWS_SECRET_ACCESS_KEY]
```
3.	Actualizar los cambios
```
dvc push
```
```
git push origin master
```

**Opción 2. Configuración de AWS con aws cli**
1.	Asegurarse de tener instalado el paquete
```
pip install awscli
```
2.	En la terminal, ingresar
```
aws configure
```
3.	Actualizar los siguientes datos: Access key ID, Secret access key, AWS Region and Output format.
```
$ aws configure 
AWS Access Key ID [None]: [EXAMPLE]
AWS Secret Access Key [None]: [EXAMPLE/EXAMPLE] 
Default region name [None]: [EXAMPLE]
Default output format [None]: [EXAMPLE]
```
4.	Agregar credenciales del servicio de almacenamiento S3
```
dvc remote modify remote credentialpath ~/.aws/credentials
```
5.	Actualizar los cambios
```
dvc push
```
```
git push origin master
```


**Obtención de los datos y modelos**
Habiendo clonado el repositorio, instalado los paquetes de requerimiento y reemplazar las credenciales del almacenamiento de S3.
Ejecutar el comando:
```
dvc pull
```

## Referencias
* https://medium.com/analytics-vidhya/versioning-data-and-models-in-ml-projects-using-dvc-and-aws-s3-286e664a7209
* https://medium.com/analytics-vidhya/docker-volumes-with-dvc-for-versioning-data-and-models-for-ml-projects-4885935db3ec
* https://abdulsamodazeez.com/optimizing-machine-learning-workflows-containerization-versioning-with-dvc-and-cicd-automation#heading-resources
* https://dagshub.com/blog/ci-cd-for-machine-learning-test-and-and-deploy-your-ml-model-with-github-actions/

