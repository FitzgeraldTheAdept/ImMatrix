from ComplexNum import ComplexNum
from ComplexCalculator import ComplexCalculator
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.

arr = list((ComplexNum(10, 5), ComplexNum(5, -10)))
# Press the green button in the gutter to run the script.
# for name in arr:
#    print(f'{name}', end='  ')

calc = ComplexCalculator()

# result = calc.add(arr[0], arr[1]).tostring
# result = '%f + i%f' % (10, 12)
# buf = calc.add(arr[0], arr[1]).tostring()
# result = type(buf)
result = calc.add(arr[0], arr[1]).torect()
print(f'Rectangular result is {result}', end='\n')
print(f'Polar result is {calc.add(arr[0], arr[1]).topolardeg()}', end='\n')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
