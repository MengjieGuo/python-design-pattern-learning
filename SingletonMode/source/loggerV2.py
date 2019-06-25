# 版本
# 要求
# 记录信息
# 记录的文件可以在写入信息时指定
# 记录的信息分为若干级别
# 使用类重写函数


class MyLogger(object):
    """
    自定义logger记录器

    Attributes: filename, the name of log file you want to write
    """

    def __init__(self, filename: str):
        """
        初始化一个对象，该对象具有属性：filename
        :param filename:
        """
        self.filename = filename

    def _write_log(self, level, msg):
        """
        Open a file and append level + msg info to it
        :param level:
        :param msg:
        :return:
        """
        with open(self.filename, 'a') as log_f:
            log_f.write('{0} {1}\n'.format(level, msg))

    def critical(self, msg):
        """
        log the critical msg
        :param msg:
        :return:
        """
        self._write_log('CRITICAL', msg)

    def error(self, msg):
        """
        log the error msg
        :param msg:
        :return:
        """
        self._write_log('ERROR', msg)

    def warn(self, msg):
        """
        log the warn msg
        :param msg:
        :return:
        """
        self._write_log('WARN', msg)

    def info(self, msg):
        """
        log the info msg
        :param msg:
        :return:
        """
        self._write_log('INFO', msg)

    def debug(self, msg):
        """
        log the debug msg
        :param msg:
        :return:
        """
        self._write_log('DEBUG', msg)
