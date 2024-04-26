import configuration
import requests
import data

def get_users_table():
    return requests.get(configuration.url_esb)

response = get_users_table()


# print(response)
# print(response.status_code)
# print(response.headers)

def service_post(body):
    return requests.post(configuration.url_esb,
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

#response = service_post(data.);