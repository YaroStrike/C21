c_name = str(input("Введите название файла .с -> ")+".c")
with open(c_name, 'w') as c:
    c.write("#include <stdio.h>\n")
    c.write("int main()\n")
    c.write("{\n")
add_var_cycle = True
print("\n*Создание входных переменных*")
main_line = int(3)
add_var_cycles = int(0)
strings_declared = int(0)
chars_declared = int(0)
ints_declared = int(0)
floats_declared = int(0)
doubles_declared = int(0)
while add_var_cycle:
    with open(c_name, 'a') as c_add:
        var_type_cycle = True
        while var_type_cycle:
            add_var_type = str(input('Введите тип данных (или "help" для справки) -> '))
            #if add_var_type == "string":
             #   scan_var_type = str("s")
              #  strings_declared += 1
               # var_type_cycle = False
            if add_var_type == "char":
                scan_var_type = str("c")
                chars_declared += 1
                var_type_cycle = False
            elif add_var_type == "int":
                scan_var_type = str("d")
                ints_declared += 1
                var_type_cycle = False
            elif add_var_type == "float":
                scan_var_type = str("f")
                floats_declared += 1
                var_type_cycle = False
            elif add_var_type == "double":
                scan_var_type = str("lf")
                doubles_declared += 1
                var_type_cycle = False
            elif add_var_type == "help":
                print("\nПоддерживаемые типы входных данных:\n")
                print("Текст/символ:")
                print('"string" - искуственный тип на основе char, может содержать 255 символов.')
                print('"char" - символьный тип, может содержать 1 символ.\n')
                print("Числовые:")
                print('"int" - целое число в диапазоне от -2147483648 до 2147483647.')
                print('"float" - дробное число c целой частью как у int и шестью дробными цифрами после "." .')
                print('"double" - дробное число с ещё большей целой частью, содержит до 15 цифр после "." .\n')
                var_type_cycle = True
            else:
                print(f'!!Ошибка "add_var_type": введён неподдерживаемый тип данных - {add_var_type}. ')
                var_type_cycle = True
        c_add.write("    "+add_var_type)
        add_var_quantity = int(input(f"Введите количество переменных {add_var_type} -> "))
        #if add_var_type != "string":
        x = 0
        while x != add_var_quantity:
            x+=1
            c_add.write(" "+add_var_type+str(x))
            if x < add_var_quantity:
                c_add.write(",")
        c_add.write(";\n")
        c_add.write("    "+'scanf("'+"Введите "+str(add_var_quantity)+" значений "+add_var_type+" через пробел: %"+scan_var_type)
        while x > 1:
            x -= 1
            c_add.write(" %"+scan_var_type)
        c_add.write('"')
        while x <= add_var_quantity:
            c_add.write(', &'+add_var_type+str(x))
            x += 1
        c_add.write(");\n")
    with open(c_name, 'r') as c_read:
        lines = [line.strip() for line in c_read.readlines()]
        print(f"Строка для ввода создана:\n")
        print(str(main_line+1)+"|    "+lines[main_line])
        print(str(main_line+2)+"|    "+lines[main_line+1])
    main_line += 1
    add_var_cycles+= 1
    yn_var_add = str(input("\nДобавить ещё переменные другого типа? [Y/N] -> "))
    if yn_var_add.lower() == "y":
        add_var_cycle = True
        main_line+=1
    else:
        add_var_cycle = False
print("\n*Сканирование переменных*")
print("Строки объявления и скана переменных:\n")
main_line = 3
with open(c_name, 'r') as c_read:
    lines = [line.strip() for line in c_read.readlines()]
    while main_line < 3+add_var_cycles:
        print(str(main_line+1)+"|    "+lines[main_line])
        main_line+=1
print(f"\nОбъявлений типа5 string: {strings_declared}")
print(f"Объявлений типа char: {chars_declared}")
print(f"Объявлений типа int: {ints_declared}")
print(f"Объявлений типа float: {floats_declared}")
print(f"Объявлений типа double: {doubles_declared}")
print(f"Циклов объявления выполнено: {add_var_cycles}")