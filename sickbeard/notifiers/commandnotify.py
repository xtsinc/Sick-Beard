import string
import sickbeard
import os

from sickbeard import logger

class CommandNotifier:
    
    def test_notify(self, command):
        return self._executeCommand(command)

    def _executeCommand(self, command):
        if not command:
            command = sickbeard.NOTIFY_COMMAND
        logger.log("Executing command notification: " + command, logger.DEBUG)
        os.system(command)
        return True
    def notify_snatch(self, ep_name, command):
        self._executeCommand(command)
    def notify_download(self, ep_name, command):
        
        
notifier = CommandNotifier