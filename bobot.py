"""Bobot
"""
import bottle


@bottle.route('/areyouok')
def areyouok():
    return 'I am ok'


if __name__ == '__main__':
    bottle.run(host='localhost', port=64246)
