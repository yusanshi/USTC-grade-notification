from config import PERIOD, MAX_TIME
from time import sleep
from get_grade import get_grade
from send_mail import send_mail

import logging


def main():
    LOG_FORMAT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    fp = logging.FileHandler('log.txt', encoding='utf-8')
    fs = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT,
                        datefmt=DATE_FORMAT, handlers=[fp, fs])

    current_grade = get_grade()
    logging.info("Initial number: %d" % len(current_grade))
    logging.info("Initial grades: %s" % current_grade)

    for i in range(MAX_TIME):
        try:
            while True:
                sleep(PERIOD * 60)
                new_grade = get_grade()
                logging.info("Current number: %d" % len(new_grade))
                increased = new_grade.keys() - current_grade.keys()
                logging.info("Increased: %s" % increased)
                if len(increased) > 0:
                    current_grade = new_grade

                    text = "出分啦！"
                    for key in increased:
                        text += " %s: %s " % (key, new_grade[key])

                    logging.info("To send: " + text)
                    send_mail(text)
        except Exception as e:
            text = "第 %d 次出现异常！ %s" % (i + 1, str(e))
            logging.error(text)
            send_mail(text)
            sleep(30)


if __name__ == "__main__":
    main()
