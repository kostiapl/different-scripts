import random
import os


# a simple script to simulate maximum possible headers size for jwt token without taking into account additional payloads (header, another claims, sign)
# see # https://stackoverflow.com/questions/686217/maximum-on-http-header-values for more details

# 4 random groups with about 10 characters in length each
possible_groups_names= ['group_name1', 'group_name2','role_name1', 'role_name2']


file_name = 'jwt_token.test'


if os.path.isfile(file_name):
    os.remove(file_name)



with open(file_name, 'w') as f:
    # about 600 entities (roles, groups,..) are possible  in 7.4 kb size
    for x in range(1,600,1):
        f.write (possible_groups_names[random.randint(0,3)] + '\n')
        #f.write("\n")







