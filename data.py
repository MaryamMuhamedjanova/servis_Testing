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
    "id": str(uuid.uuid4()),
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
    "id": str(uuid.uuid4()),
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
    "id": str(uuid.uuid4()),
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
    "id": str(uuid.uuid4()),
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
    "id": str(uuid.uuid4()),
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
    "id": str(uuid.uuid4()),
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
    "id": str(uuid.uuid4()),
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
            "amount": 10,
            "currency": "KGS",
            "description": "Перевод через Yourbi: FX at rate 88.32",
            "rateType": "RAT_JUR",
            "dealingRate": 90,
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
    "type": "008",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
             "accountDebit": {
                "department": "125001",
                "number": "1250110000041083",
                "currency": "KGS"
            },
            "accountCredit": {
                "department": "125001"
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

service_019_body = {
    "version": "1.0",
    "type": "019",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125008",
                "number": "1250820004775119",
                "currency": "KGS"
            },
            "accountCredit": {
                "department": "125008"
            },
            "bnkOper": "02083",
            "amount": 10.50,
            "currency": "KGS"
        }
    ]
}

service_020_body = {
    "version": "1.0",
    "type": "020",
    "id": str(uuid.uuid4()),
    "dateTime": "08.05.2024 13:54:57.664",
    "source": "Creatio",
    "instance": "COLVIR118",
    "body": [
        {
            "accountDebit": {
                "department": "125001",
                "number": "1250110000041083",
                "currency": "KGS"
            },
            "accountCredit": {
                "department": "125001"
            },
            "bnkOper": "02083",
            "amount": 10.50,
            "currency": "KGS"
        }
    ]
}

service_021_body = {
    "version": "1.0",
    "type": "021",
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
            "amount": 100.00,
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

service_022_body = {
    "version": "1.0",
    "type": "022",
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
            "amount": 1.00,
            "currency": "KGS",
            "description": "перевод с депозита на acc",
            "knp": {
                "gkpo": "55303005",
                "pb": "080501",
                "vpb": "null"
            }
        }
    ]
}

service_023_body = {
    "version": "1.0",
    "type": "023",
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
            "amount": 1.00,
            "currency": "KGS",
            "description": "перевод с депозита на карту ",
            "knp": {
                "gkpo": "55303005",
                "pb": "080501",
                "vpb": "null"
            }
        }
    ]
}

service_024_body = {
    "version": "1.0",
    "type": "024",
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
            "amount": 10.00,
            "currency": "KGS",
            "description": "перевод с депозита на карту ",
            "knp": {
                "gkpo": "55303005",
                "pb": "080501",
                "vpb": "null"
            }
        }
    ]
}

service_clientCreate_body = {
    "version": "1.0",
    "type": "client.create",
    "noSanctionFl": 1,
    "noAmlFl": 1,
    "source": "Creatio",
    "id": str(uuid.uuid4()),
    "dateTime": "23.11.2021 09:22:06.409",
    "colvirUser": "CRM2",
    "instance": "COLVIR118",
    "body": [
        {
            "department": "125003",
            "serviceGroup": "125003.000",
            "surname": "Бебеза",
            "name": "Лора",
            "fatherName": "Юсузовна",
            "shortName": "Бебеза Л.",
            "latinSurname": "Bebeza",
            "latinName": "Lora",
            "latinFatherName": "Iusuzovna",
            "notes": "UZENBAEVA",
            "pastName": "Bebeza Lora",
            "inn": "10601198800049",
            "birthDate": "11.08.1993",
            "pboyulFl": 0,
            "jurFl": 0,
            "residFl": 1,
            "citizenship": "KG",
            "economySector": "9",
            "economyBranch": "115",
            "sex": "M",
            "title": 1,
            "trfPlnCategory": "2003",
            "additionalInfo": [
                {
                    "code": "ADD_ACCTYPE",
                    "value": "04"
                },
                {
                    "code": "ADD_ACCTYPENM",
                    "value": "Физические лица"
                },
                {
                    "code": "FATCA",
                    "value": "Не FATCA"
                },
                {
                    "code": "FATCA_DATE",
                    "value": "10.11.2021"
                },
                {
                    "code": "SCHP",
                    "value": "6"
                },
                {
                    "code": "INCOME",
                    "value": "0"
                },
                {
                    "code": "CATEGORY",
                    "value": "Прочий"
                },
                {
                    "code": "ZKG_CLI_SOURCE",
                    "value": "CRM"
                },
                {
                    "code": "FAMSTAT",
                    "value": "1"
                },
                {
                    "code": "Z069_WORKORG",
                    "value": "ОсОО Форестер"
                },
                {
                    "code": "ACTIVITY",
                    "value": "Водитель"
                },
                {
                    "code": "NATION",
                    "value": "Кыргыз"
                },
                {
                    "code": "KM_REGFL",
                    "value": "0"
                },
                {
                    "code": "ZKG_CLI_EMP",
                    "value": "SHABAZA"
                }
            ],
            "identityDocuments": [
                {
                    "type": "07",
                    "number": "22550008",
                    "expire": "11.12.2024",
                    "issue": "11.12.2014",
                    "issuer": "МКК-5022",
                    "series": "ID",
                    "defaultFl": 1
                },
                {
                    "type": "03",
                    "number": "2255009",
                    "expire": "11.12.2024",
                    "issue": "11.12.2014",
                    "issuer": "MINOBR-5022",
                    "series": "AK"
                }
            ],
            "contacts": [
                {
                    "contactId": 4,
                    "kind": "MOBILE",
                    "value": "0550618090",
                    "note": ""
                },
                {
                    "type": "PHN",
                    "kind": "WORK",
                    "value": "0312618090",
                    "note": ""
                }
            ],
            "addresses": [
                {
                    "type": "GCLIADR_REG",
                    "ownershipsType": "OTHER",
                    "value": "КЫРГЫЗСТАН, ЧУЙСКАЯ ОБЛ., МОСКОВСКИЙ Р-Н, АЛЕКСАНДРОВСКИЙ А/А, С. АЛЕКСАНДРОВКА, УЛИЦА КОМСОМОЛЬСКАЯ, ДОМ 140",
                    "note": ""
                },
                {
                    "type": "GCLIADR_LIVE",
                    "ownershipsType": "OWNER",
                    "value": "КЫРГЫЗСТАН, КЫРГЫЗСТАН, ЧУЙСКАЯ ОБЛ.,  МОСКОВСКИЙ Р-Н, АЛЕКСАНДРОВКА А., КОМСОМОЛЬСКАЯ КӨЧ., 140",
                    "note": ""
                }
            ],
            "roles": [
                "CLI"
            ],
            "offerContracts": [
                {
                    "type": "HARD_COPY",
                    "typeName": "Физическое заявление-анкета",
                    "acceptFl": "1",
                    "signDate": "20.12.2021",
                    "offerDepartment": "125003",
                    "signSubTypeId": 1,
                    "source": "CRM",
                    "dscr": ""
                }
            ],
            "bnkAffiliate": [
                {
                    "type": "04",
                    "fromDate": "21.12.2021",
                    "toDate": ""
                }
            ],
            "relatives": [
                {
                    "relativeType": "54",
                    "fromDate": "20.10.1999",
                    "toDate": "",
                    "relativeSurname": "",
                    "relativeName": "",
                    "relativeFatherName": "",
                    "relativeAbsCode": "008.125682",
                    "note": ""
                }
            ],
            "AMLForm": {
                "registrationDate": "31.12.21",
                "note": "ПК",
                "attributes": [
                    {
                        "attributeId": 1157,
                        "value": "31.12.21"
                    },
                    {
                        "attributeId": 1158,
                        "value": "0"
                    }
                ]
            },
            "identification": {
                "department": "125003",
                "level": "3",
                "time": "28.03.2022 08:46:15",
                "note": "Клиент идентифицирован в системе CRM",
                "source": "CRM"
            },
            "operations": [
                {
                    "code": "OPN"
                }
            ]
        }
    ]
}

service_depositCreate_body = {
  "type": "deposit.create",
  "version": "1.0",
  "noSanctionFl": 1,
  "source": "BPM.Deposit",
  "id":  str(uuid.uuid4()),
  "dateTime": "11.09.2023 13:15:13",
  "instance": "COLVIR118",
  "body": [
    {
      "department": "125008",
      "dclCode": "NV",
      "subDclCode": "NVCRM",
      "creTermType": "M",
      "creTerm": 36,
      "prcRate": 12.0,
      "currency": "KGS",
      "amount": 700.0,
      "date": "11.09.2023",
      "absCode": "008.119115",
      "depositContractParameters": [
        {
          "value": "0",
          "code": "D_PROLARCFL"
        },
        {
          "value": "W",
          "code": "L_CAP_SERVICING"
        },
        {
          "value": "1",
          "code": "L_CAP_NEEDUPDATE"
        },
        {
          "value": "BPM",
          "code": "DEPO_SRC_CHANNEL"
        }
      ],
      "depositPaymentAttributes": [
        {
          "accAbsCode": "1250820004787445",
          "accType": "CLIACC",
          "department": "125008",
          "note": ""
        }
      ],
      "depositPaymentSettings": [
        {
          "amountType": "Прием вклада переводом",
          "paymentType": "Безналично",
          "accAbsCode": "1250820004787445"
        },
        {
          "amountType": "Сумма депозита",
          "paymentType": "Безналично",
          "accAbsCode": "1250820004787445"
        },
        {
          "amountType": "Возврат депозита",
          "paymentType": "Безналично",
          "accAbsCode": "1250820004787445"
        },
        {
          "amountType": "Выплата вознаграждения по депозиту",
          "paymentType": "Безналично",
          "accAbsCode": "1250820004787445"
        }
      ],
      "operations": [
        {
          "code": "OPENACC"
        },
        {
          "code": "SHD_CALC"
        },
        {
          "code": "CALCAPR"
        },
        {
          "code": "REG_SHD"
        },
        {
          "code": "GET_DEPOSIT"
        }
      ]
    }
  ]
}

service_creditCreate_body = {
  "version": "1.0",
  "type": "credit.create",
  "id": str(uuid.uuid4()),
  "dateTime": "15.03.2024 15:51:47.372122 +06:00",
  "source": "Creatio118",
  "colvirUser": "CRM2",
  "body": [
    {
      "department": "125002",
      "absCode": "008.119115",
      "dclCode": "013НС_А",
      "creditCode": "02N-КД-24-54816/1-РБ",
      "creditStartDate": "15.03.2024",
      "creditRegDate": "15.03.2024",
      "creTermType": "M",
      "creTerm": 12,
      "currency": "KGS",
      "amount": 30000.00,
      "creIssueFee": 0.00,
      "prcRate": 24.00,
      "principalOverdueFee": 0.07,
      "crePurposeId": 187,
      "additionalInfo": [
        {
          "code": "8288",
          "value": "1"
        },
        {
          "code": "7989",
          "value": "1"
        },
        {
          "code": "8233",
          "value": "1"
        },
        {
          "code": "8728",
          "value": "15.03.2024"
        },
        {
          "code": "1501",
          "value": "15"
        },
        {
          "code": "8168",
          "value": "1250820003648808"
        },
        {
          "code": "8148",
          "value": "4"
        },
        {
          "code": "8128",
          "value": "15.03.2024"
        },
        {
          "code": "8648",
          "value": "001620"
        },
        {
          "code": "8608",
          "value": "MIB"
        },
        {
          "code": "8548",
          "value": "Народная-онлайн (кредит в KGS)"
        }
      ],
      "analytics": [
        {
          "code": 371784,
          "value": "509"
        },
        {
          "code": 373504,
          "value": "509.6"
        },
        {
          "code": 373544,
          "value": "6"
        }
      ],
      "creditPaymentAttributes": [
        {
          "accAbsCode": "1250820004787445",
          "department": "125008",
          "accType": "CLIACC"
        }
      ],
      "operations": [
        {
          "code": "CALCSHD",
          "parameters": []
        },
        {
          "code": "CREDITRATE",
          "parameters": [
            {
              "code": "REASON",
              "value": "выдача займа"
            },
            {
              "code": "RES_VALUE",
              "value": "1"
            }
          ]
        }
      ]
    }
  ]
}

service_accountCreate_body = {
    "version": "1.0",
    "type": "account.create",
    "id": str(uuid.uuid4()),
    "dateTime": "15.09.2023 02:56:44",
    "source": "BAAS.AccountCreate",
     "instance": "COLVIR118",
    "body": [
        {
            "department": "125008",
            "ledgerAccount": "20201",
            "serviceGroup": "125008.000",
            "client": "008.119115",
            "name": "Мухамеджданова Марьям Ахмаджановна",
            "currency": "KGS",
            "analytics": [
                {
                    "code": "DEPARTMENT",
                    "value": "125008"
                },
                {
                    "code": "ZGL_KZT",
                    "value": "2209001kz"
                }
            ],
            "addAttributes": "",
            "operations": ""
        }
    ]
}

service_directoriesExchangeRatesRead_body = {
    "type": "directories.exchangeRates.read",
    "version": "1.0",
    "id": str(uuid.uuid4()),
    "dateTime": "14.10.2021 09:20:37.955",
    "source": "TEST",
    "instance": "COLVIR118",
    "body": [
        {
            "filter": {
                "buyCurrency": "KGS",
                "sellCurrency": "USD",
                "department": "125008"
            }
        }
    ]
}

service_cashOrderCreate_body = {
    "version": "1.0",
    "type": "cashOrder.create",
    "noSanctionFl": 1,
    "cancelCheckFl": 1,
    "id": str(uuid.uuid4()),
    "dateTime": "31.05.2024 13:28:39.887235 +06:00",
    "source": "Creatio",
    "colvirUser": "GMURSALIEVA",
    "instance": "COLVIR118",
    "body": [
        {
            "incomFl": 1,
            "accountDebit": {
                "department": "125008"
            },
            "accountCredit": {
                "department": "125008",
                "number": "1250820004787445",
                "currency": "KGS"
            },
            "amount": 19.00,
            "currency": "KGS",
            "bnkOper": "B1010",
            "docNum": "09-035832",
            "docDate": "31.05.2024",
            "operDate": "31.05.2024",
            "knp": {
                "gkpo": "55303005",
                "pb": "",
                "vpb": ""
            },
            "description": "Пополнение счета",
            "payer": "Рысбеков Серик Токторбайевич",
            "identityDocument": "Паспорт гражданина КР (ID-карта) ID 1551801 МКК 211031 17.01.2020",
            "additionalInfo": [
                {
                    "code": "Z069_ADDRESS",
                    "value": "КЫРГЫЗСТАН, ИССЫК- КУЛСЬКАЯ обл, ИССЫК КУЛЬКИЙ р-н, БАЛЫКЧИ г, ЛЕОНОВА ул, дом 15"
                },
                {
                    "code": "Z069_BIRTHDATE",
                    "value": "25.05.1984"
                },
                {
                    "code": "Z069_BIRTHPLACE",
                    "value": ""
                },
                {
                    "code": "Z069_CITIZENSHIP",
                    "value": "Кыргызстан"
                },
                {
                    "code": "Z069_CONTACTS",
                    "value": "0772 677789"
                },
                {
                    "code": "Z069_INN",
                    "value": "22505198400193"
                },
                {
                    "code": "Z069_MARITAL",
                    "value": "Женат/Замужем"
                },
                {
                    "code": "Z069_NATIONALITY",
                    "value": "казах"
                },
                {
                    "code": "Z069_RESIDFL",
                    "value": "1"
                },
                {
                    "code": "Z069_VISA_REG",
                    "value": ""
                }
            ],
            "signatures": {
                "head": ""
            },
            "cashPlanSymbols": [
                {
                    "symbol": "13",
                    "amount": 19.00
                }
            ],
            "operations": [
                {
                    "code": "REG",
                    "parameters": []
                },
                {
                    "code": "POST2",
                    "parameters": []
                }
            ]
        }
    ]
}

service_holdCreate_body = {
    "type" : "hold.create",
    "version" : "1.0",
    "id": str(uuid.uuid4()),
    "dateTime" : "12.10.2021 13:06:54.981000 +06:00",
    "source" : "TEST",
    "instance": "COLVIR118",
    "body" : [{
        "account" : {
            "number" : "1250820004787445",
            "department" : "125008"
        },
        "limType" : "L",
        "amount" : 1,
        "currency" : "KGS",
        "description" : "Тестовый холд"
    }]
}

service_holdDelete_body = {
    "type" : "hold.delete",
    "version" : "1.0",
    "id": str(uuid.uuid4()),
    "dateTime" : "12.10.2021 13:06:54.981000 +06:00",
    "source" : "TEST",
    "instance": "COLVIR118",
    "body": [
        {
            "holdId": 301054
        }
    ]
}

service_directoriesUniversal_body = {
    "type": "directories.universal",
    "version": "1.0",
    "id": str(uuid.uuid4()),
    "dateTime": "21.10.2021 13:06:54.981000 +06:00",
    "source": "TEST",
    "instance": "COLVIR118",
    "body": [
        {
            "directoryCode": "G_CLIAUTHPRS_PLACE"
        }
    ]
}