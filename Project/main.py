
def smthtoten(n,s):
  n=str(n)
  a10,t=0,0
  for i in range(len(n)):
    t=str(n[len(n)-i-1])
    if is_number(t): a10+=int(t)*s**i
    else:
      temp=int(retrans(t))
      a10+=temp*s**i
  return int(a10)
def is_number(n):
  return  n.isdigit()
def trans(n):
  a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
  return a[n-10]
def retrans(n):
  a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
  for i in range(len(a)):
    if (a[i]==n): return i+10
def tentosmth(n,s):
  a=[]
  s=int(s)
  while n!=0:
    t=str(int(n)%s)
    if int(t)>9: t=trans(int(t))
    a.append(t)
    n//=s
  a.reverse()
  numb=''.join(a)
  return numb
def smthtosmth(n,s,sn):
  return tentosmth(int(smthtoten(n,int(s))),int(sn))
def summ(a,at,b,bt,r):
  summ=smthtoten(a,at)+smthtoten(b,bt)
  return tentosmth(summ,r)
def diff(a,at,b,bt,r):
  diff=smthtoten(a,at) - smthtoten(b,bt)
  return tentosmth(diff,r)
def mult(a,at,b,bt,r):
  mult=smthtoten(a,at)*smthtoten(b,bt)
  return tentosmth(mult,r)
def findint(n):
  n=n.replace('(',' ')
  n=n.replace(')','')
  s1,s2='',''
  for i in range(len(n)):
    if n[i]!=' ':
     s1+=n[i]
    else:
      t=i
      break
  for i in range(t,len(n)):
    s2+=n[i]
  s1,s2=int(s1),int(s2)
  return s1,s2
def nsp(m, r):
  n=[str(i) for i in m.split()]
  s=n[1]
  if s!='=':
    a,at=findint(n[0])
    b,bt=findint(n[2])
    if s=='+': return(summ(a,at,b,bt,r))  
    elif s=='-': return (diff(a,at,b,bt,r))
    elif s=='*': return(mult(a,at,b,bt,r))
  else: 
    a,at=findint(n[0])
    return tentosmth(int(smthtoten(a,int(at))),int(n[2]))