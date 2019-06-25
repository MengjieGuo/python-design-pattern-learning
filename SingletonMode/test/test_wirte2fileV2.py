from SingletonMode.source.loggerV2 import MyLogger


def test_MyLogger():
    """
    对日志记录器进行测试
    :return:
    """

    file_name = '../log/accessV2.log'
    log_obj = MyLogger(file_name)
    for i in range(0, 10):
        log_obj.critical(i)
        log_obj.error(i)
        log_obj.warn(i)
        log_obj.info(i)
        log_obj.debug(i)


if __name__ == '__main__':
    test_MyLogger()