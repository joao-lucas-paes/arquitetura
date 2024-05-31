# Requisitos para rodar os codigos:

## Plot:
- Python 3.8
    
    Na pasta do plot rode:

~~~ shell
    pip install -r requirements.txt
~~~

## Testes:
- Docker
- Cmake
- Sniper-sim benchmark splash 2 (No site do Sniper-Sim pode-se achar uma versao do mesmo com os benchmarks disponiveis, contudo, apenas o splash 2 esta implementado e algumas de suas aplicacoes nao estao funcionando como deveriam, contudo os scripts disponibilizados neste repositorio filtram os problemas).

    Ao rodar o codigo seu terminal provavelmente vai abrir o docker, apos isso, monte a pasta splash 2 do seu docker para uma pasta do seu usuario,a desta maneira assim que for rodando os seus dados serao salvos em sua pasta montada (contudo, pode-se ignorar isso caso rode os comandos no container e realize um commit, no entretanto, execute isso por sua conta e risco). ao montar a pasta splash passe o arquivo run.sh e o arquivo de teste auxiliar para a pasta montada. Dentro do container coloque os dois arquivos na pasta do sniper-sim e rode! (Talvez seja necessario alterar o acesso de permissoes do script, para isso use um chmod 777 run.sh).

<br/><br/><br/>


PS: Os codigos foram todos rodados e testados em um Ubuntu 22.04 LTS, todavia, devido ao docker muito possivelmente o Windows e outras distros linux devem suportar, contudo vale ressaltar que ao testar em um Zorin OS 16.3, mesmo com o docker nao foi possivel 