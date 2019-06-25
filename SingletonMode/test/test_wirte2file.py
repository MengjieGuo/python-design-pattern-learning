from SingletonMode.source.logger import write2file, debug, info, warn, critical, error


def test_write2file():
    for i in range(0, 10):
        write2file('../log/access.log', 'some msg {0}'.format(i))


def test_debug():
    for i in range(0, 10):
        debug('some msg {0}'.format(i))


def test_info():
    for i in range(0, 10):
        info('some msg {0}'.format(i))


def test_warn():
    for i in range(0, 10):
        warn('some msg {0}'.format(i))


def test_critical():
    for i in range(0, 10):
        critical('some msg {0}'.format(i))


def test_error():
    for i in range(0, 10):
        error('some msg {0}'.format(i))


if __name__ == '__main__':
    test_critical()
    test_error()
    test_warn()
    test_info()
    test_debug()
