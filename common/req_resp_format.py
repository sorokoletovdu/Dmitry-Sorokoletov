def pprint_req(request):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '===========Request===========>',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )


def pprint_res(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<===========Response===========',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )
