# Урок 21. Проектирование. Паттерны. SOLID.

![](https://www.meme-arsenal.com/memes/9178b441f9d53476a4678e8308f6e002.jpg)

## OOA --> OOD --> OOP

OOA - объектно-ориентированный анализ. Если страшной терминологией, то это методология, при которой требования к системе
воспринимаются с точки зрения классов и объектов, выявленных в предметной области.

ООД - объектно-ориентированный дизайн. Опять же, если страшными терминами, то это методология проектирования,
соединяющая в себе процесс объектной декомпозиции и приемы представления логической и физической, а также статической и
динамической моделей проектируемой системы.

![](https://intellect.icu/th/25/blogs/id7888/2351a98acf1a7d963aed72c6a6b8c0a2.jpg)

Как это работает?

ООА - это оценка того, какие проблемы должна решать система и какие сущности у нас вообще существуют (допустим, при
проектировании интернет-магазина нужно понимать, что у нас будут сущности пользователя, товара, заказа и т. д.)

ООД - это проектирование необходимых классов и того, как они будут взаимодействовать. (Понимание, что заказ будет
совершать пользователь, при этом заказ может быть розничным и оптовым, и для того, чтобы их просчитать, необходима
различная логика, какие паттерны мы можем применить (об этом немного позже))

ООП в этой схеме - это конкретная реализация того, что было продумано на этапе ООД, основываясь на принципах ООП 
(садимся и пишем код).

## Подход к проектированию

Вне зависимости от того, что вы разрабатываете, всегда можно применять два принципа:

**KISS** = Keep it simple, stupid (Чем проще, тем лучше! Если всё можно описать двумя классами, в которых 3 метода, то 
не надо описывать 10 классов с 30-ю методами.)

**DRY** = Don't repeat yourself (Не повторяйся! Если ты используешь один и тот же код в разных местах, сделай из него 
функцию или метод)

![](https://intellect.icu/th/25/blogs/id7888/d78a87c0507fff4ae6cc91ac89031d11.png)

Про процедурное программирование и про Domain-driven design мы подробно говорить не будем. Скажем лишь, что процедурное
программирование - это другой подход к организации кода, где в основе всего идёт процедура, а не объект. А DDD 
(предметно-ориентированное проектирование) - это подход к дизайну, основанный на предметных областях.

Test-driven development - это подход к разработке, когда тесты пишутся до кода. Смысл в том, что если проектирование
было проведено правильно, то ты заранее знаешь, какие в твоей системе будут действия, и как система должна реагировать 
на разные действия. Тогда можно написать тесты, которые будут отвечать требованиям проектирования, и только после этого
писать код, который будет соответствовать уже написанным тестам.

## SOLID

SOLID - это свод пяти основных принципов ООП, введенный Майклом Фэзерсом в начале нулевых. Эти принципы — часть общей
стратегии гибкой и адаптивной разработки, их соблюдение облегчает расширение и поддержку проекта.

### Принципы

SOLID принципы советуют, как проектировать модули, т. е. кирпичикам, из которых строится приложение. Цель принципов —
проектировать модули, которые:

- способствуют изменениям

- легко понимаемы

- повторно используемы

#### SRP: The Single Responsibility Principle (S)

> A module should be responsible to one, and only one, actor.

Старая формулировка: A module should have one, and only one, reason to change.

Часто ее трактовали следующим образом: Модуль должен иметь только одну обязанность. И это главное заблуждение при
знакомстве с принципами. Все несколько хитрее.

На каждом проекте люди играют разные роли (actor): Аналитик, Проектировщик интерфейсов, Администратор баз данных.
Естественно, один человек может играть сразу несколько ролей. В этом принципе речь идет о том, что изменения в модуле
может запрашивать одна и только одна роль. Например, есть модуль, реализующий некую бизнес-логику, запросить изменения в
этом модуле может только Аналитик, но никак не DBA или UX.

#### OCP: The Open Closed Principle (O)

> A software artifact should be open for extension but closed for modification.

Старая формулировка: You should be able to extend a class's behavior, without modifying it.

Это определенно может ввести в ступор. Как можно расширить поведение класса без его модификации? В текущей формулировке
Роберт Мартин оперирует понятием артефакт, т.е. jar, dll, gem, npm package. Чтобы расширить поведение, нужно
воспользоваться динамическим полиморфизмом.

Например, наше приложение должно отправлять уведомления. Используя dependency inversion, наш модуль объявляет только
интерфейс отправки уведомлений, но не реализацию. Таким образом, логика нашего приложения содержится в одном dll файле,
а класс отправки уведомлений, реализующий интерфейс — в другом. Таким образом, мы можем без изменения (перекомпиляции)
модуля с логикой использовать различные способы отправки уведомлений.

Этот принцип тесно связан с LSP и DIP, которые мы рассмотрим далее.

#### LSP: The Liskov Substitution Principle (L)

Потомок может заменить родителя.

Имеет сложное математическое определение, которое можно заменить на: "Функции, которые используют базовый тип, должны
иметь возможность использовать подтипы базового типа, не зная об этом."

Классический пример нарушения. Есть базовый класс `Stack`, реализующий следующий интерфейс: `length`, `push`, `pop`. И 
есть потомок `DoubleStack`, который дублирует добавляемые элементы. Естественно, класс `DoubleStack` нельзя 
использовать вместо `Stack`.

У этого принципа есть забавное следствие: Объекты, моделирующие сущности, не обязаны реализовывать отношения этих
сущностей. Например, у нас есть целые и вещественные числа, причем целые числа — подмножество вещественных. Однако,
double состоит из двух int: мантиссы и экспоненты. Если бы int наследовал от double, то получилась бы забавная картина:
родитель содержит 2-х своих детей.

В качестве второго примера можно привести Generics. Допустим, есть базовый класс `Shape` и его потомки `Circle` и 
`Rectangle`. И есть некая функция `Foo(List list)`. Мы считаем, что `List` можно привести к `List`. Однако, это не так. 
Допустим, это приведение возможно, но тогда в `list` можно добавить любую фигуру, например `rectangle`. А изначально 
`list` должен содержать только объекты класса `Circle`.

#### ISP: The Interface Segregation Principle (I)

> Make fine grained interfaces that are client specific.

Разделение интерфейса облегчает использование и тестирование модулей.

Если есть метод, который при разных входных данных ведёт себя по-разному, то лучше написать несколько методов.

#### DIP: The Dependency Inversion Principle (D)

> Depend on abstractions, not on concretions.

Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций.
Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций. Что такое модули верхних уровней? Как
определить этот уровень? Как оказалось, все очень просто. Чем ближе модуль к вводу/выводу, тем ниже уровень модуля. Т.е.
модули, работающие с BD, интерфейсом пользователя, — низкого уровня. А модули, реализующие бизнес-логику — высокого
уровня.

Что такое зависимость модулей? Это ссылка на модуль в исходном коде, т.е. `import`, `require` и т.п. С помощью 
динамического полиморфизма в runtime можно обратить эту зависимость.

Принципы SOLID стремятся свести изменение модулей к их добавлению и удалению.

Принципы SOLID способствуют откладыванию принятия технических решений и разделению труда программистов.

Таким образом:

- Принцип единственной ответственности (Single responsibility)

> На каждый объект должна быть возложена одна единственная обязанность

Для этого проверяем, сколько у нас есть причин для изменения класса — если больше одной, то следует разбить данный 
класс.

- Принцип открытости/закрытости (Open-closed)

> Программные сущности должны быть открыты для расширения, но закрыты для модификации

Для этого представляем наш класс как «черный ящик» и смотрим, можем ли в таком случае изменить его поведение.

- Принцип подстановки Барбары Лисков (Liskov substitution)

> Объекты в программе могут быть заменены их наследниками без изменения свойств программы

Для этого проверяем, не усилили ли мы предусловия и не ослабили ли постусловия. Если это произошло — то принцип не 
соблюдается.

- Принцип разделения интерфейса (Interface segregation)

> Много специализированных интерфейсов лучше, чем один универсальный

Проверяем, насколько много интерфейс содержит методов и насколько разные функции накладываются на эти методы, и если 
необходимо — разбиваем интерфейсы.

- Принцип инверсии зависимостей (Dependency Invertion)

> Зависимости должны строиться относительно абстракций, а не деталей

Проверяем, зависят ли классы от каких-то других классов (непосредственно инстанцируют объекты других классов и т. д.) и 
если эта зависимость имеет место, заменяем на зависимость от абстракции.

### Паттерны проектирования

![](https://kloud-blogwpsite-ause-prd-web.azurewebsites.net/wp-content/uploads/2017/02/60288347.jpg)

На самом деле, паттерн - это просто любая шаблонная конструкция, которую можно использовать несколько раз. И вы даже
знаете несколько паттернов, только не знаете, что это паттерны :)

Например, декоратор, итератор, генератор (нет, не все паттерны заканчиваются на -ратор).

Паттернов существует просто огромное количество, настолько огромное, что существуют сотни книг по паттернам
проектирования. [Тут](http://design-pattern.ru/patterns/) можно посмотреть на многие из них, но далеко не на все.

## Что такое паттерн?

Паттерн проектирования — это часто встречающееся решение определённой проблемы при проектировании архитектуры программ.

В отличие от готовых функций или библиотек паттерн нельзя просто взять и скопировать в программу. Паттерн представляет
собой не какой-то конкретный код, а общую концепцию решения той или иной проблемы, которую нужно будет ещё подстроить
под нужды вашей программы.

Паттерны часто путают с алгоритмами, ведь оба понятия описывают типовые решения каких-то известных проблем. Но если
алгоритм — это чёткий набор действий, то паттерн — это высокоуровневое описание решения, реализация которого может
отличаться в двух разных программах.

Если привести аналогии, то алгоритм — это кулинарный рецепт с чёткими шагами, а паттерн — инженерный чертёж, на котором
нарисовано решение, но не конкретные шаги его реализации.

### Из чего состоит паттерн?

Описания паттернов обычно очень формальны и чаще всего состоят из таких пунктов:

- проблема, которую решает паттерн;
- мотивация к решению проблемы способом, который предлагает паттерн;
- структура классов, составляющих решение;
- пример на одном из языков программирования;
- особенности реализации в различных контекстах;
- связи с другими паттернами.

Такой формализм в описании позволил создать обширный каталог паттернов, проверив каждый из них на состоятельность.

### Зачем знать паттерны?

Вы можете вполне успешно работать, не зная ни одного паттерна. Более того, вы могли уже не раз реализовать какой-то из
паттернов, даже не подозревая об этом.

Но осознанное владение инструментом как раз и отличает профессионала от любителя. Вы можете забить гвоздь молотком, а
можете и дрелью, если сильно постараетесь. Но профессионал знает, что главная фишка дрели совсем не в этом. Итак, зачем
же знать паттерны?

- Проверенные решения. Вы тратите меньше времени, используя готовые решения, вместо повторного изобретения велосипеда.
  До некоторых решений вы смогли бы додуматься и сами, но многие могут быть для вас открытием.

- Стандартизация кода. Вы делаете меньше просчётов при проектировании, используя типовые унифицированные решения, так
  как все скрытые проблемы в них уже давно найдены.

- Общий программистский словарь. Вы произносите название паттерна, вместо того, чтобы час объяснять другим
  программистам, какой крутой дизайн вы придумали и какие классы для этого нужны.

## Классификация паттернов

Паттерны отличаются по уровню сложности, детализации и охвату проектируемой системы. Проводя аналогию со строительством,
вы можете повысить безопасность перекрёстка, поставив светофор, а можете заменить перекрёсток целой автомобильной
развязкой с подземными переходами.

Самые низкоуровневые и простые паттерны — идиомы. Они не универсальны, поскольку применимы только в рамках одного языка
программирования.

Самые универсальные — архитектурные паттерны, которые можно реализовать практически на любом языке. Они нужны для
проектирования всей программы, а не отдельных её элементов.

- `Порождающие` паттерны беспокоятся о гибком создании объектов без внесения в программу лишних зависимостей.

- `Структурные` паттерны показывают различные способы построения связей между объектами.

- `Поведенческие` паттерны заботятся об эффективной коммуникации между объектами

[Тут](https://refactoring.guru/) шикарный сайт с описанием некоторых паттернов и их реализации на разных языках
программирования.

### Рассмотрим некоторые паттерны

#### Итератор

Итератор — это поведенческий паттерн проектирования, который даёт возможность последовательно обходить элементы
составных объектов, не раскрывая их внутреннего представления.

Коллекции — самая распространённая структура данных, которую вы можете встретить в программировании. Это набор объектов,
собранный в одну кучу по каким-то критериям.

Большинство коллекций выглядят как обычный список элементов. Но есть и экзотические коллекции, построенные на основе
деревьев, графов и других сложных структур данных.

Но как бы ни была структурирована коллекция, пользователь должен иметь возможность последовательно обходить её элементы,
чтобы проделывать с ними какие-то действия.

Но каким способом следует перемещаться по сложной структуре данных? Например, сегодня может быть достаточным обход
дерева в глубину, но завтра потребуется возможность перемещаться по дереву в ширину. А на следующей неделе и того хуже —
понадобится обход коллекции в случайном порядке.

Добавляя всё новые алгоритмы в код коллекции, вы понемногу размываете её основную задачу, которая заключается в
эффективном хранении данных. Некоторые алгоритмы могут быть и вовсе слишком «заточены» под определённое приложение и
смотреться дико в общем классе коллекции.

Идея паттерна Итератор состоит в том, чтобы вынести поведение обхода коллекции из самой коллекции в отдельный класс.

Объект-итератор будет отслеживать состояние обхода, текущую позицию в коллекции и сколько элементов ещё осталось обойти.
Одну и ту же коллекцию смогут одновременно обходить различные итераторы, а сама коллекция не будет даже знать об этом.

К тому же, если вам понадобится добавить новый способ обхода, вы сможете создать отдельный класс итератора, не изменяя
существующий код коллекции.

#### Декоратор

Декоратор — это структурный паттерн проектирования, который позволяет динамически добавлять объектам новую
функциональность, оборачивая их в полезные «обёртки».

Вы работаете над библиотекой оповещений, которую можно подключать к разнообразным программам, чтобы получать уведомления
о важных событиях.

Основой библиотеки является класс `Notifier` с методом `send`, который принимает на вход строку-сообщение и высылает 
её всем администраторам по электронной почте. Сторонняя программа должна создать и настроить этот объект, указав, кому 
отправлять оповещения, а затем использовать его каждый раз, когда что-то случается.

В какой-то момент стало понятно, что одних email-оповещений пользователям мало. Некоторые из них хотели бы получать
извещения о критических проблемах через SMS. Другие хотели бы получать их в виде сообщений Facebook. Корпоративные
пользователи хотели бы видеть сообщения в Slack.

Сначала вы добавили каждый из этих типов оповещений в программу, унаследовав их от базового класса `Notifier`. Теперь
пользователь выбирал один из типов оповещений, который и использовался в дальнейшем.

Но затем кто-то резонно спросил, почему нельзя выбрать несколько типов оповещений сразу? Ведь если вдруг в вашем доме
начался пожар, вы бы хотели получить оповещения по всем каналам, не так ли?

Вы попытались реализовать все возможные комбинации подклассов оповещений. Но после того, как вы добавили первый десяток
классов, стало ясно, что такой подход невероятно раздувает код программы.

Наследование — это первое, что приходит в голову многим программистам, когда нужно расширить какое-то существующее
поведение. Но механизм наследования имеет несколько досадных проблем.

Он статичен. Вы не можете изменить поведение существующего объекта. Для этого вам надо создать новый объект, выбрав
другой подкласс. Он не разрешает наследовать поведение нескольких классов одновременно. Из-за этого вам приходится
создавать множество подклассов-комбинаций для получения совмещённого поведения. Одним из способов обойти эти проблемы
является замена наследования агрегацией либо композицией. Это когда один объект содержит ссылку на другой и делегирует
ему работу, вместо того чтобы самому наследовать его поведение. Как раз на этом принципе построен паттерн Декоратор.

#### Одиночка

![](https://i.pinimg.com/originals/ce/8b/ef/ce8bef2daa2ad2b583e5cbdbde537bbc.jpg)

Одиночка — это порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр, и
предоставляет к нему глобальную точку доступа.

Одиночка решает сразу две проблемы, нарушая принцип единственной ответственности класса.

Гарантирует наличие единственного экземпляра класса. Чаще всего это полезно для доступа к какому-то общему ресурсу,
например, базе данных.

Представьте, что вы создали объект, а через некоторое время пробуете создать ещё один. В этом случае хотелось бы
получить старый объект, вместо создания нового.

Такое поведение невозможно реализовать с помощью обычного конструктора, так как конструктор класса всегда возвращает
новый объект.

Предоставляет глобальную точку доступа. Это не просто глобальная переменная, через которую можно достучаться к
определённому объекту. Глобальные переменные не защищены от записи, поэтому любой код может подменять их значения без
вашего ведома.

Но есть и другой нюанс. Неплохо бы хранить в одном месте и код, который решает проблему №1, а также иметь к нему простой
и доступный интерфейс.

Интересно, что в наше время паттерн стал настолько известен, что теперь люди называют «одиночками» даже те классы,
которые решают лишь одну из проблем, перечисленных выше.

Все реализации одиночки сводятся к тому, чтобы скрыть конструктор по умолчанию и создать публичный статический метод,
который и будет контролировать жизненный цикл объекта-одиночки.

Если у вас есть доступ к классу одиночки, значит, будет доступ и к этому статическому методу. Из какой точки кода вы бы
его ни вызвали, он всегда будет отдавать один и тот же объект.

Правительство государства — хороший пример одиночки. В государстве может быть только одно официальное правительство. Вне
зависимости от того, кто конкретно заседает в правительстве, оно имеет глобальную точку доступа «Правительство страны
N».

#### Фасад

Фасад — это структурный паттерн проектирования, который предоставляет простой интерфейс к сложной системе классов,
библиотеке или фреймворку.

Вашему коду приходится работать с большим количеством объектов некой сложной библиотеки или фреймворка. Вы должны
самостоятельно инициализировать эти объекты, следить за правильным порядком зависимостей и так далее.

В результате бизнес-логика ваших классов тесно переплетается с деталями реализации сторонних классов. Такой код довольно
сложно понимать и поддерживать.

Фасад — это простой интерфейс для работы со сложной подсистемой, содержащей множество классов. Фасад может иметь
урезанный интерфейс, не имеющий 100% функциональности, которой можно достичь, используя сложную подсистему напрямую. Но
он предоставляет именно тот функционал, который нужны клиенту, и скрывает все остальные.

Фасад полезен, если вы используете какую-то сложную библиотеку со множеством подвижных частей, но вам нужна только часть
её возможностей.

К примеру, программа, заливающая видео котиков в социальные сети, может использовать профессиональную библиотеку сжатия
видео. Но все, что нужно клиентскому коду этой программы — простой метод `encode(filename, format)`. Создав класс с 
таким методом, вы реализуете свой первый фасад.

#### Фабрика

Фабричный метод — это порождающий паттерн проектирования, который определяет общий интерфейс для создания объектов в
суперклассе, позволяя подклассам изменять тип создаваемых объектов.

Представьте, что вы создаёте программу управления грузовыми перевозками. Сперва вы рассчитываете перевозить товары
только на автомобилях. Поэтому весь ваш код работает с объектами класса `Грузовик`.

В какой-то момент ваша программа становится настолько известной, что морские перевозчики выстраиваются в очередь и
просят добавить поддержку морской логистики в программу.

Отличные новости, правда?! Но как насчёт кода? Большая часть существующего кода жёстко привязана к классам `Грузовиков`.
Чтобы добавить в программу классы морских `Судов`, понадобится перелопатить всю программу. Более того, если вы потом
решите добавить в программу ещё один вид транспорта, то всю эту работу придётся повторить.

В итоге вы получите ужасающий код, наполненный условными операторами, которые выполняют то или иное действие, в
зависимости от класса транспорта.

Паттерн Фабричный метод предлагает создавать объекты не напрямую, используя оператор `new`, а через вызов особого
фабричного метода. Не пугайтесь, объекты всё равно будут создаваться при помощи `new`, но делать это будет фабричный
метод.

В этот метод можно добавить логику выбора транспортного средства, это и будет паттерн фабрика.
