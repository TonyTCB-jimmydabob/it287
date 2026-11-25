import logging
import traceback

logging.basicConfig(
    filename='game.log',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def e(message):
    logging.error(message)

def p(message):
    logging.info(message)