# Техническое задание проекта Black Pirate

Структура проекта

```python
desktop_useragents = []

REFLINK = 'реферальная ссылка'

def get_proxy():
    """
    Данный метод читает текстовый фаил, извлекает из него proxy так же удаляя его. Затем встряхивает удааляя поле с     пустым значением, и перезаписывает список в тот же файл. Возвращает proxy
    """
    return proxy

def get_mail():
    """
    Данный метод читает текстовый фаил, извлекает из него email так же удаляя его. Затем встряхивает удааляя поле с     пустым значением, и перезаписывает в тот же файл. Возвращает email 
    """
    return email

def get_password():
    """
    Данный метод читает текстовый фаил, извлекает из него пароль методом choise. Затем встряхивает удааляя поле 
    с пустым значением, и перезаписывает в тот же файл. Возвращает password 
    """
    return password

def write_err():  # тут в качестве параметров будет предаваться данные при которых произошла ошибка.
    pass

def main():
    try:
        # тут выполняются все действия со страницей по регистрации
        pass
    except Exception as ex:
        # тут вызывается метод который записывает информацию об ошибке в файл
        pass
    finally:
        # тут указывается код который будет выполняться в случае неуспешного выполнения блока try 
        pass
```

![image-20211107163713526](C:\Users\mugen\AppData\Roaming\Typora\typora-user-images\image-20211107163713526.png)

email input == find by id == emailCreateAccount
nickname input == find by id == usernameCreateAccount
password input == find by id == passwordCreateAccount
confirm password input == find by id == confirmPasswordCreateAccount
phone number input == find by id == mobileSetupAccount
press button to continue == find by id == submitButtonCreateAccount



![image-20211107164448628](C:\Users\mugen\AppData\Roaming\Typora\typora-user-images\image-20211107164448628.png)

first name input == find by id == 'firstNameSetupPersonalDetails'
last name input == find by id == 'lastNameSetupPersonalDetails'
gender choose box == find by id == male = 'male_GenderSetupAccount' == female = 'female_GenderSetupAccount' 

date of birth 
month == find by id == birthdayDropdownSetupAccount_Month
select month == find by xpath == "//*[@id="birthdayDropdownSetupAccount_Month"]/option[{range(2, 13)}]"

day == find by id == birthdayDropdownSetupAccount_Day
select month == find by xpath == "//*[@id="birthdayDropdownSetupAccount_Day"]/option[{range(2, 30)}]"

year == find by id == birthdayDropdownSetupAccount_Year
select year == find by xpath == //*[@id="birthdayDropdownSetupAccount_Year"]/option[{range(4, 15)}]

press button to continue == find by id == almostDone



![image-20211108001122627](C:\Users\mugen\AppData\Roaming\Typora\typora-user-images\image-20211108001122627.png)

country input == find by id == countrySetupAccount
choose country == find by xpath == "//*[@id="register-form"]/div/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div[2]/div/select/option[190]"

postal code == find by id == postcode-field

address == find by id == address-field

locate == find by id == city-fiield

i accept to rules (check box)== find by xpath == "//*[@id="register-form"]/div/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div/div[1]/div/label/input"

press button to registrate == find by id == submitCreateAccount 
