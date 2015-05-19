#!/usr/bin/env python

import web
import os.path
import pickle

urls = (
    '/stats', 'stats',
    '/notify/(.*)', 'notify'
)

app = web.application(urls, globals())

class stats:
    def GET(self):
        counter=load_obj('counter')
        output = 'total number of uses:'
        for k in counter:
            output += "\n"
            output += str(k)
            output += '      '
            output += str(counter[k])
        return output

class notify:
    def GET(self, container):
        counter=load_obj('counter')
        output = container
        if container in counter:
            counter[container]+=1
        else:
            counter[container]=1
        save_obj(counter, 'counter')
        return output

def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    if os.path.isfile('obj/' + name + '.pkl'):
        with open('obj/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        return dict()

if __name__ == "__main__":
    app.run()
