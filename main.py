from instagrapi import Client
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def insta_auth():
    USERNAME = getenv('LOGIN')
    PASSWORD = getenv('PASSWORD')

    try:
        cl = Client()
        cl.login(USERNAME, PASSWORD)

        return cl
    except Exception as ex:
        print(ex)
        print('Sorry, something went wrong :(')


def get_user_medias(cl, username='lilireinhart'):
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id, 7)

    # for item in medias:
    #     print(item, '\n')
    #     print(item.pk)
    #
    #     cl.video_download(media_pk=item.pk, folder='path_to_media_folder')

    cl.album_download(media_pk='2915703388603986272', folder='C:\\pythonProject\\instagram-bot\\media')


def media_like(cl, username='lilireinhart'):
    user_id = cl.user_id_from_username(username)
    cl.media_like(media_id=f'2915703388603986272_{user_id}')
    # cl.media_unlike(media_id=f'media_id_{user_id}')


def main():
    cl = insta_auth()
    get_user_medias(cl)
    # media_like(cl)


if __name__ == '__main__':
    main()
