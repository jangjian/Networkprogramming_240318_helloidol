# helloidol

 - - -

1. startproject helloidol
   1. phthon -m pip install django~=4.2 (4.2의 최신버전 설치)
   2. django-admin startproject _helloidol_ .(현재 디렉토리)
   3. [python manage.py migrate]
   4. python manage.py runserver
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. _helloidol_/setting.py
      1. 'playground', in INSTALLED_APPS
3. playground/
   - 정보 전달 : urls -> views -> (models ->) templetes
   - 코드 작성 : (models -> )views -> templetes -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
      4. -> templates에 context 전달
   2. urls 
      1. _/playground/hello/_ -> _say_hello()_
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/ 
    1. urls, playground/urls
       1. _playground/_ -> _hello/_ -> _say_hello()_
       2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
       3. _playground/_ -> _bye_html/_ -> _say_bye_html()_

---
5. startapp T5
   1. Terminal
      1. python manage.py startapp T5
   2. helloidol/setting.py
      1. 'T5', in INSTALLED_APPS
6. T5
   1. views
      1. show_박지훈()
      2. show_김준규()
      3. show_윤재혁()
      4. show_김도영()
      5. show_소정환()
   2. templates/T5/
      1. 박지훈.html
         1. title : T5 - 박지훈
         2. h1 : T5
         3. h2 : 박지훈
         4. img : 박지훈 프로필 사진
            1. boder-radius : 50%
      2. 김준규.html
      3. 윤재혁.html
      4. 김도영.html
      5. 소정환.html
   3. urls
      1. T5/ -> 박지훈/ -> show_박지훈()
      2. T5/ -> 김준규/ -> show_김준규()
      3. T5/ -> 윤재혁/ -> show_윤재혁()
      4. T5/ -> 김도영/ -> show_김도영()
      5. T5/ -> 소정환/ -> show_소정환()