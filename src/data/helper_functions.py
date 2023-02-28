import os

def get_env_var(var):
    try:
        return os.environ.get(var)
    except ValueError:
        raise Exception(f'environment variable {var} isn\'t set properly')
        
