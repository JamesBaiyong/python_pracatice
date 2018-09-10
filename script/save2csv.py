# encoding=utf-8
import os
import csv
import datetime

class Save2CSV(object):

    def save(self, data):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        file_name = './sources/%s/%s_%s.csv' % (data["name"], data["name"], today)
        self.make_dir(data["name"])
        with open(file_name, 'ab+') as f:
            for one_data in data["content"]:
                k_list = []
                v_list = []
                for k, v in one_data.items():
                    k_list.append(k)
                    v_list.append(str(v).replace('\t','').replace('\n','').replace(' ',''))
                self.make_head(file_name, k_list)
                try:
                    output_writer = csv.writer(f)
                    output_writer.writerow(v_list)
                except BaseException:
                    import traceback
                    print(traceback.print_exc())
                print('over')

    def make_dir(self, dir_name):
        if not os.path.exists('./sources/%s' % dir_name):
            os.makedirs('./sources/%s' % dir_name)

    def make_head(self, file_name, k_list):
        if not os.path.getsize(file_name):
            print(u'写入表头')
            with open(file_name, 'ab+') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(k_list)


if __name__ == '__main__':
    worker = Save2CSV()
    worker.save({
        'content': [{'test': 'test string','filter1':'deq'},
                    {'test': 'test string', 'filter1': 'deq'},
                    {'test': 'test string', 'filter1': 'deq'}],
        'name': u'测试一下'})
