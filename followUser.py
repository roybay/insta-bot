from instapy import InstaPy


def follow_user(insta_username, insta_password, follow_insta_user):
    # if you want to run this script on a server,
	# simply add nogui=True to the InstaPy() constructor
	session = InstaPy(username=insta_username, password=insta_password)
	session.login()

	# Fallowing by a List.
	session.set_do_follow(enabled=True, percentage=10, times=2)
	session.set_skip_users(skip_private=False,
	                       private_percentage=100)
	session.follow_by_list(followlist=[follow_insta_user], times=1, sleep_delay=600, interact=False)

	# end the bot session
	session.end()

# follow_user('username', 'password', 'follow_insta_user')