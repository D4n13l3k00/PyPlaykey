<div align="center">

# 🐍 PyPlaykey 🎮

![Python version](https://img.shields.io/badge/python-v3.9.10-success)
![GitHub](https://img.shields.io/github/license/D4n13l3k00/PyPlaykey)
![CodeStyle](https://img.shields.io/badge/code%20style-black-black)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/D4n13l3k00/PyPlaykey/Client%20Updater?label=auto%20update%20client)

![GitHub repo size](https://img.shields.io/github/repo-size/D4n13l3k00/PyPlaykey)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/D4n13l3k00/PyPlaykey)

---

## Портативный лаунчер Playkey с поддержкой Linux 🐧 (Wine)

</div>

---

### ❓ Что он делает

- Данный лаунчер использует API Playkey, который был вручную разобран с сайта
- Запуск происходит через официальный клиент Playkey для Windows через Wine
- Для простоты запуска в лаунчере выбор игры реализован через терминал

---

### 📦 Установка зависимостей

```bash
python3 -m pip install -r requirements.txt
```

Так-же для работы требуется токен с [playkey.net](playkey.net).

Получить его можно через вкладку "Network" в Chrome.

В `Filter` вводим `https://api.playkey.net/rest/`, открываем любой запрос, открываем вкладку `payload` и ищем поле `token`. Если его нету, посмотрите в других запросах.

---

### 🚀 Запуск

```bash
python3 main.py
```
