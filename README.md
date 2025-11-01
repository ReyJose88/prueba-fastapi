## Requisitos 
*   Python 3.12 o mayor
*   Docker (para la base de datos)
*   pip y un entorno virtual

## Instalación
1.	Clonar repo
	```bash
	git clone https://github.com/ReyJose88/prueba-fastapi.git
	cd prueba-fastapi
    dotnet run
    ```

2.	Crea y activa un entorno virtual
	```bash
	python -m venv venv
    ```

3.	Windows:
	```bash
	.\venv\Scripts\activate
	```

4.	Linux:
	```bash
	source venv/bin/activate
	```

5.	Instala dependencias:
	```bash
	pip install -r requirements.txt
	```

6.	Levanta la base de datos:
	```bash
	docker-compose up -d
	```

## Crea las tablas con Alembic:
alembic upgrade head


## Poner a correr el servidor
uvicorn app.main:app --reload

