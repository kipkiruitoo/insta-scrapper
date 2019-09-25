from context import Instagram  # pylint: disable=no-name-in-module
import json
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

    data = {"id": account.identifier, "username": account.username,
            "follower_count": account.followed_by_count, "full_name": account.full_name}

    print(data)

    # location = instagram.get_location_by_id(account.identifier)
    # print(location)

    output.append(data)
    o = json.dumps(output)


try:
    with open('accoutnts.json', 'a') as tf:
        tf.write(o)
except BaseException as e:
    print("Error on_data : %s" % str(e))
