from controller import Controller
from utils.constants import POSITIVE_ANSWERS
from utils.prints import print_goodbye_msg, MSG_PLAY_NEW_GAME


def main():
    controller = Controller()
    controller.setup()

    while True:
        controller.play()
        controller.show_results()
        new_game_prompt = input(MSG_PLAY_NEW_GAME).lower()
        if new_game_prompt not in POSITIVE_ANSWERS:
            print_goodbye_msg()
            break
        controller.switch_symbols()


if __name__ == '__main__':
    main()
