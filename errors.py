def fcn():
    x = {'hello': 'hi'}
    try:
        result = x['hi']
    except KeyError:
        print('Key "hi" not in dictionary. Using key "hello" instead.')
        result = x['hello']

    return result


def main():
    print(fcn())


if __name__ == "__main__":
    main()
