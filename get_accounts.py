from context import Instagram  # pylint: disable=no-name-in-module
import json
import re
# If account is public you can query Instagram without auth
instagram = Instagram()

# For getting information about account you don't need to auth:

f = open('c.txt', "r")
lines = f.readlines()

print(lines)
output = []
for line in lines:
    print(line)
    account = instagram.get_account(line.replace('\n', ''))
    reg = re.compile("(\d{2}\d{5}\d{4})")

    data = {"id": account.identifier, "username": account.username,
            "follower_count": account.followed_by_count, "biography":account.biography , "full_name":  account.full_name}

    # print(data)

    # location = instagram.get_location_by_id(account.identifier)
    # print(location)

    output.append(data)
    o = json.dumps(output)


try:
    with open('accoutnts.json', 'a') as tf:
        tf.write(o)
except BaseException as e:
    print("Error on_data : %s" % str(e))
