from cpm.const import ERROR, WARNING, INFO, DEBUG
from cpm import *
import sys

class Logger:

    def error(self, msg):
        if sysconf.get("log-level", WARNING) >= ERROR:
            self.message(ERROR, msg)

    def warning(self, msg):
        if sysconf.get("log-level", WARNING) >= WARNING:
            self.message(WARNING, msg)

    def info(self, msg):
        if sysconf.get("log-level", WARNING) >= INFO:
            self.message(INFO, msg)

    def debug(self, msg):
        if sysconf.get("log-level", WARNING) >= DEBUG:
            self.message(DEBUG, msg)

    def message(self, level, msg):
        prefix = {ERROR: "error", WARNING: "warning",
                  DEBUG: "debug"}.get(level)
        if prefix:
            for line in msg.split("\n"):
                sys.stderr.write("%s: %s\n" % (prefix, line))
        else:
            msg = msg[0].upper()+msg[1:]
            sys.stderr.write("%s\n" % msg)

