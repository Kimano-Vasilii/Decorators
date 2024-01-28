import os
from datetime import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(path, "a+") as file:
                file.write(f"Timestamp: {timestamp}\n")
                file.write(f"Function Name: {old_function.__name__}\n")
                file.write(f"Arguments: args={args}, kwargs={kwargs}\n")

                result = old_function(*args, **kwargs)


                file.write(f"Return Value: {result}\n\n")

            return result

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"