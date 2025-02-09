# Motivação

Motivava-se da atividade da disciplina de Auditoria e Pericia Forense Computacional, no qual foi utilizado para identificar se algum arquivo foi alterado dado um quantidade determinada de arquivos, no caso desse desafio imagens.


## Desenvolvimento

Visto que queremos utilizar a comparação entre arquivo(s) que sejam e achar se existe arquivos diferentes da maioria deles. Dado essa informações, pensamos logo de incio em utilizar Hash, mas um das limitações em vista quando se trata de comparação é a possibilidade de colisão de informações. Desta forma, foi implementado o motodo utilizando a comparação por byte que atende as limitações deixadas pelo algoritmos de hash, mas claro apresenta suas desvantagens quando se trata de escalabilidade e dependendo da quantidade de arquivos, pois existe o grande esforço para verificação neessitando de alto poder computacional.

- **Execução:**  
  Basta alterar o valor da variável `pasta` para o caminho desejado, salvar o script e executá-lo com o comando:

  ```bash
  python seu_script.py
