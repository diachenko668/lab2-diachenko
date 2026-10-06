# Завершение пункта Projects

Issue: https://github.com/diachenko668/lab2-diachenko/issues/1
Диаграмма: `docs/git-workflow.png` и `docs/git-workflow.svg`.

Создание проекта через текущую интеграцию отклонено GitHub:
`Resource not accessible by integration (createProjectV2)`.
Проект и перемещение карточки в Done пока не выполнены.

## Через браузер под своей учётной записью

1. Открыть профиль diachenko668 → Projects → New project.
2. Выбрать Board; название: «Лабораторная работа № 2 — Git и GitHub».
3. В поле Status настроить значения `To Do`, `In Progress`, `Done`.
4. Через Add item добавить Issue #1 из репозитория lab2-diachenko.
   Если Issue закрыт, включить закрытые задачи в поиске.
5. Переместить карточку последовательно To Do → In Progress → Done.
6. Связать Project с репозиторием (Projects → Link a project).
7. Сделать снимок доски с Issue #1 в Done и добавить его в раздел 3.8 отчёта.

## Для автоматического продолжения

В защищённых настройках среды можно добавить персональный
`GH_PROJECTS_TOKEN` с разрешением управлять Projects (для classic PAT — scope `project`).
Не вставлять токен в репозиторий, команды отчёта или сообщения чата.
Для gh использовать `GH_TOKEN="$GH_PROJECTS_TOKEN" gh project ...` только
при наличии этой переменной; текущее репозиторное подключение не менять.
Сам факт добавления токена не доказывает доступ: сначала проверить
создание проекта, затем настройку Board и перемещение карточки.
