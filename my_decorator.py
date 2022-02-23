from datetime import datetime
import os


def loger_decor(file_name, path_to_file=None):
    if path_to_file is None:
        file_path = os.path.join(os.getcwd())
    else:
        file_path = os.path.join(os.path.abspath(path_to_file))

    full_file_path = os.path.join(file_path, file_name)

    def log_dec(old_function):
        def new_def(*args, **kwargs):
            log_date = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
            func_name = old_function.__name__
            input_data = f'аргументы:{args} и {kwargs}'
            output_data = old_function(*args, **kwargs)
            result_line = f'вызвана функция {func_name} \n' \
                          f'дата и время вызова : {log_date} \n' \
                          f'{input_data} \n' \
                          f'возвращаемое значение {func_name}: {output_data}\n' \
                          f'-----------------------------------\n'
            with open(full_file_path, 'a', encoding='utf-8') as f:
                f.write(result_line)
            return output_data

        return new_def

    return log_dec
