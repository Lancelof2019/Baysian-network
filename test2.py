counter=len(list(network["Alarm"]["probabilities"].keys()))

    print("counter is ",counter)

    A_CDP={}
    A_rever_CDP={}
    for i in range(counter):
       key_para=list(network["Alarm"]["probabilities"].keys())[i]
       print("The key is :",key_para)
       print(f'P({network["Alarm"]["name"].lower()}',":True","|",f'{network["Alarm"]["parents"]}'":",list(network["Alarm"]["probabilities"].keys())[i],")=",network['Alarm']['probabilities'].get(key_para))
       A_CDP[f'P({network["Alarm"]["name"].lower()}:True|{network["Alarm"]["parents"]}:{list(network["Alarm"]["probabilities"].keys())[i]})']=network['Alarm']['probabilities'].get(key_para)
       reme_para=network['Alarm']['probabilities'].get(key_para)
       print("rempara is ",reme_para)
       #print("The poosite para is: ",1-reme_para)
       A_rever_CDP[f'P({network["Alarm"]["name"].lower()}:False|{network["Alarm"]["parents"]}:{list(network["Alarm"]["probabilities"].keys())[i]})']=1-reme_para
