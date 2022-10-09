# hillel_hw_5
## Описание домашки
Инициализоровать новый django проект с последней версией django:

зайти в папку репозитория

django-admin startproject <project_name> .
(точка в конце - путь куда положить файлы проекта, в данном случае - текущая папка)

В .gitignore не забыть добавить (удостовериться в наличии) файл базы данных, папку виртульаного окружения (если она в
папке проекта) и папку настроект среды разработки

Создать requirements.txt (или Pipfile + Pipfile.lock в зависимости от используемого)

Создать django приложение catalog (python manage.py startapp <app_name>) и добавить его в INSTALLED_APPS

Убедиться что SECRET_KEY будет взят из переменных окружения и НЕ будет храниться в репозитории (os.environ.get("
SECRET_KEY", "<def value>"))


# Реализовано
Создан django проект с названием core, создано приложение catalog и доавленно в INSTALLED_APPS. Secret key берется из env. 