headers = {
    "Content-Type": "application/json",
    'Authorization': 'Basic ZGJvOnBhc3MxMjM='
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

service_207_proofNum_body ={
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

