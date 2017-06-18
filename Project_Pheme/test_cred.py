import os
import yaml
direct = "/Users/user/"
x_file = open(os.path.join(direct, "cred.yaml"), "r")
print(os.path.join(direct, "cred.yaml"))
docs = yaml.load(x_file)
print(docs.items())
