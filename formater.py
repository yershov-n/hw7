
def list_rec2html_br(param):
    return '<br/>'.join(str(elem) for elem in param)


def records2dct(records):
    """
    Formats a list of pairs (key, value) into a dict.

    :param records: a list of pairs (key, value)
    :type records: list
    :return: dict
    :rtype: dict
    """
    dct = {}
    for k, v in records:
        dct[k] = v

    return dct
