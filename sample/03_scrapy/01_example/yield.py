def func(number):
    for i in range(number):
        yield {
            "hoge": i,
            "fuga": i,
        }

    if True is not None:
        yield f'number = {number}'

if __name__ == '__main__':
    for i, result in enumerate(func(3)):
        print(f'ループ{i+1}回目')
        print(result)