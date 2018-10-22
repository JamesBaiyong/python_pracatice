# encoding=utf-8
import os
import csv
import fcntl
import codecs
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Save2OutputObj(object):
    def __init__(self, cfg):
        try:
            self.split = cfg['split']
            self.encoding = cfg['encoding']
        except KeyError:
            raise KeyError('Missing parameters')

    def save(self, data):
        if len(self.split) == 1:
            split = self.split
            self.save_2_csv(data, split)
        else:
            split = self.split
            self.save_2_obj(data, split)

    def save_2_csv(self, data, split):
        # 分割符为单字符时,存为csv
        today = datetime.datetime.now().strftime("%Y%m%d")
        file_name = './sources/%s/%s_%s.csv' % (
            data["name"], data["name"], today)
        self.make_dir(data["name"])
        with codecs.open(file_name, 'ab+', encoding=self.encoding) as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            each_data = self.traver_data(data)
            for one_data in each_data:
                k_list = []
                v_list = []
                for k, v in one_data.items():
                    k_list.append(k)
                    v_list.append(
                        str(v).replace('\t', '').replace('\r', '').replace(',','，')
                        .replace('\n', '').replace(' ', '').replace('\r\n', '')
                        .replace('　', '') # 中文空格
                        .replace(';', '；').replace('None', ''))
                self.make_csv_head(file_name, k_list, split)
                try:
                    output_writer = csv.writer(f, delimiter=split)
                    output_writer.writerow(v_list)
                except IOError:
                    raise IOError


    def save_2_obj(self, data, split):
        # 分割符不为单字符时,存为txt
        today = datetime.datetime.now().strftime("%Y%m%d")
        file_name = './sources/%s/%s_%s.txt' % (
            data["name"], data["name"], today)
        self.make_dir(data["name"])
        with codecs.open(file_name, 'ab+', encoding=self.encoding) as f:
            each_data = self.traver_data(data)
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            for one_data in each_data:
                k_str = ''
                v_str = ''
                for k, v in one_data.items():
                    k_str += k + split
                    v_str += (str(v)
                              .replace('\t', '').replace(split, '')
                              .replace('\n', '').replace(' ', '').replace('\r', '')
                              .replace('\r\n', '')
                              .replace('　', '')  # 中文空格
                              .replace(';', '；').replace('None', '')
                              + split)
                self.make_obj_head(file_name, k_str[:-len(split)])
                try:
                    f.write(v_str[:-len(split)])
                    f.write('\n')
                except IOError:
                    raise IOError

    @staticmethod
    def make_dir(dir_name):
        if not os.path.exists('./sources/%s' % dir_name):
            os.makedirs('./sources/%s' % dir_name)

    @staticmethod
    def make_csv_head(file_name, k_list, split):
        if not os.path.getsize(file_name):
            with open(file_name, 'ab+') as f:
                csv_writer = csv.writer(f, delimiter=split)
                csv_writer.writerow(k_list)

    @staticmethod
    def make_obj_head(file_name, k_str):
        if not os.path.getsize(file_name):
            with open(file_name, 'ab+') as f:
                f.write(k_str)
                f.write('\n')

    @staticmethod
    def traver_data(data):
        for one_data in data["content"]:
            yield one_data


if __name__ == '__main__':
    worker = Save2OutputObj(',')
    worker.save({
        'content': [{'test': 'test string', 'test1': 'te,s\tt', 'test3': 'test333'},
                    {'test': 'test string', 'test1': 'test \n', 'test3': 'test333'},
                    {'test': 'test string', 'test1': 'test', 'test3': 'test333'}],
        'name': u'测试一下'})
