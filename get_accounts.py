from context import Instagram  # pylint: disable=no-name-in-module
import json
# If account is public you can query Instagram without auth
instagram = Instagram()

# For getting information about account you don't need to auth:

f = open('accounts.txt', "r")
lines = f.readlines()

print(lines)
output = []
for line in lines:
    print(line)
    account = instagram.get_account(line.replace('\n', ''))

    data = {"id": account.identifier, "username": account.username,
            "follower_count": account.followed_by_count, "full_name": account.full_name}

    print(data)

    output.append(data)
    o = json.dumps(output)


# json.dump(output, 'accounts.json')
try:
    with open('accoutnts.json', 'a') as tf:
        tf.write(o)
except BaseException as e:
    print("Error on_data : %s" % str(e))


# print('Account info:')
#     print('Id', account.identifier)
#     print('Username', account.username)
#     print('Full name', account.full_name)
#     print('Biography', account.biography)
#     print('Profile pic url', account.get_profile_picture_url())
#     print('External Url', account.external_url)
#     print('Number of published posts', account.media_count)
#     print('Number of followers', account.followed_by_count)
#     print('Number of follows', account.follows_count)
#     print('Is private', account.is_private)
#     print('Is verified', account.is_verified)
