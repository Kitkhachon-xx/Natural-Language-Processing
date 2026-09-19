import yaml

def load_config(config_path):
    with open(config_path,encoding= 'utf-8-sig',mode='r') as f:
        config = yaml.safe_load(f)
    return config