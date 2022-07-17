from flask import Flask

app = Flask(__name__)

import json

def load_candidates_from_json() ->list[dict]:
    """
    Возвращает спсиок всех кандидатов
    :param path:
    :return:
    """
    with open ('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates

def get_candidate_by_id(candidate_id):
    """
    Возвращает одного кандидатов по его id
    :param candidate_id:
    :return:
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate

def get_candidates_by_name(name) -> list:
    """
    Возвращает кадидатов по имени
    :param name:
    :return:
    """
    result=[]
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["name"] == name:
            result.append(candidate)
            return candidate
def get_candidates_by_skill(skill:str) -> list:
    """
    Возвращает кандидатов по навыку
    :param skill_name:
    :return:
    """

    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if skill in candidate["skills"].lwer().split(','):
            result.append(candidate)
    return result

# def form_candidates(candidates : list) -> str:
#         """Форматирование списков кандидатов"""
#         print("< h1 > Все кандидаты < / h1 > \n")
#
#         result = '<p>'
#
#         for candidate in candidates:
#             result += f"""
#                         <a href="/candidate/<{candidate["name"]}>">{candidate["name"]}</a></p>\n
#                     """
#         result += '</p>'
#         return result

# a=form_candidates(load_candidates_from_json())
# print(a)