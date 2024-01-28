import os
import datetime


def logger(old_function):
    def new_function(*args, **kwargs):

        with open('main.log', 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'{timestamp} - ')


            file.write(f'{old_function.__name__} - ')


            arguments = ", ".join(
                [str(arg) for arg in args] +
                [f'{key}={value}' for key, value in kwargs.items()]
            )
            file.write(f'Called with arguments: {arguments} - ')


            return_value = old_function(*args, **kwargs)
            file.write(f'Returned: {return_value}\n')

            return return_value

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

test_1()