import numpy as np

def query(network, node, evidence):
    
  if node in ('Burglary','Earthquake','Alarm','JohnCalls','MaryCalls'):
     #estr = join([e if evidence[e] else   for e in evidence.keys()])
     #print(evidence)
     estr = ','.join([e if evidence[e] else "¬"+e for e in evidence.keys()])
     
     estr0=estr.split(',',1)[0]
     estr1=estr.split(',',1)[1]
     #print(estr0)
     #c#####ondition_get###The way I got node name and then I can get the value of con_node possbility##############################
     con_node=0
     condition_node={}
     condition_nvalue={}
     #print("--------------------------------------------------------------")
     for e in  evidence.keys():
         #if evidence[e]:
            # print(evidence[e])
            # condition_node[i]=e
         #else:
            #print(f'¬{evidence[e]}')
         condition_node[con_node]=e
         condition_nvalue[con_node]=evidence.get(e)         
        # print(condition_node[con_node])
        # print("The value of condition node",e,"is ",condition_nvalue[con_node])
         
         con_node=con_node+1
     #print(condition_node_counter)
    # print(condition_node)
    # print(condition_node[0])
    # print(len(condition_node))
         #print(e)
     #print(condition_nvalue)
     #print(len(condition_nvalue))
         
         
     #print("--------------------------------------------------------------")
     
     ###The value of condition value has been created##################
     #c#####ondition_get###The way I got node name and then I can get the value of con_node possbility##############################
     #Alarm
     counter=len(list(network["Alarm"]["probabilities"].keys()))
     Alarm_CDP={}
     Alarm_rever_CDP={}
     for i in range(counter):
        key_para=list(network["Alarm"]["probabilities"].keys())[i]
        Alarm_CDP[f'P({network["Alarm"]["name"].lower()}:True|{network["Alarm"]["parents"]}:{list(network["Alarm"]["probabilities"].keys())[i]})']=network['Alarm']['probabilities'].get(key_para)
        reme_para=network['Alarm']['probabilities'].get(key_para)
        Alarm_rever_CDP[f'P({network["Alarm"]["name"].lower()}:False|{network["Alarm"]["parents"]}:{list(network["Alarm"]["probabilities"].keys())[i]})']=1-reme_para

     #print("The alarm is")
     #print(Alarm_CDP)
     #print(len(Alarm_CDP))
     #print(Alarm_rever_CDP)
     #print(len(Alarm_rever_CDP))
     #Earthquake
     Earthquake_CDP={}
     Earthquake_rever_CDP={}
     Earthquake_CDP[f'P({network["Earthquake"]["name"]}:True)']=network["Earthquake"]["probabilities"].get(())
     Earthquake_rever_CDP[f'P({network["Earthquake"]["name"]}:False)']=1-network["Earthquake"]["probabilities"].get(())


     #Burglary
     #print(f'P({network["Burglary"]["name"]}:True)',"=",network["Burglary"]["probabilities"].get(()))
     Burglary_CDP={}
     Burglary_rever_CDP={}
     Burglary_CDP[f'P({network["Burglary"]["name"]}:True)']=network["Burglary"]["probabilities"].get(())
     Burglary_rever_CDP[f'P({network["Burglary"]["name"]}:False)']=1-network["Burglary"]["probabilities"].get(())




     #John
     counter_John=len(list(network["JohnCalls"]["probabilities"].keys()))
     JohnCalls_CDP={}
     JohnCalls_rever_CDP={}
     for i in range(counter_John):
         key_para=list(network["JohnCalls"]["probabilities"].keys())[i]
         JohnCalls_CDP[f'P({network["JohnCalls"]["name"].lower()}:True|{network["JohnCalls"]["parents"]}:{list(network["JohnCalls"]["probabilities"].keys())[i]})']=network['JohnCalls']['probabilities'].get(key_para)
         reme_para=network['JohnCalls']['probabilities'].get(key_para)
         JohnCalls_rever_CDP[f'P({network["JohnCalls"]["name"].lower()}:False|{network["JohnCalls"]["parents"]}:{list(network["JohnCalls"]["probabilities"].keys())[i]})']=1-reme_para


     #Mary
     counter_Marry=len(list(network["MaryCalls"]["probabilities"].keys()))
     MaryCalls_CDP={}
     MaryCalls_rever_CDP={}


     for i in range(counter_Marry):
         key_para=list(network["MaryCalls"]["probabilities"].keys())[i]
         MaryCalls_CDP[f'P({network["MaryCalls"]["name"].lower()}:True|{network["MaryCalls"]["parents"]}:{list(network["MaryCalls"]["probabilities"].keys())[i]})']=network["MaryCalls"]['probabilities'].get(key_para)
         reme_para=network["MaryCalls"]['probabilities'].get(key_para)
         MaryCalls_rever_CDP[f'P({network["MaryCalls"]["name"].lower()}:False|{network["MaryCalls"]["parents"]}:{list(network["MaryCalls"]["probabilities"].keys())[i]})']=1-reme_para

     #print((list(Alarm_CDP.keys())))

     for j in range(len(list(Alarm_CDP.keys()))):
      #   print((list(Alarm_CDP.keys()))[j])
         boolean_value=(list(Alarm_CDP.keys()))[j].split(':',2)[2]
       #  print(boolean_value)
         boolean_value_judge=boolean_value.split(',',1)[0]
         boolean_value_judge_final=boolean_value_judge.split('(',1)[1]
        # print(f'The value of {boolean_value} is ',boolean_value_judge_final)

     #print(f'P({network["Burglary"]["name"]}:False)',"=",1-network["Burglary"]["probabilities"].get(()))
     #print("The Burglary CDP is ")
     #print(Burglary_CDP)
     #print("The reverse Burglary CDP is")
     #print(Burglary_rever_CDP)
     boolean_bur=list(Burglary_CDP.keys())[0].split(':',1)[1].split(')',1)[0]
     #print(boolean_bur)

     #print(f'{estr}')
     #print(estr0)
     #print(estr1)


     #if  in ('Burglary','Earthquake','Alarm','JohnCalls','MaryCalls') and estr1 in ('Burglary','Earthquake','Alarm','JohnCalls','MaryCalls'):
     #   print("The condition is ",estr0," and ",estr1)
     #   print(f'The node {node} that we need to caculate the distribution is under the condition of {estr0} and {estr1}')
     #   print(f'The node {node} that we need to caculate the distribution is under the condition of {estr0,estr1}')


     #print(f'{estr0}_CDP')
     #print(f'{node_CPD}')
     #summ=f'{estr0}_CDP'
     #print(summ)
     #print(MaryCalls_CDP)
     #summ1=f'{estr1}_CDP'
     #print(summ1)
     #print(summ.keys())
     #print(summ1.keys())
     #print(locals()[summ1])
     

     #print(condition_node[1])
     #combination_condition_node=f'{condition_node[1]}_CDP'
     #print(combination_condition_node)
     #print(locals()[combination_condition_node])
     #######
     #print("---------------------------------")
     #print(locals()["node"]) 
     #print("---------------------------------")
     #print(locals()["Alarm_CDP"])
     #print("---------------------------------")
     #print(locals()["Alarm_rever_CDP"])
     #print("---------------------------------")
     #print(locals()["Earthquake_CDP"])
     #print("---------------------------------")
     #print(locals()["Earthquake_rever_CDP"])
     #print("---------------------------------")
     #print(locals()["Burglary_CDP"])
     #print("---------------------------------")
     #print(locals()["Burglary_rever_CDP"])
     #print("---------------------------------")
     #print(locals()["JohnCalls_CDP"])
     #print("---------------------------------")
     #print(locals()["JohnCalls_rever_CDP"])
     #print("---------------------------------")
     #print(locals()["MaryCalls_CDP"])
     #print("---------------------------------")
     #print(locals()["MaryCalls_rever_CDP"])
     #print("---------------------------------")

    # print(locals()[f'{node}_CDP'])
    # print(locals()[f'{node}_rever_CDP'])
     accum_value=0
     condition_multi={}
     sum_value=0.0
     #print(condition_node)
     #print(condition_nvalue)
     #print(condition_nvalue[0])
     #print(condition_nvalue[1])
     for input_node in (f'{node}_CDP',f'{node}_rever_CDP'):
         #print("                               start                               ")
         #print(input_node)
         #sum_value=0.0
         #print(locals()[input_node].keys())
         #print(locals()[input_node])
         #print("****************************************************************")
         possi_node=list(locals()[input_node].values())[0]
         #possi_node_test=list(locals()[input_node].values())[1]
         #print("Possi is ",possi_node)
         #print(list(locals()[input_node].keys())[0].split(':',1)[1].split(')',1)[0]) 
         input_node_value=list(locals()[input_node].keys())[0].split(':',1)[1].split(')',1)[0]
         #print("The value of input_value is ",input_node_value)
         ##node true of false
         #print("****************************************************************")
         condi_combi={}
         #print("The lenght of condition node is ",len(condition_node))
         #print("The condition node is ",condition_node)
         for w in range(len(condition_node)):
             if condition_nvalue[w]==True:
                print(condition_nvalue[w])
                condi_combi[w]=f'{condition_node[w]}_CDP'
             elif condition_nvalue[w]==False:
                condi_combi[w]=f'{condition_node[w]}_rever_CDP'
                print(condition_nvalue[w])
         #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
         #print(condi_combi)
         #print(locals()[f'{condi_combi[0]}'])
         #print(len(locals()[f'{condi_combi[0]}']))
         #print(locals()[condi_combi[0]])
         #print(locals()[condi_combi[1]])
         for u in range(len(condition_node)):
                
             if u<1:
                #print("The value of A true")
                A_node_value=True
                #print(list(locals()[condi_combi[u]].values())[0])
                #print(list(locals()[condi_combi[u+1]].values())[0])
                condition_multi=list(locals()[condi_combi[u]].values())[0]*list(locals()[condi_combi[u+1]].values())[0]
                #for()
                # if node=="Earthquake":
                #print("************UUUUUUUUUUUUUUUUUUUUUUUUUUUUUU**********************************************************")
                if node=="Burglary":
                   temp_node_value=list(locals()[input_node].keys())[0].split(':',1)[1].split(')',1)[0]
                   #print(temp_node_value)
                   #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                   A_con_B_E=0.0 
                   for input_node2 in (f'Earthquake_CDP',f'Earthquake_rever_CDP'):
                       #A_con_B_E=0.0
                       #print(input_node2)
                       #print(locals()[f'{input_node2}'])
                       #print("The node2 is",input_node2.split('_',1)[0])    
                       node2=input_node2.split('_',1)[0]
                       #print(list(locals()[f'{input_node2}'].keys())[0]," ",list(locals()[f'{input_node2}'].keys())[0].split(':',1)[1].split(')',1)[0])
                       temp_node2_key=list(locals()[f'{input_node2}'].keys())[0]
                       temp_node2_value=list(locals()[f'{input_node2}'].keys())[0].split(':',1)[1].split(')',1)[0]
                       #print("The key of the node2 is ",temp_node2_key)
                       #print(temp_node2_value)
                       #print(list(locals()[f'{input_node2}'].values())[0])
                       #print(input_node)
                       #print("The possibility value of node ",node," : ",list(locals()[input_node].values())) 
                       # possi_node=list(locals()[input_node].values())
                       #print("Possi is ",possi_node)
                       #print(input_node2)
                       possi_input_node2=list(locals()[f'{input_node2}'].values())[0]
                       #print("The possibility of node2 is",possi_input_node2)
                       #print(locals()[f'input_node2'].keys())
                       #print("test:")
                       #print(locals()['Alarm_CDP'].get(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))'))
                       #print("test")    
                       #print("---------------------------------------------------------------------------------------------------------------------------")
                       #print(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))')  
                       #print("--------------------------------------------------------")  
                       #print(locals()['Alarm_CDP'].get(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))'))   
                       #print("---------------------------------------------------------------------------------------------------------------------------")
                       A_con_B_E=locals()['Alarm_CDP'].get(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))')+A_con_B_E
                       #print("The multi value is :",np.dot(np.dot(possi_node,condition_multi),possi_input_node2))                      
                   #print(" The sum of A|BE is ",A_con_B_E)
                   #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                   #print("One sum of one time",float(possi_node)*float(possi_input_node2)*float(condition_multi))
                   sum_value=float(possi_node)*float(possi_input_node2)*float(condition_multi)+sum_value
                   #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                   #print("The sum of P(B)*P(A)*Sigma(P(E)P(A|BE)))",sum_value)                      
                   #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")    
                #print("********************UUUUUUUUUUUUUUUUU***************************************************************")
             elif u>=1:
                  #print("The value of A False")
                  A_node_value=False
                  A_node_form="Alarm_rever_CDP"
                 # print(list(locals()[condi_combi[u-1]].values())[1])
                  #print(list(locals()[condi_combi[u]].values())[1])   
                  condition_multi=list(locals()[condi_combi[u-1]].values())[1]*list(locals()[condi_combi[u]].values())[1]
             #print(condition_multi)
                  #print("************UUUUUUUUUUUUUUUUUUUUUUUUUUUUUU**********************************************************")
                  if node=="Burglary":
                     temp_node_value=list(locals()[input_node].keys())[0].split(':',1)[1].split(')',1)[0]
                     # print(temp_node_value)
                     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                     A_con_B_E=0.0
                     for input_node2 in (f'Earthquake_CDP',f'Earthquake_rever_CDP'):
                         #A_con_B_E=0.0
                         #print(input_node2)
                         #print(locals()[f'{input_node2}'])
                         #print("The node2 is",input_node2.split('_',1)[0])
                         node2=input_node2.split('_',1)[0]
                         #print(list(locals()[f'{input_node2}'].keys())[0]," ",list(locals()[f'{input_node2}'].keys())[0].split(':',1)[1].split(')',1)[0])
                         temp_node2_key=list(locals()[f'{input_node2}'].keys())[0]
                         temp_node2_value=list(locals()[f'{input_node2}'].keys())[0].split(':',1)[1].split(')',1)[0]
                         #print("The key of the node2 is ",temp_node2_key)
                         #print(temp_node2_value)
                         #print(list(locals()[f'{input_node2}'].values())[0])
                         #print(input_node)
                         #print("The possibility value of node ",node," : ",list(locals()[input_node].values()))
                         #possi_node=list(locals()[input_node].values())
                         #print("Possi is ",possi_node)
                         #print(input_node2)
                         possi_input_node2=list(locals()[f'{input_node2}'].values())[0]
                         #print("The possibility of node2 is",possi_input_node2)
                         #print(locals()[f'{input_node2}'].keys())
                         ##print("test:")
                         #print(locals()[f'{A_node_form}'].get(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))'))
                         #print("test")
                         #print("---------------------------------------------------------------------------------------------------------------------------")
                         #print(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))')
                         #print("--------------------------one time for one ------------------------------")
                         #print(locals()[f'{A_node_form}'].get(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))'))
                         #print("---------------------------------------------------------------------------------------------------------------------------")
                         A_con_B_E=locals()[f'{A_node_form}'].get(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))')+A_con_B_E
                         #print("The multi value is :",np.dot(np.dot(possi_node,condition_multi),possi_input_node2))
                     #print(" The sum of A|BE is ",A_con_B_E)
                     #print(possi_node)
                     #print(possi_input_node2)
                     #print(condition_multi)
                     #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                     #sum_test=float(possi_node)*float(possi_input_node2)*float(condition_multi)+sum_value
                     #print("sum test is ",sum_test)a
                     #print("---------------------------------------------------------------------------------------------------------------------------")
                     #print(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))')
                     #print("--------------------------------------------------------")
                     #print(locals()[f'{A_node_form}'].get(f'P(alarm:{A_node_value}|[\'{node}\', \'{node2}\']:({input_node_value}, {temp_node2_value}))'))
                     #print("---------------------------------------------------------------------------------------------------------------------------")
                     #print("One sum of one time",float(possi_node)*float(possi_input_node2)*float(condition_multi)) 
                     sum_value=float(possi_node)*float(possi_input_node2)*float(condition_multi)+sum_value
                     #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                     #print("The sum of P(B)*P(A)*Sigma(P(E)P(A|BE)))",sum_value)
                  
                  
                     #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
                  #print("********************UUUUUUUUUUUUUUUUU***************************************************************")
                  
         #print("                                 end                                                      ")
     #print("The sumary of total P(B)Sigma_A((P(J|A)P(M|A))Sigma_E(P(E)P(A|BE))", sum_value)
  return sum_value   
