MAX_LENGTH_ABOUT_TEAM = 128
MAX_LENGTH_FIRSTNAME = 64
MAX_LENGTH_GRADE = 10
MAX_LENGTH_LASTNAME = 128
MAX_LENGTH_KEY_EMPLOYEE = 4
MAX_LENGTH_KEY_SKILL = 4
MAX_LENGTH_LEVEL = 16
MAX_LENGTH_NAME_EXPERTISE = 16
MAX_LENGTH_REQUIRED_LEVEL = 128
MAX_LENGTH_REQ_LEVEL_GRADE = 16
MAX_LENGTH_RIGHTS = 4
MAX_LENGTH_ROLE = 64
MAX_LENGTH_SKILL_NAME = 32
MAX_LENGTH_SKILL_TYPE = 16
MAX_LENGTH_STATUS = 64
MAX_LENGTH_URL_CONFLUENCE = 128
MAX_LENGTH_URL_JIRA = 128

GRADE = (
    (1, 'Senior'),
    (2, 'Middle+'),
    (3, 'Middle'),
    (4, 'Junior+'),
    (5, 'Junior'),
    (6, 'Intern')
)

LEVEL = (
    (1, 'Экспертный'),
    (2, 'Уверенный'),
    (3, 'Базовый'),
    (4, 'Начинающий'),
    (5, 'Не владеет')
)

RIGHT = (
    (0, 'view'),
    (1, 'edit')
)

SKILL_TYPE = (
    (1, 'hard-skill'),
    (2, 'soft-skill')
)

STATUS = (
    (0, 'Не соответствует'),
    (1, 'Соответствует'),
    (2, 'В процессе развития')
)
