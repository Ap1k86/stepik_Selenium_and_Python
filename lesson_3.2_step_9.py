s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('is')
if index != -1:
    print(f'Substring found at index {index}')
# same


def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
