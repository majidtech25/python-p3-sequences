# fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# # An immutable, ordered sequence of months
month_tuple = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
    
)
month_list = ['January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']
print(month_tuple[2:5:2])
print(len(month_tuple))
print('March' in month_tuple)
print(month_tuple + month_tuple)
print(month_tuple * 2)
print(min(month_tuple))
print(max(month_tuple))
print(month_tuple.index('May'))
print(month_tuple.count('May'))
print(len(month_tuple))
print(month_tuple[-1], month_tuple[-2])
print(month_tuple[-2:])
print(month_tuple[-1:-3:-1])
# month_list.sort()
# print(month_list)
sorted_list = sorted(month_list, key=len,reverse=True)
print(month_list)
print(sorted_list)
month_list[0] = None
month_list.append('Another_month')
month_list.insert(6, 'Almost_birtmonth')
print(month_list)
my_range = range(2, 10, 2)
for numbers in my_range:
  print(numbers)
# # A simple pattern of numbers
# even_numbers_up_to_100 = range(0, 101, 2)
# # A grammatical sentence
# sentence_string = "Strings are immutable sequences of Unicode code points."

# lists = [[]] * 3
# print(lists)

# lists[0].append(3)
# lists[1].append(5)
# lists[2].append(7)
# print(lists)
# lists = [[] for i in range(3)]
# lists[0].append(3)
# lists[1].append(5)
# lists[2].append(7)
# print(lists)