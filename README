#check_ips.py
Script used to query through a list of ip addresses and request Whois information

#Usage
```$ ./check_ips.py base-ips.txt```

#How-To
Vai criar um arquivo json chamado result.txt

Limpar o arquivo usando o sed:
```$ sed -f script.sed result.txt > result.json```

Usar query do jq para escolher os campos necessários:
```$ jq '.query' result.json```

Melhor query até agora:
```$ jq  '[.query,.asn_description,.asn_country_code,.entities[]] | @csv' result.json```

Substituir os caracteres especiais que estão em HEX por letras normais.

# Todo
- O arquivo json esta incorreto. Precisa usar o SED para ajustar.
