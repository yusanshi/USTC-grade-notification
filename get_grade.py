import requests
import json
from bs4 import BeautifulSoup
from login import *


def get_grade(latest_only=False):
    # return a dict of all courses

    semester_ID_url = 'https://jw.ustc.edu.cn/for-std/grade/sheet/getSemesters'

    grade_url_base = 'https://jw.ustc.edu.cn/for-std/grade/sheet/getGradeList?trainTypeId=1&semesterIds='

    brow = login()
    semester_ID = brow.get(semester_ID_url, headers=headers)
    semester_ID = BeautifulSoup(semester_ID.text, 'lxml')
    semester_ID = json.loads(semester_ID.p.string)
    semester_ID = sorted([unit['id'] for unit in semester_ID])
    if latest_only:
        semester_ID = semester_ID[-1:]
    semester_ID = [str(unit) for unit in semester_ID]
    assert len(semester_ID) > 0
    semester_ID = ','.join(semester_ID)

    grade_url = grade_url_base + semester_ID

    grade_info = brow.get(grade_url, headers=headers)
    grade_info = BeautifulSoup(grade_info.text, 'lxml')
    grade_info = json.loads(grade_info.p.string)

    grade = {}

    for idx in range(len(grade_info['semesters'])):
        grade.update({x['courseNameCh']: x['score']
                      for x in grade_info['semesters'][idx]['scores']})

    return grade


if __name__ == "__main__":
    # Test
    print(get_grade(latest_only=True))
