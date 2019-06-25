def write2file(msg, file='../log/access.log'):
    """

    将print信息写入文件

    :param file:
    :param msg:
    :return:
    """
    with open(file, 'a') as log_f:
        log_f.write('{0}\n'.format(msg))


def error(msg):
    """
    记录Error级别的信息
    :param msg:
    :return:
    """
    write2file('[ERROR  ] {0}'.format(msg))


def critical(msg):
    """
    记录严重级别的信息
    :param msg:
    :return:
    """
    write2file('[CRITICAL   ] {0}'.format(msg))


def debug(msg):
    """
    记录Debug级别的信息
    :param msg:
    :return:
    """
    write2file('[DEBUG  ] {0}'.format(msg))


def info(msg):
    """
    记录info级别的信息
    :param msg:
    :return:
    """
    write2file('[INFO   ] {0}'.format(msg))


def warn(msg):
    """
    记录warn级别的信息
    :param msg:
    :return:
    """
    write2file('[WARN   ] {0}'.format(msg))
