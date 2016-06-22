"""Bobot
"""
import os
import random

import bottle


@bottle.route('/')
def index():
    return 'Bobot'


@bottle.route('/areyouok')
def areyouok():
    return 'I am ok'


@bottle.route('/dice')
def dice():
    return str(random.randint(1, 6))


@bottle.route('/fb/webhook')
def fb_webhook():
    verify_token = bottle.request.query.get('hub.verify_token', None)
    my_token = os.environ.get('BOBOT_TOKEN', random.random())
    if verify_token == my_token:
        response = bottle.request.query.get('hub.challenge')
    else:
        response = 'That\'s not my token!'

    return response


@bottle.post('/fb/webhook')
def fb_webhook_post():
    print(bottle.request.json)
    return '(0.o)'


bobot_app = bottle.default_app()


if __name__ == '__main__':
    bottle.run(host='localhost', port=os.environ.get('PORT', 64246))
