# -*- coding: utf-8 -*-

from django.contrib.staticfiles.storage import staticfiles_storage

static = staticfiles_storage.url

statuses = {
    0: 'Не выполнено',
    1: 'На проверке',
    2: 'Проверенно',
    3: 'Просрочено'
}

task_statuses = {
    0: 'На проверке',
    1: 'Завершено'
}

avg_mark = 4.2

student = {
    'name': 'Афанасьева И.И.',
    'classname': '1Б',
    'img': static('img/account/avatar.png')
}

solutions = [
    {
        'task': {
            'id': 1,
            'title': 'Домашнее задание 1',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 0,
        'dateLoading': '04.05.2020',
        'mark': 5,
        'dateCheck': '05.05.2020',
        'markAI': 5,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    },
    {
        'task': {
            'id': 2,
            'title': 'Домашнее задание 2',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 1,
        'dateLoading': '04.05.2020',
        'mark': 3,
        'dateCheck': '05.05.2020',
        'markAI': 4,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    },
    {
        'task': {
            'id': 3,
            'title': 'Домашнее задание 3',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 2,
        'dateLoading': '04.05.2020',
        'mark': 4,
        'dateCheck': '05.05.2020',
        'markAI': 4,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    },
    {
        'task': {
            'id': 4,
            'title': 'Домашнее задание 4',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 3,
        'dateLoading': '04.05.2020',
        'mark': 2,
        'dateCheck': '05.05.2020',
        'markAI': 2,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    },
    {
        'task': {
            'id': 5,
            'title': 'Домашнее задание 1',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 0,
        'dateLoading': '04.05.2020',
        'mark': 5,
        'dateCheck': '05.05.2020',
        'markAI': 5,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    },
    {
        'task': {
            'id': 6,
            'title': 'Домашнее задание 2',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 1,
        'dateLoading': '04.05.2020',
        'mark': 3,
        'dateCheck': '05.05.2020',
        'markAI': 4,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    },
    {
        'task': {
            'id': 7,
            'title': 'Домашнее задание 3',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 2,
        'dateLoading': '04.05.2020',
        'mark': 4,
        'dateCheck': '05.05.2020',
        'markAI': 4,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    },
    {
        'task': {
            'id': 8,
            'title': 'Домашнее задание 4',
            'description': 'Выполните задание со страницы 4',
            'deadline': '05.05.2020'
        },

        'status': 3,
        'dateLoading': '04.05.2020',
        'mark': 2,
        'dateCheck': '05.05.2020',
        'markAI': 2,
        'img': static('img/bg.jpg'),
        'fileName': 'jopfec.jpg',

        'student': {
            'name': 'Афанасьева И.И.',
            'position': '1Б',
            'img': static('img/account/avatar.png')
        }
    }
]

teacher = {
    'name': 'Карл Тимофеевич',
    'img': static('img/account/avatar.png'),

    'tasks': [
        {
            'id': 1,
            'deadline': '05.05.2020',
            'status': 1,
            'donePercent': 78,
            'notSendedPercent': 22,
            'solutions': [
                {
                    'dateLoading': '04.05.2020',
                    'mark': 5,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 92,

                    'student': {
                        'name': 'Афанасьева И.И.',
                        'img': static('img/account/avatar.png')
                    }
                },
                {
                    'dateLoading': '04.05.2020',
                    'mark': 2,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 44,

                    'student': {
                        'name': 'Данелюк И.И.',
                        'img': static('img/account/avatar.png')
                    }
                },
                {
                    'dateLoading': '04.05.2020',
                    'mark': 2,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 44,

                    'student': {
                        'name': 'Афанасьева И.И.',
                        'img': static('img/account/avatar.png')
                    }
                },
                {
                    'dateLoading': '04.05.2020',
                    'mark': 4,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 81,

                    'student': {
                        'name': 'Данелюк И.И.',
                        'img': static('img/account/avatar.png')
                    }
                }
            ]
        },
        {
            'id': 2,
            'deadline': '05.05.2020',
            'status': 0,
            'donePercent': 5,
            'checkPercent': 80,
            'notSendedPercent': 15,
            'solutions': [
                {
                    'dateLoading': '04.05.2020',
                    'markAI': 2,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 30,

                    'student': {
                        'name': 'Афанасьева И.И.',
                        'img': static('img/account/avatar.png')
                    }
                }
            ]
        },
        {
            'id': 3,
            'deadline': '05.05.2020',
            'status': 0,
            'donePercent': 90,
            'checkPercent': 0,
            'notSendedPercent': 10,
            'solutions': [
                {
                    'dateLoading': '04.05.2020',
                    'markAI': 2,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 30,

                    'student': {
                        'name': 'Афанасьева И.И.',
                        'img': static('img/account/avatar.png')
                    }
                },
                {
                    'dateLoading': '04.05.2020',
                    'markAI': 2,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 30,

                    'student': {
                        'name': 'Афанасьева И.И.',
                        'img': static('img/account/avatar.png')
                    }
                }
            ]
        },
        {
            'id': 4,
            'deadline': '05.05.2020',
            'status': 1,
            'donePercent': 100,
            'checkPercent': 0,
            'notSendedPercent': 0,
            'solutions': [
                {
                    'dateLoading': '04.05.2020',
                    'mark': 2,
                    'dateCheck': '05.05.2020',
                    'img': static('img/bg.jpg'),
                    'fileName': 'jopfec.jpg',
                    'percent': 30,

                    'student': {
                        'name': 'Афанасьева И.И.',
                        'img': static('img/account/avatar.png')
                    }
                }
            ]
        }
    ]
}
