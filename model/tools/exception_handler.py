from model.tools.logging import Logger


def exception_handler(function):
    def inner(*args, **kwargs):
        try:
            output = function(*args, **kwargs)
            if not "find" in function.__name__ :
                Logger.info(f"{function.__qualname__}{args[1:]} [RETURNED] : {output}")
            else:
                Logger.info(f"{function.__qualname__}{args[1:]}")
            return True, output
        except Exception as e:
            Logger.error(f"{function.__qualname__}{args[1:]} [RAISED EXCEPTION] : {e}")
            return False, str(e)

    return inner