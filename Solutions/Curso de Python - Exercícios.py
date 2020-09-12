#!/usr/bin/env python
# coding: utf-8

# # Curso relâmpago de Python - Exercícios
# 
# Este é um exercício opcional para testar sua compreensão sobre o Python Basics. Se você achar isso extremamente desafiador, então você provavelmente ainda não está pronto para o resto deste curso e não tem experiência de programação suficiente para continuar. Eu sugiro que você faça outro curso mais orientado para iniciantes, como [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp)

# ## Exercícios
# 
# Responda as perguntas ou complete as tarefas descritas em negrito abaixo, use o método específico, se aplicável.

# ** Quanto é 7 elevado na potência 4?**

# In[1]:


7**4


# ** Quebre a seguinte string em uma lista:**
# 
#     s = "Olá, Pai!"

# In[4]:


s = "Olá, Pai!"
print(s.split())


# ** Dada as variáveis:**
# 
#     Planeta = "Terra"
#     Diametro = 12742
# 
# ** Use .format() para printar a seguinte frase: **
# 
#     O diâmetro da terra é de 12742 kilômetros.

# In[7]:


planeta = "Terra"
diametro = 12742

#print("O diâmetro da {p} é de {d} quilomêtros.".format(p = planeta, d = diametro))
print("O diâmetro da %s é de %d quilomêtros." % (planeta, diametro))


# ** Dada a lista abaixo, use indexação para obter apenas a string "ola". **

# In[14]:


lst = [1,2,[3,4],[5,[100,200,['olá']],23,11],1,7]


# In[18]:


index = lst.index("olá")


# In[16]:


print(lst[3][1][2])


# ** Dado o seguinte dicionário aninhado, extraia a palavra "hello" **

# In[19]:


d = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}


# In[29]:


d["k1"][3]["café"][3]["alvo"][3]


# ** Qual a principal diferença entre um dicionário e uma tupla? **

# In[3]:


O dicionário é mutavél.


# ** Construa uma função que retire o domínio dado um e-mail no seguinte formato: **
# 
#     user@domain.com
#     
# **Por exemplo, passando como parâmetro "user@domain.com" retornaria: domain.com**

# In[31]:


dominio = "leobandeiraf@gmail.com"


# In[42]:


dominio.split("@")[-1]


# ** Crie uma função básica que retorna True se a palavra 'dog' estiver contida na string de entrada. Não se preocupe com os casos de extremos, como uma pontuação que está sendo anexada à palavra cão, mas que seja senível à caixa. **

# In[69]:


def encontreCachorro(string):
    return "cachorro" in string.lower().split()


# In[71]:


string = "Existe um cachorro ai?"

if encontreCachorro(string):
    print(True)
else:
    print(False)


# ** Crie uma função que conta o número de vezes que a palavra "dog" ocorre em uma string. Novamente ignore os casos extremos. **

# In[88]:


def contaCachorro(string):
    count = 0
    
    for palavra in string.lower().split():
        if palavra == "cachorro":
            count += 1
    return count


# In[90]:


string = "Esse cachorro é mais rápido que o outro cachorro"

print(contaCachorro(string))


# ** Use expressões lambda e a função filter () para filtrar as palavras de uma lista que não começa com a letra 's'. Por exemplo: **
# 
#     seq = ['sopa','cachorro','salada','gato','ótimo']
# 
# ** Deveria ser filtrado para:**
# 
#     ['sopa','salada']

# In[91]:


seq = ['sopa','cachorro','salada','gato','ótimo']


# In[94]:


list(filter(lambda x: x[0] == "s", seq))


# ### Problema final
# ** Você está dirigindo um pouco rápido demais, e um policial para você. Escreva uma função para retornar um dos 3 resultados possíveis: "Sem multa", "Pequena multa" ou "Multa Grande".
#    Se a sua velocidade for igual ou inferior a 60, o resultado é "Sem multa". Se a velocidade for entre 61 e 80 inclusive, o resultado é "Multa Pequena". Se a velocidade é de 81 ou mais, o resultado é "Multa Grande". A menos que seja seu aniversário (codificado como um valor booleano nos parâmetros da função) - em seu aniversário, sua velocidade pode ser 5 maior em todos os casos. **

# In[96]:


def capturar_velocidade(speed, birthday):
    
    if birthday:
        speed = speed - 5
    else:
        speed = speed
        
    if speed <= 60:
        return("Sem multa")
    elif speed > 61 and speed <= 80:
        return("Multa Pequena")
    else:
        return("Multa Grande")


# 

# In[99]:


capturar_velocidade(65,True)


# In[98]:


capturar_velocidade(81,False)

