# TodoApp

**Número da Lista**: Greed<br>
**Conteúdo da Disciplina**: Algoritmos ambiciosos<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0111836  |  Luan Vasco Cavalcante |
| 18/0130889  |  Sávio Cunha de Carvalho |

## Sobre 
O meu projeto tem o objetivo de demonstrar como o algoritmo de Scheduling To Minimize Lateness impactaria uma todo list.

Na aplicação, você escolhe um nome para sua todo, um tempo de processamento, ou seja, quanto tempo (em dias) leva pra terminar a atividade e por fim uma deadline, a data que você tem que entregar a deadline.

Feito isso, uma lista surgirá na direita conforme for aumentando as suas Todo's. Há 3 botões que reorganizarão as tarefas para achar o atraso mínimo possível ao realizar todas.

## Screenshots

![alt text](https://github.com/projeto-de-algoritmos/Greed_TodoList/blob/master/media/foto1.png)
![alt text](https://github.com/projeto-de-algoritmos/Greed_TodoList/blob/master/media/foto2.png)
![alt text](https://github.com/projeto-de-algoritmos/Greed_TodoList/blob/master/media/foto3.png)
![alt text](https://github.com/projeto-de-algoritmos/Greed_TodoList/blob/master/media/foto4.png)

## Instalação 
**Linguagem**: Python<br>
**Framework**: Flask<br>
**Sistema Operacional**: Linux<br>

Para rodar o programa na sua máquina você precisa instalar :

    - Flask
    - SQLAlchemy
    - Pandas 


## Uso 
Se você preferir rodar em um ambiente virtual :

 - python3 -m venv nome_env
 - source nome_env/bin/activate

Comandos em ordem :

 - pip install Flask
 - pip install -U Flask-SQLAlchemy
 - pip install pandas
 - export FLASK_APP=todo
 - flask run
 
Depois é só acessar : localhost:5000


## Outros 
O esqueleto da aplicação foi tirado do vídeo : https://www.youtube.com/watch?v=yKHJsLUENl0




