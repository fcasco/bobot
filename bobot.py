"""Bobot
"""
import os
import random

import bottle


@bottle.route('/areyouok')
def areyouok():
    return 'I am ok'


@bottle.route('/dice')
def talk():
    return str(random.randint(1, 6))


bobot_app = bottle.default_app()


if __name__ == '__main__':
    bottle.run(host='localhost', port=os.environ.get('PORT', 64246))
