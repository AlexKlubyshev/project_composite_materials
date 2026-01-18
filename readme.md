# Прогнозирование конечных свойств новых материалов (композиционных материалов)

## Задача
На входе имеются данные о начальных свойствах компонентов композиционных материалов (количество связующего, наполнителя, температурный режим отверждения и т.д.). На выходе необходимо спрогнозировать ряд конечных свойств получаемых композиционных материалов.

## Данные
- **Размер:** 1023 строки, 12 признаков
- **Целевые переменные:** 'Модуль упругости при растяжении','Прочность при растяжении','Соотношение матрица-наполнитель' 

## Что сделано
1. **EDA и анализ корреляций**
2. **Кластеризация**
3. **Предобработка признаков:** StandardScaler, PolynomialFeatures, PCA
4. **Сравнение моделей** (кросс-валидация): Lasso,Ridge,Ridge+PolynomialFeatures,KNN,SVR(с RBF),SVR(с Poly),RandomForest, GradientBoosting   
5. **Подбор гиперпараметров:** GridSearchCV
6. **Проектирование архитектуры нейросети**
7. **интерпретация результатов** 
8. **Flask-приложение**

## Результаты
 
**Целевая переменная:** Прочность при растяжении
**Лучшая модель:**  GradientBoosting (R²=0.361, MAPE=15.22%) 

**Целевая переменная:** Модуль упругости при растяжении
**Лучшая модель:**  GradientBoosting (R²=0.161, MAPE=1.62%)

**Целевая переменная:** Соотношение матрица-наполнитель
**Лучшая модель:**  Нейросеть с 1 скрытым слоем из 12 нейронов (R² = 0.226, MAPE= 22.29%)

**Примечание:** Показатели низкие. Большинство данных в датасете оказались фальшивыми и реальный датасет сократился до 40 записей. Поэтому, для получения лучших результатов требуется более углубленная обработка признаков (Feature Engineering). 

## Стек технологий
Python, Pandas, NumPy, Scikit-learn, GradientBoosting, PolynomialFeatures, PCA, Matplotlib, Seaborn  

## Установка и запуск
### 1. Клонирование репозитория
git clone https://github.com/AlexKlubyshev/project_composite_materials.git<br>
cd project_composite_materials

### 2. Создание окружения используя conda(рекомендуемый способ) 
conda env create -f environment.yml
conda activate composite_materials

### 3. Альтернативная установка (через pip): 
   pip install -r requirements.txt

### 4. Проверка корректности установки пакетов
tests/test_import.py

### 5. Запуск проекта
jupyter notebook notebooks/composite_materials.ipynb

### 6. Flask-приложения
cd src<br>
python app.py

## Зависимости

Полный список зависимостей находится в файлах:
- environment.yml — для установки через conda
- requirements.txt — для установки через pip

## Основные библиотеки:

- Python 3.11
- pandas, numpy, scikit-learn
- shap, matplotlib, seaborn
- jupyterlab

## Структура проекта

project_composite_materials/<br>
├── data/ # Данные (или ссылки на них)<br>
├── notebooks/ # Jupyter ноутбуки<br>
│   └── composite_materials.ipynb<br>
├── src/<br>
│   ├── templates/ # Шаблоны web-страниц<br>
│   ├── app.py # Flask приложение<br>
│   └── process.py # Логика обработки<br>
├── tests/<br>
│   └── test_import.py<br>
├── models/<br> 
├── environment.yml # Conda environment<br>
├── requirements.txt # Pip requirements<br>
└── README.md

