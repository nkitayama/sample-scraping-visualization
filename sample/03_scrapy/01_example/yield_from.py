def func():
    yield from ["one", "two", "three"]
    print("finish")

if __name__ == '__main__':
    for i, result in enumerate(func()):
        print(f'ループ{i+1}回目')
        print(result)