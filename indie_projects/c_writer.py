c_name = str(input("Введите название файла .с -> ")+".c")
with open(c_name, 'w') as c:
    c.write("#include <stdio.h>\n")
    c.write("int main()\n")
    c.write("{\n")
add_var_cycle = True
main_line = int(3)
print("\n*Создание входных переменных*")
main_line = int(3)
add_var_cycles = int(0)
ints_declared = int(0)
floats_declared = int(0)
while add_var_cycle:
    add_var_cycles+=1
    with open(c_name, 'a') as c_add:
        add_var_type = str(input("Введите тип данных -> "))
        if add_var_type == "int":
            scan_var_type = str("d")
            ints_declared += 1
        elif add_var_type == "float":
            scan_var_type = str("f")
            floats_declared += 1
        else:
            print(f"!!Ошибка var_type-1: введён неподдерживаемый тип данных - {add_var_type}. Exit(0)")
            exit(0)
        c_add.write("    "+add_var_type)
        add_var_quantity = int(input(f"Введите количество переменных {add_var_type} -> "))
        x = 0
        while x != add_var_quantity:
            x+=1
            c_add.write(" "+add_var_type+str(x))
            if x < add_var_quantity:
                c_add.write(",")
        c_add.write(";\n")
    with open(c_name, 'r') as c_read:
        lines = [line.strip() for line in c_read.readlines()]
        print(f"Строка создания переменных:\n")
        print(str(main_line+1)+"|    "+lines[main_line])
    yn_var_add = str(input("\nДобавить ещё тип с переменными? [Y/N] -> "))
    if yn_var_add.lower() == "y":
        add_var_cycle = True
        main_line+=1
    else:
        add_var_cycle = False
print("\n*Сканирование переменных*")
print("Строки объявления переменных:\n")
main_line = 3
with open(c_name, 'r') as c_read:
    lines = [line.strip() for line in c_read.readlines()]
    while main_line < 3+add_var_cycles:
        print(str(main_line+1)+"|    "+lines[main_line])
        main_line+=1
print(f"\nОбъявлений типа int: {ints_declared}")
print(f"Объявлений типа float: {floats_declared}")
print(f"Циклов объявления выполнено: {add_var_cycles}")
with open (c_name, 'a') as c_add:
    add_scan_cycles = 0
    while add_scan_cycles < add_var_cycles:
        c_add.write("    "+'scanf("'+"Введите "+str(add_var_quantity)+" значений "+add_var_type+": %"+scan_var_type)
        while x > 1:
            x -= 1
            c_add.write(" %"+scan_var_type)
        c_add.write('"')
        while x <= add_var_quantity:
            c_add.write(', &'+add_var_type+str(x))
            x += 1
        c_add.write(");\n")
        add_scan_cycles += 1
with open (c_name, 'r') as c_read:
    lines = [line.strip() for line in c_read.readlines()]
    print("\nСтроки для ввода значений:\n")
    print(str(main_line+1)+"|    "+lines[main_line])