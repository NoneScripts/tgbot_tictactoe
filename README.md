# tgbot_tictactoe
Телеграм бот с крестиками ноликами на фреймворке аиограм

1. <b>Установка</b>
   ```cmd
   git clone https://github.com/NoneScripts/tgbot_tictactoe
   cd tgbot_tictactoe
   pip install -r requirements.txt
   ```
   Если у вас Linux система, то
   ```zsh
   git clone https://github.com/NoneScripts/tgbot_tictactoe
   cd tgbot_tictactoe
   ```
   ubuntu/debian
   ```zsh
   sudo apt install python3.9-distutils
   ```
   fedora/gentoo вам придётся самим разбираться как установить на fedora или gentoo aiogram==3.15.0 с помощью pip
   ```zsh
   pip install -r requirements.txt
   ```
   
   arch/mangaro
   ```zsh
   sudo pacman -S python-aiogram
   ```
   Если у вас есть проблемы с совместимостью, ищите в интернете - как установить aiogram 3.15.0 версии для "своего" дистрибутива
   
   Установите [git](https://git-scm.com/downloads) если не установлен
   
   или для Linux систем
   ```zsh
   sudo apt-get install git
   sudo pacman -S git
   sudo emerge --ask dev-vcs/git
   sudo dnf install git
   ```
   
   
2. <b>Получение токен бота (если знакомы - скипайте пункт)</b>

     Заходим в [@BotFather](https://t.me/BotFather)
     /start
     /newbot
     
     Он будет спрашивать это
     
     ![image](https://github.com/user-attachments/assets/c344dbc2-b0ae-4531-b7b4-6baa367ee7db)
   
     Задаём имя бота (как он будет подписан?) | Пример: NoneScripts
   
     ![image](https://github.com/user-attachments/assets/a425d88a-6dd0-43f6-8b4c-8cf5fd8a9e9b)
   
     Задаём пользовательское имя бота, на конце должен быть обязательно bot | Пример: nonescripts_bot
   
     ![image](https://github.com/user-attachments/assets/4d1d53d3-4706-41fa-a5c7-51f215189a5a)
   
     Нажимаем на голубой текст там где я замазал, чтобы скопировать токен (этот токен никому нельзя показывать, это ключ доступа к боту)
  
3. <b>Настройка</b>

   Заходим в файл setup.py
   
   Должно быть что-то вроде этого
   ```python
   import sqlite3
   
   config = {
       "token": "0"
   
   }
   def autosetting():
       with sqlite3.connect('database.db') as connect:
           cursor = connect.cursor()
           cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY,
                       score INTEGER NOT NULL,
                       money INTEGER NOT NULL
                       )""")
           connect.commit()
   ```
   там где 
   ```python
   config = {
       "token": "0"
   
   }
   ```
   вставляем свой токен между кавычками убирая цифру 0
   
   Сохраняем или ctrl + s
   
4. <b>Запуск</b>

   Установите [python](https://www.python.org/downloads/) если ещё не установлен
   
   для Linux
   ```zsh
   sudo emerge --ask dev-lang/python
   sudo pacman -S python
   sudo apt install python3
   sudo dnf install python3
   ```

   Запускаем файл main.py
   ```zsh
   python main.py
   ```
   Для fedora/debian/ubuntu
   ```zsh
   python3 main.py
   ```
   Убедитесь что python установлен и git
   ```zsh
   git --version
   python --version
   ```
   Для fedora/debian/ubuntu
   ```zsh
   python3 --version
   ```

   Заходим в своего бота которого вы создали и нажимаем "запустить" или пишем /start
   
   Если он отправляет вот это 
   
   ![image](https://github.com/user-attachments/assets/0cbbb177-a961-4b69-a524-a73d1f533c92)

   значит всё сделали правильно
   
   (согласен что превью "фу", сделано на коленках. Но я не дизайнер, поэтому по быстрому в блендере сделал)
## Полезные ссылки

[aiogram](https://docs.aiogram.dev/en/v3.15.0/)

[python](https://www.python.org/)

[git](https://git-scm.com/)

[BotFather](https://t.me/BotFather)
