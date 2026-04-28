# Wikipedia analysis

### Цель проекта

Проанализировать данные о просмотрах страниц Wikipedia в период с 01 по 08 марта 2026 года

### Задачи, выполняемые проектом

- Предобработка данных:
  - Преобразование формата .gz в .parquet;
  - очистка и подготовка данных;
- Исследовательский анализ данных (EDA);
- Развертывание PostgreSQL в Docker-контейнере
- Хранение данных:
  - Создание партиционированной таблицы (по дате)
  - Cоздание индексов и materialized view для ускорения выполнения запросов
  - Загрузка и организация данных для аналитики
- Анализ подготовленной витрины данных
- Создание дашбордов в BI Grafana
- Развертывание контейнера для локального запуска проекта в пределах репозитория Github
  
### Технологии

- Python (pandas, matplotlib.pyplot)
- PostgreSQL
- Docker / Docker Compose
- Grafana BI
- SQL
- Parquet

## Запуск проекта

1. Клонировать репозиторий:
```bash
git clone https://github.com/derswadert/wikipedia-analysis.git
cd wikipedia-analysis
```
2. Запустить контейнеры:
```bash
docker-compose up
```
3. Подключение к pgAdmin

Открыть в браузере: http://localhost:8081

Email: admin@admin.com
Пароль: admin

4. Подключение к базе данных в pgAdmin

Servers → Register → Server...

Вкладка General: 
- Name — 'любое'

Вкладка Connections: 
- Host name/address — postgres
- Port — 5432
- Maintenance database — portfolio
- Username — analyst
- Password — password123

5. Подключение к BI Grafana

Открыть в браузере: http://localhost:3001

Логин: admin
Пароль: admin

Connections -> Data Source -> Add new data Source

- Host URL — postgres:5432
- Database name — portfolio
- Username — analyst
- Password — password123

6. Импорт дашбордов

Dashboards -> New -> Import -> Upload 




  








<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/574a90c6-fcd3-4c27-9df6-1de23bf3d7f0" />
