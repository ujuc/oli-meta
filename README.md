# Oil meta

* [opinet](http://www.opinet.co.kr)에 보여지는 주유소별 휘발유, 경유 가격을 읽어와 보여준다.

## 사용 방법

```shell script
poetry run crawler.py <시도 이름>

# or
python crawler.py <시도 이름>
```

## 데이터

* 주유소 상표명
* 주유소 명
* 휘발유 가격
* 경유 가격

## 사용 패키지

* Beautiful Soup : HTML 파서
* pytest : python test 패키지. 테스트를 보여주는 것이 잘보여서 사용
* poetry : 패키지 매니저. 패키지들을 명시해두거나 주변 작업들이 가능하게 구성할 수 있음.
* block : code formatter. IDEA를 쓰면 알아서 해주긴하지만 혹시나하여.
