#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import logging
import web
import json

import api_handler


reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


API_HANDLER = api_handler.NLPHandler()


class NLPHandlerWrapper:

    def __init__(self):

        self.api_handler = API_HANDLER 
  

    def SetHeader(self):

        web.header('Access-Control-Allow-Origin', '*', unique=True)
        web.header('Access-Control-Allow-Methods', 'POST', unique=True)
        web.header('Access-Control-Allow-Methods', 'GET', unique=True)
        web.header('Access-Control-Max-Age', '1000', unique=True)
        web.header('Content-Type', 'application/json; charset=UTF-8')


    def POST(self):

        return self.GET()


    def GET(self):

        self.SetHeader()

        request = dict(web.input())
        logging.info('req: %s' % json.dumps(request, ensure_ascii=False))

        params = {}
        for k, v in request.iteritems():
            if type(v) == unicode:
                params[k] = v.encode('utf8')
            else:
                params[k] = v

        try:
            text = params.get('text', '')
            result = json.dumps(self.api_handler.get_result(text), ensure_ascii=False)

        except KeyError as e:
            output = '{ "return_code": "01", "error_message": "empty command" }'

        except Exception as e:
            output = '{ "return_code": "01", "error_message": "%s" }' % str(e)

        else:
            output = '{"return_code": "00", "result": %s}' % result

        logging.info('res: %s' % output)

        return output


if __name__ == '__main__':

    urls = (
            '/nlp/get_data', 'NLPHandlerWrapper',
    )
    app = web.application(urls, globals())
    app.run()
