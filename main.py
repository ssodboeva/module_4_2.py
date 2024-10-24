def test_function():
    def inner_function():
        print ('Я в области видимости функции test_function')
    inner_function() # функция существует в локальной области видимости внутри функции test_function
test_function() # без вызова функции test_function Python не видит функцию inner_function
inner_function() # ошибка имени "inner_function" не существует в глобальной области видимости