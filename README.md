# Проект 3 — Уровень дохода (Adult Census)

Учебный проект по классификации годового дохода на данных переписи населения США.

## Файлы

- `income_level_project.ipynb` — полный ноутбук с базовым, основным и продвинутым блоками.
- `download_data.py` — загрузка исходного датасета Adult Census из UCI в файл `adult.csv`.
- `requirements.txt` — зависимости Python.

## Запуск

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python download_data.py
jupyter notebook
```

Откройте `income_level_project.ipynb` и выполните ячейки по порядку. Если `adult.csv` отсутствует, ноутбук также попробует загрузить данные автоматически.

## Что входит в проект

- EDA: `df.info()`, пропуски, дубликаты и доля классов.
- Стратифицированное разделение train/test.
- Pipeline + ColumnTransformer без утечки данных.
- SimpleImputer, OneHotEncoder и StandardScaler.
- Logistic Regression и Decision Tree.
- StratifiedKFold(5), сравнение class_weight и RandomOverSampler.
- Подбор порога на out-of-fold прогнозах train.
- Confusion matrix, метрики и анализ ошибок по группам.

## Ограничения

Это учебный эксперимент, а не система принятия кредитных решений. Данные исторические и могут содержать социальные смещения. Метрики на этой выборке не доказывают справедливость модели или её пригодность для реального банковского скоринга.
