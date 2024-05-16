import uuid

headers = {
    "Content-Type": "application/json",
    'Authorization': 'Basic ZGJvOnBhc3MxMjM='
}

headers_cardPayment = {
    "Content-Type": "application/json",
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiIzZjFhMTdhNC1hZjU2LTQzYzMtOTYxNy1mNzY2MmYxZGVhOGMiLCJ1bmlxdWVfbmFtZSI6ImRibyIsIm5iZiI6MTY5ODM3ODY0OCwiZXhwIjoxNjk4Mzc4NzA4LCJpYXQiOjE2OTgzNzg2NDgsImlzcyI6Imlzc3VlciIsImF1ZCI6ImF1ZGllbmNlIn0.LjVK4FowqkyGD6B-y9K5NVHhbhSg5RTICVabWVAI1JQ'
}

cardPayment_body = {
    "accNumber": "1250820006886382",
    "processing": "OW4",
    "amount": 1,
    "purposeCode": "51B",
    "purposeDescription": "тест 1",
    "currency": "KGS",
    "transactionPart": "c",
    "type": "auth"
}

service_100_body = {
    "version": "1.0",
    "type": "100",
    "id": "2208A15C-CF68-4948-8E0C-94BD82CDD0F8",
    "dateTime": "05.10.2023 11:25:52.770434 +06:00",
    "source": "Creatio",
    "body": [
        {
            "clientCode": "008.119115"
        }
    ]
}

service_101_body = {
    "version": "1.0",
    "type": "101",
    "id": "2208A15C-CF68-4948-8E0C-94BD82CDD0F8",
    "dateTime": "05.10.2023 11:25:52.770434 +06:00",
    "source": "Creatio",
    "body": [
        {
            "customerId": "008.119115"
        }
    ]
}

service_102_body = {
    "version": "1.0",
    "type": "102",
    "id": "F2B065C5-2605-4758-A148-34766EF992D9",
    "dateTime": "30.11.2020 16:25:44.995000 +06:00",
    "source": "DBO",
    "body": [
        {
            "identifier": "1250820004775119",
            "readFlags": {
                "balance": 1,
                "cards": 1
            }
        }
    ]
}

service_205_body = {
    "version": "1.0",
    "type": "205",
    "id": "2208A15C-CF68-4948-8E0C-94BD82CDD0F8",
    "dateTime": "05.10.2023 11:25:52.770434 +06:00",
    "source": "Creatio",
    "body": [
        {
          "customerId": "008.128090"
        }
    ]
}

service_207_inn_body ={
    "version": "2.0",
    "type": "207",
    "id": "{{$guid}}",
    "dateTime": "05.10.2023 11:25:52.770434 +06:00",
    "source": "Creatio",
    "body": [
        {
            "inn": "12006200000711"
        }
    ]
}

service_207_customerId_body = {
    "version": "2.0",
    "type": "207",
    "id": "{{$guid}}",
    "dateTime": "05.10.2023 11:25:52.770434 +06:00",
    "source": "Creatio",
    "body": [
        {
            "customerId": "996553565311"
        }
    ]
}

service_207_proofNum_body = {
    "version": "2.0",
    "type": "207",
    "id": "{{$guid}}",
    "dateTime": "05.10.2023 11:25:52.770434 +06:00",
    "source": "Creatio",
    "body": [
        {
            "proofNum": "996553565311"
        }
    ]
}

service_001_body = {
    "version": "1.0",
    "type": "001",
    "id": str(uuid.uuid4()),
    "dateTime": "05.10.2023 11:25:52.770434 +06:00",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820006718250",
                "currency": "KGS",
                "name": "Дубов Александр Вадимович",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "accountCredit": {
                "department": "125008",
                "number": "1250820004787445",
                "currency": "KGS",
                "name": "Мухамеджанова Марьям Ахмаджановна",
                "inn": "12006200000711",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "amount": 1,
            "currency": "KGS",
            "description": "Перевод через Yourbi: FX at rate 88.32",
            "rateType": "RAT_JUR",
            "dealingRate": 88.32,
            "debitAmount": 10,
            "creditAmount": 0.11,
            "knp": {
                "gkpo": "55501000",
                "pb": "080402"
            }
        }
    ]
}

service_013_body = {
    "version": "1.0",
    "type": "013",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820004775119",
                "currency": "KGS",
                "name": "Мухамеджанова Марьям Ахмаджано",
                "inn": "12006200000711",
                "cardFl": 1,
                "processing": "OW4"
            },
            "accountCredit": {
                "department": "125008",
                "number": "1250820006718250",
                "currency": "KGS",
                "name": "Дубов Александр Вадимович",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "amount": 1,
            "currency": "KGS",
            "description": "Перевод через Yourbi: FX at rate 88.32",
            "rateType": "RAT_JUR",
            "dealingRate": 1,
            "debitAmount": 1,
            "creditAmount": 1,
            "knp": {
                "gkpo": "55501000",
                "pb": "080402"
            }
        }
    ]
}

service_014_body = {
    "version": "1.0",
    "type": "014",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820006718250",
                "currency": "KGS",
                "name": "Дубов Александр Вадимович",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "accountCredit": {

                "department": "125008",
                "number": "1250820004775119",
                "currency": "KGS",
                "name": "Мухамеджанова Марьям Ахмаджано",
                "inn": "12006200000711",
                "cardFl": 1,
                "processing": "OW4"
            },
            "amount": 1,
            "currency": "KGS",
            "description": "Перевод через Yourbi: FX at rate 88.32",
            "rateType": "RAT_JUR",
            "dealingRate": 1,
            "debitAmount": 1,
            "creditAmount": 1,
            "knp": {
                "gkpo": "55501000",
                "pb": "080402"
            }
        }
    ]
}

service_002_body = {
    "version": "1.0",
    "type": "002",
    "id": str(uuid.uuid4()),
    "dateTime": "29.07.2020 09:26:31.759000 +06:00",
    "source": "DBO",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125001",
                "number": "1250110000041083",
                "currency": "KGS",
                "name": "VISA Транзитный счет по списанию с ПК",
                "inn": "20508199401533",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "accountCredit": {
                "department": "125002",
                "number": "1250220000188322",
                "currency": "KGS",
                "name": "Рахимов Кучкарбай Ражапбайович",
                "inn": "21709196700070",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "amount": 64.44,
            "currency": "KGS",
            "description": "Пополнение счета 1250820001326464 в сумме 55.50 KGS",
            "knp": {
                "gkpo": "55501000",
                "pb": "080401",
                "vpb": "null"
            }
        }
    ]
}

service_003_body = {
    "version": "1.0",
    "type": "003",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820101177557",
                "currency": "USD",
                "name": "Дубов Александр Вадимович ИП тест",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "accountCredit": {
                "department": "125001",
                "number": "1250110100008172",
                "currency": "USD",
                "name": "VISA Транзитный счет по списанию с ПК",
                "inn": "20508199401533",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "amount": 10,
            "currency": "USD",
            "description": "Перевод через Yourbi: FX at rate 88.32",
            "rateType": "RAT_JUR",
            "dealingRate": 88.32,
            "debitAmount": 10,
            "creditAmount": 0.11,
            "knp": {
                "gkpo": "55501000",
                "pb": "080402"
            }
        }
    ]
}

service_007_body = {
    "version": "1.0",
    "type": "007",
    "id": str(uuid.uuid4()),
    "dateTime": "29.07.2020 09:26:31.759000 +06:00",
    "source": "DBO",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008"
            },
            "accountCredit": {
                "department": "125008",
                "number": "1250820001326464",
                "currency": "KGS"
            },
            "incomFl": 1,
            "amount": 10,
            "currency": "KGS",
            "knp": {
                "gkpo": "55501027",
                "pb": "null",
                "vpb": "null",
                "cashSign": "34"
            },
            "description": "Приход из кассы"
        }
    ]
}

service_008_body = {
    "version": "1.0",
    "type": "007",
    "id": str(uuid.uuid4()),
    "dateTime": "29.07.2020 09:26:31.759000 +06:00",
    "source": "DBO",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820001326464",
                "currency": "KGS"
            },
            "accountCredit": {
                "department": "125008"
            },
            "incomFl": 0,
            "amount": 10,
            "currency": "KGS",
            "knp": {
                "gkpo": "55501027",
                "pb": "null",
                "vpb": "null",
                "cashSign": "34"
            },
            "description": "Выдача из кассы"
        }
    ]
}

service_015_body = {
    "version": "1.0",
    "type": "015",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820004775119",
                "currency": "KGS",
                "name": "Мухамеджанова Марьям Ахмаджано",
                "inn": "12006200000711",
                "cardFl": 1,
                "processing": "OW4"
            },
            "accountCredit": {
                "department": "125008",
                "number": "1250820008709881",
                "currency": "KGS",
                "name": "Дубов А.В. ИП тест Элкарт",
                "inn": "22708199600981",
                "cardFl": 1,
                "processing": "IPC"
            },
            "amount": 4.00,
            "currency": "KGS",
            "description": "Перевод c карты на карту 4196-73**-****-0727 в сумме 80.00 KGS",
            "knp": {
                "gkpo": "55303005",
                "pb": "080501",
                "vpb": "null"
            }
        }
    ]
}

service_016_body = {
    "version": "1.0",
    "type": "016",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820004775119",
                "currency": "KGS",
                "name": "Мухамеджанова Марьям Ахмаджано",
                "inn": "12006200000711",
                "cardFl": 1,
                "processing": "OW4"
            },
            "accountCredit": {
                "department": "125001",
                "number": "1250110000041083",
                "currency": "KGS",
                "name": "VISA Транзитный счет по списанию с ПК",
                "inn": "20508199401533",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "amount": 4.00,
            "currency": "KGS",
            "description": "Перевод c карты на карту 4196-73**-****-0727 в сумме 80.00 KGS",
            "knp": {
                "gkpo": "55303005",
                "pb": "080501",
                "vpb": "null"
            }
        }
    ]
}

service_017_body = {
    "version": "1.0",
    "type": "017",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820004775119",
                "currency": "KGS",
                "name": "Мухамеджанова Марьям Ахмаджано",
                "inn": "12006200000711",
                "cardFl": 1,
                "processing": "OW4"
            },
            "accountCredit": {
                "department": "125001",
                "number": "1250110000041083",
                "currency": "KGS",
                "name": "VISA Транзитный счет по списанию с ПК",
                "inn": "20508199401533",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "amount": 4.00,
            "currency": "KGS",
            "description": "Перевод c карты на карту 4196-73**-****-0727 в сумме 80.00 KGS",
            "knp": {
                "gkpo": "55303005",
                "pb": "080501",
                "vpb": "null"
            }
        }
    ]
}