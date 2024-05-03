grammar={}
new_grammar={}

with open('input.txt', 'r') as f:
    for line in f:
        non_terminal,productions=line.strip().split('->')
        productions=productions.split('|')
        grammar[non_terminal.strip()] = productions





for non_terminal,rules in grammar.items():
    check=0
    remaining_rules=[ r for r in rules if not r.startswith(non_terminal)]
    p=[]
    for rule in rules:
        if rule.startswith(non_terminal):
            check=1
            new_symbol=non_terminal+"'"
            o=[]
            p.append(rule[1:]+new_symbol)
            for _ in remaining_rules:
                o.append(_+new_symbol)
            new_grammar[non_terminal]='|'.join(o)
    if(check):
        new_grammar[new_symbol]='|'.join(p)+'|$'
    else:
        new_grammar[non_terminal]='|'.join(remaining_rules)

file=open('./output.txt', 'w')
for a,b in new_grammar.items():
    file.write(a+'->'+b+'\n')
file.close()
print("Output written in output.txt")