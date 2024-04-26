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