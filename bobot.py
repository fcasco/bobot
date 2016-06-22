"""Bobot
"""
import os

import bottle


@bottle.route('/areyouok')
def areyouok():
    return 'I am ok'


bobot_app = bottle.default_app()


if __name__ == '__main__':
    bottle.run(host='localhost', port=os.environ.get('PORT', 64246))
