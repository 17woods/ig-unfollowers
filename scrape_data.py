from time import time
import instaloader


def rntm(start_time):
    return f'[RUNTIME {round(time() - start_time, 1)}s]'


def get_lists(usr, pw, usr_wanted=''):
    s_t = time()

    ig = instaloader.Instaloader()

    USERNAME = usr
    PASSWORD = pw

    WANT = usr_wanted if usr_wanted else usr

    print(f'{rntm(s_t)} [Info] - Logging In @{usr}...')

    try:
        ig.login(USERNAME, PASSWORD)
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        code_2fa = input("Enter 2FA Code: ")
        ig.two_factor_login(code_2fa)
    except:
        print("Unknown error occured, please check your USERNAME and PASSWORD")

    want_profile = instaloader.Profile.from_username(ig.context, WANT)

    print(f'{rntm(s_t)} [Info] - Getting Following...')
    followees = want_profile.get_followees()
    followees_list = [profile.username for profile in followees]

    print(f'{rntm(s_t)} [Info] - Getting Followers...')
    followers = want_profile.get_followers()
    followers_list = [profile.username for profile in followers]

    print(f'{rntm(s_t)} [Info] Followers: {len(followers_list)}')
    print(f'{rntm(s_t)} [Info] Following: {len(followees_list)}')

    print("--- %s seconds ---" % (time() - s_t))

    return followers_list, followees_list
