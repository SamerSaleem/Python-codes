#prasing data from yaml file.
import yaml

with open ("yamldata.yml") as data:
    yaml_sample = data.read()
    print(yaml_sample)
yaml_dict = yaml.load(yaml_sample, Loader = yaml.FullLoader)
print (yaml_dict)