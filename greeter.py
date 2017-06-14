#!/usr/bin/python

from errbot import BotPlugin
from errbot import botcmd
import logging


class Greeter(BotPlugin):
    """
    Very simple Greeter plugin
    """

    def callback_message(self, message):
        channel = "%s" % message.frm
        is_new_user = False
        logging.info("Checking if user is new... (joined #general channel)")
        if channel.split("/")[0]== "#general" and message.body.find('joined'):
            is_new_user = True
        if is_new_user:
            self.send(
                self.build_identifier('#general'),
                """@%s, bem vindo ao Slack da FL! Algumas dicas para você:\n 
1. Sempre que tiver dúvidas sobre processos, acesse a pagina de padroes e manuais no Confluence (https://fundacaolemann.atlassian.net/wiki/index.action)  \n
2. Se quiser um jeito fácil de ficar online, não deixe de experimentar o aplicativo http://meetfranz.com""" % message.frm.nick,
            )

