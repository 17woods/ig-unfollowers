import scrape_data


def get_unfollowers(followers, following):
    unfollowers = []

    for user in following:
        if user not in followers:
            unfollowers.append(user)

    print('Unfollowers:')
    print('\n'.join(unfollowers) + '\n')


if __name__ == '__main__':
    # Enter valid IG login info below
    # Account w/o 2fa recommended, haven't gotten 2fa to work yet
    USERNAME = ''
    PASSWORD = ''

    # Will find for USERNAME if left empty
    WANTED_USER = ''

    list_ers, list_ing = scrape_data.get_lists(USERNAME, PASSWORD, WANTED_USER)

    get_unfollowers(list_ers, list_ing)
