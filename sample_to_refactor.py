# File contoh yang perlu di-refactor
def calculate(a, b, c):
    x = a + b
    y = x * c
    return y

def process_data(data_list):
    new_list = []
    for i in data_list:
        if i > 10:
            new_list.append(i * 2)
    return new_list
