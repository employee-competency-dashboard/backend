import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Данные для вставки

team_data = [
    (1, 'Разработка', 'https://www.atlassian.com/ru/software/confluence/1/', 'https://www.atlassian.com/ru/software/jira/1/', 1, 2),
    (2, 'Разработка', 'https://www.atlassian.com/ru/software/confluence/2/', 'https://www.atlassian.com/ru/software/jira/2/', 3, 4)
]

# Вставка данных

cursor.executemany('INSERT INTO users_skills_team VALUES (?, ?, ?, ?, ?, ?)',
                   team_data)

# Сохранение изменений и закрытие соединения

employee_data = [
    (1, 'Сергей', 'Петров', 'Тестировщик (QA)', 'Junior', 'да', '/user-photo1.jpg'),
    (2, 'Мария', 'Лебедева', 'Менеджер проекта', 'Junior', 'нет', '/user-photo2.jpg'),
    (3, 'Иван', 'Новиков', 'Аналитик', 'Junior', 'да', '/user-photo3.jpg'),
    (4, 'Анна', 'Иванова', 'Тестировщик (QA)', 'Junior', 'да', '/user-photo4.jpg')
]
cursor.executemany('INSERT INTO users_skills_employee VALUES (?, ?, ?, ?, ?, ?, ?)',
                   employee_data)

employee_skill_data = [
    (1, 'Экспертный', 'да', '2024-Q1', 1, 1),
    (2, 'Уверенный', 'да', '2024-Q1', 2, 2),
    (3, 'Базовый', 'нет', '2024-Q3', 3, 3),
    (4, 'Экспертный', 'да', '2024-Q2', 4, 4)
]
cursor.executemany('INSERT INTO users_skills_employee_skills VALUES (?, ?, ?, ?, ?, ?)',
                   employee_skill_data)

expertise_data = [
    (1, 'Контейнеризация'),
    (2, 'Методологии управления проектами'),
    (3, 'Работа с базами данных'),
    (4, 'Frontend разработка')
]
cursor.executemany('INSERT INTO users_skills_expertise VALUES (?, ?)',
                   expertise_data)

skill_data = [
    (1, 'Docker', 'hard-skill', 1),
    (2, 'Agile', 'soft-skill', 2),
    (3, 'SQL', 'hard-skill', 3),
    (4, 'React', 'hard-skill', 4)
]
cursor.executemany('INSERT INTO users_skills_skill VALUES (?, ?, ?, ?)',
                   skill_data)

skill_for_grade_data = [
    (1, 'Junior', 'Экспертный', 1),
    (2, 'Junior', 'Уверенный', 2),
    (3, 'Junior', 'Экспертный', 3),
    (4, 'Middle', 'Экспертный', 4)
]
cursor.executemany('INSERT INTO users_skills_skill_for_grade VALUES (?, ?, ?, ?)',
                   skill_for_grade_data)

team_s_employees_data = [
    (1, 1, 1),
    (2, 2, 1),
    (3, 3, 2),
    (4, 4, 2)
]
cursor.executemany('INSERT INTO users_skills_team_s_employees VALUES (?, ?, ?)',
                   team_s_employees_data)

team_s_skills_data = [
    (1, 'да', 'Экспертный', 4, 1, 1),
    (2, 'нет', 'Уверенный', 2, 2, 1),
    (3, 'да', 'Экспертный', 4, 3, 2),
    (4, 'да', 'Экспертный', 4, 4, 2)
]
cursor.executemany('INSERT INTO users_skills_team_s_skills VALUES (?, ?, ?, ?, ?, ?)',
                   team_s_skills_data)

user_s_teams_data = [
    (1, 'edit', 1, 1),
    (2, 'view', 2, 1),
    (3, 'edit', 3, 2),
    (4, 'edit', 4, 2)
]
cursor.executemany('INSERT INTO users_skills_user_s_teams VALUES (?, ?, ?, ?)',
                   user_s_teams_data)

conn.commit()
conn.close()   
