#!/usr/bin/env python
# -*- coding: utf8 -*-


import os
import sys
import logging
import json

import search_tokenizer


TOKEN_CONFIG_NM = '11st.index.hdfs'
SIMBOOST_CONFIG_NM = '11st.nterm.hdfs'
SINGLE_SYNONYM_FILE = '/app/memex/fcmp/synonym/synonym.index.dic'
DUPLEX_SYNONYM_FILE = '/app/memex/fcmp/synonym/keyword.normal.equal.dic'


reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


class NLPHandler():
   

    def __init__(self):

        self.tokenizer = search_tokenizer.SearchTokenizer(
                TOKEN_CONFIG_NM, SIMBOOST_CONFIG_NM,
                SINGLE_SYNONYM_FILE, DUPLEX_SYNONYM_FILE)


    def get_result(self, text):

        text = text.replace('\t', ' ')
        token_results, simboost_results = self.tokenizer.get_tokens(text)
        ver = self.tokenizer.token_tokenizer.get_version()
       
        return {
                'text': text,
                'tokens': token_results,
                'simboosts': simboost_results, 
                'version': ver,
        }


    def __del__(self):

        pass


