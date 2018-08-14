# encoding=utf-8
import os
import logging.config


class SetLog(object):
    def create_logger(self):
        self._work_path = os.getcwd()
        self._data_path = '%s/data' % self._work_path
        self._log_path = '%s/log' % self._data_path
        self._logger_name = 'log_note'
        logger = logging.getLogger(self._logger_name)
        self.logfile = self.load_file(
            self._work_path + '/config/logging.conf')
        if not os.path.isdir(self._data_path):
            self.make_data_dir()
        logging.config.dictConfig(eval(self.logfile))

        return logger

    def make_data_dir(self):
        os.makedirs(self._data_path)

    @staticmethod
    def load_file(filename):
        with open(filename, 'r') as f:
            return f.read()
