# QA-Example

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ssanga_QA-example&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ssanga_QA-example)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=ssanga_QA-example&metric=coverage)](https://sonarcloud.io/summary/new_code?id=ssanga_QA-example)

## Introducción

Este proyecto es un ejemplo completo de integración continua y despliegue para una API REST desarrollada con FastAPI. Incluye:
- Cobertura de tests unitarios con pytest y pytest-cov
- Análisis de calidad y cobertura de código con SonarQube/SonarCloud
- Despliegue automático en Azure App Service
- Ejemplo de configuración de pipelines CI/CD en GitHub Actions

## URLs del proyecto

- **Web desplegada en Azure:** [https://qa-example-fqhxccfwepagbhdb.northeurope-01.azurewebsites.net](https://qa-example-fqhxccfwepagbhdb.northeurope-01.azurewebsites.net)
- **SonarQube/SonarCloud:** [https://sonarcloud.io/summary/new_code?id=ssanga_QA-example](https://sonarcloud.io/summary/new_code?id=ssanga_QA-example)



## Librerías requeridas

- fastapi
- uvicorn
- httpx
- pytest
- pytest-cov
- gunicorn

Instala todas las dependencias con:

```
pip install -r requirements.txt
```


## SonarQube y cobertura de tests en Python

Para más información sobre cómo integrar la cobertura de tests de Python en SonarQube, consulta la documentación oficial:  
[https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/python-test-coverage/](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/python-test-coverage/)


