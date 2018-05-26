from django.shortcuts import render

import sys
import os
from imaplib import IMAP4_SSL
import email
import json
from datetime import datetime

JSON_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'json_files')


class MailReader:
    def __init__(self, dict_mail):
        self._host = dict_mail.get('host', 'no')
        self._port = dict_mail.get('port', 'no')
        self._user = dict_mail.get('user', 'no')
        self._psw = dict_mail.get('psw', 'no')
        self._sender = dict_mail.get('sender', 'no')

    def check_jsonfiles_dir(self):
        if not os.path.exists(JSON_FILES_DIR):
            os.mkdir(JSON_FILES_DIR)

    def read_and_save_json(self):
        self.check_jsonfiles_dir()

        mail_server = IMAP4_SSL(host=self._host, port=self._port)
        mail_server.login(user=self._user, password=self._psw)

        status, msgs = mail_server.select('INBOX')
        answer_code, msgs_tuples = mail_server.search(None, 'FROM', f'"{self._sender}"')

        for num in msgs_tuples[0].split():
            code, msg = mail_server.fetch(num, '(RFC822)')
            email_message = email.message_from_bytes(msg[0][1])

            if email_message.is_multipart():
                for part in email_message.walk():
                    filename = part.get_filename()

                    if filename and filename.split('.')[-1] == 'json':
                        with open(os.path.join(JSON_FILES_DIR, filename), 'wb') as file_json:
                            file_json.write(part.get_payload(decode=True))

        mail_server.close()
        mail_server.logout()


class JsonFilesReader:
    def __init__(self):
        self.check_jsonfiles_dir()

    def check_jsonfiles_dir(self):
        if not os.path.exists(JSON_FILES_DIR):
            print(f'my_error - No directory for json_files: {JSON_FILES_DIR}')
            sys.exit(1)

    def json_file_read(self):
        pass

    def get_last_json_file(self):
        global last_time, last_file
        last_time = datetime(2000, 1, 1)
        last_file = ''

        for json_file_name in os.listdir(JSON_FILES_DIR):
            if json_file_name.split('.')[-1] == 'json':
                with open(os.path.join(JSON_FILES_DIR, json_file_name), encoding='utf-8') as file_json:
                    json_data = list(reversed(json.loads(file_json.read())))
                    time_str = json_data[0]['document']['receipt'].get('dateTime', '0')

                    t_year = int(time_str[0:4])
                    t_month = int(time_str[5:7])
                    t_day = int(time_str[8:10])
                    t_hour = int(time_str[11:13])
                    t_minute = int(time_str[14:16])
                    t_second = int(time_str[17:19])
                    temp_time = datetime(t_year, t_month, t_day, t_hour, t_minute, t_second)

                    if temp_time > last_time:
                        last_time = temp_time
                        last_file = json_file_name

        return last_file


    def vipiska_json_parser(self, json_file_name):
        # amount_documents = len(json_data)
        # amount_items = len(json_data[7]['document']['receipt']['items'])
        # amount_data = len(json_data)
        # print(amount_documents, amount_items)

        with open(os.path.join(JSON_FILES_DIR, json_file_name), encoding='utf-8') as file_json:
            # data = json.loads(file_json.read().replace('\n', '').replace('\t', ''))
            json_data = json.loads(file_json.read())

        for num_record, record in enumerate(json_data):
            current_record = record['document']['receipt']

            cashTotalSum = current_record.get('cashTotalSum', '-')
            dateTime = current_record.get('dateTime', '-')
            ecashTotalSum = current_record.get('ecashTotalSum', '-')
            fiscalDocumentNumber = current_record.get('fiscalDocumentNumber', '-')
            fiscalDriveNumber = current_record.get('fiscalDriveNumber', '-')
            fiscalSign = current_record.get('fiscalSign', '-')
            kktRegId = current_record.get('kktRegId', '-')
            message = current_record.get('message', '-')
            modifiers = current_record.get('modifiers', '-')
            nds10 = current_record.get('nds10', '-')
            nds18 = current_record.get('nds18', '-')
            operationType = current_record.get('operationType', '-')
            operator = current_record.get('operator', '-')
            properties = current_record.get('properties', '-')
            rawData = current_record.get('rawData', '-')
            receiptCode = current_record.get('receiptCode', '-')
            requestNumber = current_record.get('requestNumber', '-')
            retailPlaceAddress = current_record.get('retailPlaceAddress', '-')
            senderAddress = current_record.get('senderAddress', '-')
            shiftNumber = current_record.get('shiftNumber', '-')
            stornoItems = current_record.get('stornoItems', '-')
            taxationType = current_record.get('taxationType', '-')
            totalSum = current_record.get('totalSum', '-')
            user = current_record.get('user', '-')
            userInn = current_record.get('userInn', '-')

            print(f'{num_record+1} {dateTime} sum = {cashTotalSum}/{ecashTotalSum}  {fiscalDocumentNumber} {fiscalDriveNumber} {message}')

            # amount_items = len(current_record.get('items', 0))
            items = current_record.get('items', 0)

            for num_item, item in enumerate(items):
                modifiers = item.get('modifiers', '-')
                name = item.get('name', '-')
                nds18 = item.get('nds18', '-')
                price = item.get('price', '-')
                properties = item.get('properties', '-')
                quantity = item.get('quantity', '-')
                sum = item.get('sum', '-')

                print('\t', num_item+1, name, price, quantity, sum)





# Create your views here.
def fni(request):
    return render(request, 'app_fni/fni.html', {})


def check_mail(request):
    di_gmail = {'host': 'imap.gmail.com', 'port': '993', 'user': 'falkov.mobile@gmail.com', 'psw': 'gamergamer', 'sender': 'sfalkov@icloud.com'}

    mail_reader = MailReader(di_gmail)
    mail_reader.read_and_save_json()

    json_files_reader = JsonFilesReader()
    last_json_file_name = json_files_reader.get_last_json_file()
    json_files_reader.vipiska_json_parser(last_json_file_name)

    return render(request, 'app_fni/check_mail.html', {})


