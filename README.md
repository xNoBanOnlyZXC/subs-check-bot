
<div align="center">
    <h1>SubsCheckBot</h1>
    <img alt="code size" src="https://img.shields.io/github/languages/code-size/xnobanonlyzxc/subs-check-bot?style=for-the-badge">
    <img alt="repo stars" src="https://img.shields.io/github/stars/xnobanonlyzxc/subs-check-bot?style=for-the-badge">
    <img alt="repo stars" src="https://img.shields.io/github/commit-activity/w/xnobanonlyzxc/subs-check-bot?style=for-the-badge">
</div>

## Настройка бота

В файле config.py нужно поставить токен бота в переменную TOKEN
Получить токен можно у https://t.me/BotFather

В переменную CHANNEL_IDS вставьте ссылки на каналы, пример:

#### Есть 2 канала, ссылки:

`https://t.me/NoBanOnly`
`https://t.me/neuralmachine`

#### Ссылки преобразуются так:

`https://t.me/OnlySq -> OnlySq`

#### Дальше ссылки вставляются в переменную в виде списка:

`CHANNEL_IDS = ['OnlySq','neuralmachine']`

Также рекомендую настроить `welcome_text` (отправляется в ответ на /start) и `succ_text` (отправляется если все условия выполнены) по требованию

#### Бот запускается через main.py
